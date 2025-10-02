"""Simulation commands."""

from __future__ import annotations

import re
import time
from pathlib import Path
from typing import Annotated

import typer
import httpx
from rich import print as rprint
from rich.live import Live
from rich.text import Text

from veris_cli.config import load_config, save_config
from veris_cli.loaders import load_scenarios
from veris_cli.run_models import RunStatus
from veris_cli.runner import SimulationRunner
from veris_cli.runs import RunsStore
from veris_cli.errors import UpstreamServiceError, ConfigurationError
from veris_cli.api import ApiClient
from veris_cli.fs import ensure_veris_dir
from veris_cli.run_models import V3Run, V3SessionEntry, V3SessionStatus

sim_app = typer.Typer(add_completion=False, no_args_is_help=False)


def _select_scenarios(
    scenarios: list[dict],
    ids: list[str] | None = None,
    use_cases: list[str] | None = None,
) -> list[dict]:
    """Select scenarios."""
    selected = scenarios
    if use_cases:
        use_set = set(use_cases)
        selected = [
            s for s in selected if s.get("skeleton_metadata", {}).get("use_case_name") in use_set
        ]
    if ids:
        id_set = set(ids)
        selected = [s for s in selected if s.get("scenario_id") in id_set]
    return selected


def _colorize_status(text: str) -> str:
    """Add Rich markup colors to status keywords in a status string."""
    mapping = {
        "pending": "yellow",
        "running": "cyan",
        "completed": "green",
        "failed": "red",
    }

    def _repl(match: re.Match[str]) -> str:
        word = match.group(0)
        color = mapping.get(word.lower())
        return f"[{color}]{word}[/]" if color else word

    return re.sub(
        r"\b(pending|running|completed|failed)\b",
        _repl,
        text,
        flags=re.IGNORECASE,
    )


def query_run(
    agent_id: str, run_id: str, *, live: Live | None = None, header_prefix: str | None = None
) -> V3Run:
    """Load run, fetch latest sessions/logs/details, grade if terminal, save and display.

    If ``live`` is provided, updates the Live display instead of printing new lines.
    ``header_prefix`` (e.g., elapsed time) is prepended when rendering output.
    """
    project_dir = Path.cwd()
    veris_dir = ensure_veris_dir(project_dir)
    store = RunsStore(project_dir)
    api = ApiClient()

    try:
        run = store.load_v3_run(run_id)
    except ConfigurationError as e:
        rprint(f"[red]{str(e)}[/red]")
        raise typer.Exit(code=1)

    # Fetch agent evaluation config (best-effort)
    try:
        agent_full = api.v3_get_agent(agent_id)
        graders_dict = agent_full.get("evaluation_config") if isinstance(agent_full, dict) else None
    except Exception:
        graders_dict = None

    def _grader():
        if isinstance(graders_dict, dict) and graders_dict:
            return next(iter(graders_dict.values()))
        return None

    sessions = api.v3_list_sessions(agent_id, run_id)
    session_map = {s.session_id: s for s in run.sessions}
    for s in sessions:
        sess_id = s.get("session_id")
        if not sess_id:
            continue
        entry = session_map.get(sess_id)
        status_str = s.get("status", "FAILED")
        status_enum = V3SessionStatus(status_str)
        if entry is None:
            entry = V3SessionEntry(
                session_id=sess_id,
                scenario_id=s.get("scenario_id", ""),
                status=status_enum,
            )
            run.sessions.append(entry)
            session_map[sess_id] = entry
        else:
            entry.status = status_enum

        try:
            logs = api.v3_get_session_logs(agent_id, run_id, sess_id)
            if isinstance(logs, list):
                entry.logs = logs
        except UpstreamServiceError:
            pass

        try:
            details = api.v3_get_session_details(agent_id, run_id, sess_id)
            if isinstance(details, dict):
                entry.details = details
        except UpstreamServiceError:
            pass

        # Grade once terminal
        if entry.status in (V3SessionStatus.completed, V3SessionStatus.failed):
            has_eval = False
            if isinstance(entry.details, dict):
                ev = entry.details.get("evaluation")
                if isinstance(ev, dict) and ("results" in ev or "error" in ev):
                    has_eval = True
            if not has_eval and _grader() and isinstance(entry.logs, list):
                try:
                    result = api.grade(_grader(), entry.logs)
                    entry.details.setdefault("evaluation", {})["results"] = result
                except Exception as e:
                    entry.details.setdefault("evaluation", {})["error"] = str(e)

    all_terminal = (
        all(s.status in (V3SessionStatus.completed, V3SessionStatus.failed) for s in run.sessions)
        and len(run.sessions) > 0
    )
    run.status = V3SessionStatus.completed if all_terminal else V3SessionStatus.in_progress

    # If all sessions have completed/failed, start and poll evaluations for the run
    evaluation_results: dict[str, dict] | None = None
    if run.status == V3SessionStatus.completed:
        try:
            start = api.v3_start_evaluations(agent_id, run.run_id)
            eval_run_id = start.get("evaluation_run_id")
            if eval_run_id:
                # Poll until evaluation run completes or times out
                while True:
                    ev = api.v3_get_evaluations(agent_id, eval_run_id)
                    status = ev.get("status")
                    # Map results by session_id for easier merge into display
                    ses = ev.get("session_evaluations") or []
                    evaluation_results = {
                        x.get("session_id"): x for x in ses if isinstance(x, dict)
                    }
                    if status in ("COMPLETED", "FAILED"):
                        break
                    time.sleep(1.0)
        except Exception as e:
            # Best-effort evaluations; keep going if they fail
            rprint(f"[yellow]Evaluations error: {e}[/yellow]")

    # Attach evaluation summaries to session details for display
    if isinstance(evaluation_results, dict):
        for entry in run.sessions:
            ev = evaluation_results.get(entry.session_id)
            if isinstance(ev, dict):
                entry.details.setdefault("evaluation", {})["results"] = ev.get("result", {})
                if err := ev.get("error"):
                    entry.details.setdefault("evaluation", {})["error"] = err

    store.save_run(run)

    # Render concise status
    lines: list[str] = []
    lines.append("Run file: " + str(veris_dir.joinpath("runs", run.run_id + ".json")))

    if header_prefix:
        lines.append(header_prefix.rstrip("\n"))
    lines.append(f"Run {run.run_id} - {run.status.value}")
    by_scenario: dict[str, list[V3SessionEntry]] = {}
    for entry in run.sessions:
        key = entry.scenario_id or "unknown"
        by_scenario.setdefault(key, []).append(entry)
    for scen_id, entries in by_scenario.items():
        lines.append(f"  [bold cyan]Scenario[/bold cyan] [bold]{scen_id}[/bold]")
        for entry in entries:
            lines.append(
                f"    Session {entry.session_id}: {entry.status.value} ({len(entry.logs)} logs)"
            )
            ev = entry.details.get("evaluation") if isinstance(entry.details, dict) else None
            if isinstance(ev, dict):
                result_obj = ev.get("results")
                error_msg = ev.get("error")
                if error_msg:
                    lines.append(f"      [red]eval error:[/red] {error_msg}")
                if isinstance(result_obj, dict) and result_obj:
                    # Pretty print compact JSON-like dict for results
                    import json as _json

                    lines.append("      [green]eval results:[/green]")
                    lines.append("        " + _json.dumps(result_obj, ensure_ascii=False, indent=4))

    rendered = "\n".join(lines)
    if live is not None:
        live.update(Text.from_markup(rendered))
    else:
        rprint(Text.from_markup(rendered))

    return run


@sim_app.command("launch")
def launch(
    agent: Annotated[
        Path | None,
        typer.Option("--agent", help="Path to agent.json"),
    ] = None,
    scenarios: Annotated[
        list[str] | None,
        typer.Option("--scenarios", help="Scenario IDs to run"),
    ] = None,
    use_cases: Annotated[
        list[str] | None,
        typer.Option("--use-cases", help="Filter by use_case_name"),
    ] = None,
    watch: Annotated[
        bool,
        typer.Option(
            "--watch",
            help="Continuously poll status until simulations and evals complete",
        ),
    ] = False,
):
    """Launch a simulation."""
    project_dir = Path.cwd()
    veris_dir = project_dir / ".veris"
    scenarios_dir = veris_dir / "scenarios"

    all_scenarios = load_scenarios(scenarios_dir)
    selected_scenarios = _select_scenarios(all_scenarios, scenarios, use_cases)

    if not selected_scenarios:
        rprint("[red]No scenarios selected[/red]")
        raise typer.Exit(code=1)

    store = RunsStore(project_dir)
    runner = SimulationRunner(store)

    # Load agent configuration from .veris/config.json, if available
    cfg = load_config(project_dir)
    agent_payload = None
    if getattr(cfg, "agent", None) is None:
        # Provide actionable guidance if no agent connection configured
        raise ConfigurationError(
            message=(
                "Agent endpoint is not configured in .veris/config.json (missing 'agent' block)."
            ),
            hint=(
                "Run 'veris setup ...' to detect your public URL automatically, or set it manually "
                "with 'veris config public_url https://<your-ngrok>.ngrok.io'."
            ),
            file_path=str(veris_dir / "config.json"),
            command_suggestion="veris setup  # or: veris config public_url https://...",
        )
    else:
        # Validate MCP endpoint itself is reachable.
        # We treat 2xx–4xx as a signal that the server is up (e.g., 400/405 on GET),
        # and only fail on network errors/timeouts or 5xx.
        mcp_url = cfg.agent.mcp_url.rstrip("/")

        per_attempt_timeout = 5.0
        attempts = 3
        last_status_details: list[str] = []
        last_exception: Exception | None = None
        reachable = False

        for attempt in range(attempts):
            try:
                resp = httpx.get(mcp_url, timeout=per_attempt_timeout, follow_redirects=True)
                if resp.status_code < 500:
                    # 2xx–4xx considered OK for liveness
                    reachable = True
                    break
                else:
                    last_status_details.append(f"{mcp_url} -> {resp.status_code}")
            except httpx.RequestError as exc:
                last_exception = exc
                last_status_details.append(f"{mcp_url} -> request error: {exc.__class__.__name__}")
            time.sleep(0.4 * (attempt + 1))

        if not reachable:
            hint_lines = [
                f"Tried MCP endpoint: {mcp_url}.",
                "Ensure your FastAPI app is running and ngrok tunnel is active.",
                "Run 'veris setup ...' or set a working public URL.",
            ]
            if last_status_details:
                hint_lines.insert(1, "Checks: " + "; ".join(last_status_details))
            raise ConfigurationError(
                message="Unable to reach configured agent MCP URL.",
                hint=" ".join(hint_lines),
                file_path=str(veris_dir / "config.json"),
                command_suggestion="veris setup  # or: veris config public_url https://...",
            ) from last_exception

        # Convert Pydantic model to plain dict for payload
        agent_payload = cfg.agent.model_dump()  # type: ignore[assignment]

    run = runner.launch(selected_scenarios, agent=agent_payload)

    print("Run file: ", veris_dir.joinpath("runs", run.run_id + ".json"))

    if watch:
        try:
            with Live("", refresh_per_second=4, transient=False) as live:
                while True:
                    time.sleep(2.0)
                    try:
                        run = runner.poll_once(run)
                    except UpstreamServiceError as e:
                        rprint(f"[red]{str(e)}[/red]")
                        raise typer.Exit(code=1)
                    base = runner.format_status(run)
                    colored = _colorize_status(base)
                    header = "[cyan]Watching run status. Press Ctrl+C to stop.[/cyan]"
                    live.update(Text.from_markup(header + "\n" + colored))
                    # Done when all evals have reached a terminal state
                    all_evals_terminal = all(
                        getattr(sim, "evaluation_status", None)
                        in (
                            RunStatus.completed,
                            RunStatus.failed,
                        )
                        for sim in run.simulations
                    )
                    if all_evals_terminal:
                        live.update(
                            Text.from_markup(
                                header
                                + "\n"
                                + colored
                                + "\n[green]All simulations and evaluations are complete.[/green]"
                            )
                        )
                        break
        except KeyboardInterrupt:
            rprint(
                "[yellow]Stopped watching. Check later with: "
                f"veris sim status --run {run.run_id}[/yellow]"
            )
    else:
        rprint(runner.format_status(run))


@sim_app.command("status")
def status(
    run_id: str = typer.Option(..., "--run", help="Run ID"),
):
    """Get the status of a simulation."""
    store = RunsStore(Path.cwd())
    runner = SimulationRunner(store)
    try:
        run = store.load_run(run_id)
    except ConfigurationError as e:
        rprint(f"[red]{str(e)}[/red]")
        raise typer.Exit(code=1)
    try:
        run = runner.poll_once(run)
    except UpstreamServiceError as e:
        rprint(f"[red]{str(e)}[/red]")
        raise typer.Exit(code=1)
    rprint(runner.format_status(run))


@sim_app.command("query", help="Query and update a V3 run once")
def query(
    agent_id: Annotated[str, typer.Option("--agent-id", help="Agent ID")],
    run_id: Annotated[str, typer.Option("--run-id", help="Run ID")],
):
    """Single refresh of a V3 run: fetch sessions/logs/details/grades, save, and display."""
    query_run(agent_id, run_id)


@sim_app.command("results")
def results(
    run_id: Annotated[str, typer.Option("--run", help="Run ID")],
    json_out: Annotated[bool, typer.Option("--json", help="Output JSON")] = False,
):
    """Print evaluation_results for all sessions in the run."""
    store = RunsStore(Path.cwd())
    try:
        run = store.load_run(run_id)
    except ConfigurationError as e:
        rprint(f"[red]{str(e)}[/red]")
        raise typer.Exit(code=1)

    simulations = [
        {
            "scenario_id": sim.scenario_id,
            "simulation_id": sim.simulation_id,
            "eval_id": sim.eval_id,
            "evaluation_results": sim.evaluation_results or {},
        }
        for sim in run.simulations
    ]

    if json_out:
        import json as _json

        rprint(
            _json.dumps(
                {"run_id": run.run_id, "simulations": simulations},
                indent=2,
                ensure_ascii=False,
            )
        )
        return

    # Default human-readable output
    rprint(f"[bold]Run[/bold] {run.run_id}")
    for item in simulations:
        scen = item["scenario_id"]
        sid = item["simulation_id"]
        rprint(f"- [cyan]{scen}[/cyan] ({sid})")
        rprint(item["evaluation_results"])  # prints dict or empty


@sim_app.command("kill")
def kill(simulation_id: str):
    """Kill a simulation."""
    from veris_cli.api import ApiClient

    api = ApiClient()
    api.kill_simulation(simulation_id)
    rprint(f"[yellow]Requested kill for simulation {simulation_id}[/yellow]")


@sim_app.command("eval-kill")
def eval_kill(eval_id: str):
    """Kill an evaluation."""
    from veris_cli.api import ApiClient

    api = ApiClient()
    api.kill_evaluation(eval_id)
    rprint(f"[yellow]Requested kill for evaluation {eval_id}[/yellow]")


@sim_app.command("v3launch")
def v3launch(
    agent_id: Annotated[
        str | None,
        typer.Option("--agent-id", help="Agent ID"),
    ] = None,
    agent_version: Annotated[
        str | None,
        typer.Option("--agent-version", help="Agent version to use (e.g., v1.2.3)"),
    ] = None,
    scenario_set_id: Annotated[
        str | None,
        typer.Option("--scenario-set-id", help="Scenario set ID to use"),
    ] = None,
    watch: Annotated[
        bool,
        typer.Option(
            "--watch",
            help="Continuously poll status until simulations complete",
        ),
    ] = False,
):
    """Launch full V3 flow rooted on agent_id with interactive version selection.

    Flow:
    - Resolve agent_id: CLI option > .veris/config.json > prompt user and save
    - Fetch available versions and prompt numeric selection (default: latest)
    - Select or generate a scenario set, fetch scenarios and start simulation
    """
    project_dir = Path.cwd()
    veris_dir = ensure_veris_dir(project_dir)
    scenarios_dir = veris_dir / "scenarios"
    scenarios_dir.mkdir(exist_ok=True)

    api = ApiClient()

    # =========================
    # Resolve agent_id from CLI > config > prompt and save
    # =========================
    cfg = load_config(project_dir)
    if agent_id:
        # Validate provided agent_id exists, then update config and inform user
        try:
            _ = api.v3_get_agent(agent_id)
        except UpstreamServiceError as e:
            rprint(f"[red]Provided agent_id is invalid: {e}[/red]")
            raise typer.Exit(code=1)
        cfg.agent_id = agent_id
        save_config(project_dir, cfg, overwrite=True)
        rprint(f"[green]Updated .veris/config.json with agent_id[/green] {agent_id}")
    else:
        if cfg.agent_id:
            agent_id = cfg.agent_id
        else:
            entered = typer.prompt("Enter agent_id")
            if not entered.strip():
                rprint("[red]agent_id is required[/red]")
                raise typer.Exit(code=1)
            agent_id = entered.strip()
            cfg.agent_id = agent_id
            save_config(project_dir, cfg, overwrite=True)
            rprint(f"[green]Saved agent_id to .veris/config.json[/green] {agent_id}")

    rprint(f"[green]Agent ready[/green] {agent_id}")

    # =========================
    # Fetch versions and select (CLI override via --agent-version, else interactive)
    # =========================
    versions = api.v3_list_agent_versions(agent_id)  # type: ignore[arg-type]
    version_id: str | None = None
    if not isinstance(versions, list) or len(versions) == 0:
        rprint("[red]No versions found for this agent.[/red]")
        raise typer.Exit(code=1)

    if agent_version:
        found = next((v for v in versions if v.get("version") == agent_version), None)
        if not found:
            rprint(f"[red]Specified --agent-version not found[/red] {agent_version}")
            raise typer.Exit(code=1)
        version_id = agent_version
        rprint(f"[green]Using agent version[/green] {version_id}")
    else:
        rprint("[bold]Available versions[/bold]")
        for idx, v in enumerate(versions, start=1):
            ver = v.get("version", "unknown")
            msg = v.get("commit_message") or v.get("message") or ""
            created = v.get("created_at") or ""
            rprint(f"  {idx}. {ver}  {msg}  {created}")
        default_index = len(versions)
        choice_str = typer.prompt(
            "Select version number (default latest)", default=str(default_index)
        )
        try:
            choice = int(choice_str)
            if choice < 1 or choice > len(versions):
                choice = default_index
        except Exception:
            choice = default_index
        selected = versions[choice - 1]
        version_id = selected.get("version")
    if not version_id:
        rprint("[red]Unable to resolve version for agent[/red]")
        raise typer.Exit(code=1)

    # =========================
    # V3: SCENARIO SET (interactive: default latest)
    # =========================
    selected_scenario_set_id: str | None = scenario_set_id
    scenario_sets = api.v3_list_scenario_sets(agent_id)  # type: ignore[arg-type]

    # If provided via flag, validate and use directly
    if selected_scenario_set_id:
        found_ss = next(
            (ss for ss in scenario_sets if ss.get("scenario_set_id") == selected_scenario_set_id),
            None,
        )
        if not found_ss:
            rprint(f"[red]Specified --scenario-set-id not found[/red] {selected_scenario_set_id}")
            raise typer.Exit(code=1)
        if found_ss.get("status") == "IN_PROGRESS":
            rprint("[red]Specified scenario set is still IN_PROGRESS[/red]")
            raise typer.Exit(code=1)
        rprint(f"[green]Using scenario set[/green] {selected_scenario_set_id}")
    else:
        rprint("[bold]Scenario sets[/bold]")
        rprint("  0. Generate new scenario set")
        if isinstance(scenario_sets, list) and len(scenario_sets) > 0:
            for idx, ss in enumerate(scenario_sets, start=1):
                sid = ss.get("scenario_set_id", "unknown")
                dimension_names_list = list(ss.get("actual_dimensions", {}).keys())
                created = ss.get("created_at", "")
                n = ss.get("scenarios_generated") or ss.get("num_scenarios") or ""
                rprint(f"  {idx}. {sid} n={n} {created}")
                if dimension_names_list:
                    rprint(f"    Dimensions: {dimension_names_list}")
                if ss.get("description"):
                    rprint(f"    {ss.get('description')}")

        default_choice = "1"
        if len(scenario_sets):
            choice_str = typer.prompt(
                "Select scenario set (default latest)", default=default_choice
            )
        else:
            choice_str = "0"
        try:
            choice = int(choice_str)
        except Exception:
            choice = 1

        if choice == 0:
            body = {"version_id": version_id, "dimensions": {}, "num_scenarios": 3}  # type: ignore[arg-type]
            with Live(
                "[cyan]Creating scenario set...[/cyan]", refresh_per_second=4, transient=False
            ) as live:
                ss = api.v3_create_scenario_set(agent_id, body)  # type: ignore[arg-type]
                time.sleep(0.5)
                selected_scenario_set_id = ss.get("scenario_set_id")
                if not selected_scenario_set_id:
                    rprint("[red]Scenario set creation failed[/red]")
                    raise typer.Exit(code=1)
                live.update(
                    Text.from_markup(f"[green]Scenario set[/green] {selected_scenario_set_id}")
                )
            with Live(
                "[cyan]Waiting for scenarios to generate...[/cyan]",
                refresh_per_second=4,
                transient=False,
            ) as live:
                status = "IN_PROGRESS"
                gen_start = time.time()
                for _ in range(120):
                    details = api.v3_get_scenario_set(agent_id, selected_scenario_set_id)  # type: ignore[arg-type]
                    status = details.get("status", status)
                    elapsed = int(time.time() - gen_start)
                    live.update(
                        Text.from_markup(
                            f"Scenario set status: [bold]{status}[/bold] (elapsed: {elapsed}s)"
                        )
                    )
                    if status != "IN_PROGRESS":
                        break
                    time.sleep(2.0)
                elapsed = int(time.time() - gen_start)
                if status == "IN_PROGRESS":
                    rprint(
                        f"[red]Scenario set generation failed after {elapsed}s: still IN_PROGRESS[/red]"
                    )
                    raise typer.Exit(code=1)
            time.sleep(0.5)
        if choice != 0:
            if not isinstance(scenario_sets, list) or choice < 1 or choice > len(scenario_sets):
                rprint("[red]Invalid selection for scenario set[/red]")
                raise typer.Exit(code=1)
            selected_ss = scenario_sets[choice - 1]
            selected_scenario_set_id = selected_ss.get("scenario_set_id")
            if not selected_scenario_set_id:
                rprint("[red]Selected scenario set missing id[/red]")
                raise typer.Exit(code=1)
            status = selected_ss.get("status")
            if status == "IN_PROGRESS":
                rprint("[red]Selected scenario set is still IN_PROGRESS[/red]")
                raise typer.Exit(code=1)
            rprint(f"[green]Using scenario set[/green] {selected_scenario_set_id}")

    # Clear scenarios directory
    for file in scenarios_dir.glob("*.json"):
        file.unlink()

    # Save scenarios locally
    import json as _json

    scenarios = api.v3_list_scenarios(agent_id, selected_scenario_set_id)  # type: ignore[arg-type]
    for sc in scenarios:
        sid = sc.get("scenario_id")
        if not sid:
            continue
        (scenarios_dir / f"{sid}.json").write_text(_json.dumps(sc, indent=2), encoding="utf-8")

    # =========================
    # V3: START SIMULATION
    # =========================
    with Live(
        "[cyan]Starting simulation run...[/cyan]", refresh_per_second=4, transient=False
    ) as live:
        sim = api.v3_start_simulation(
            agent_id,
            {"version_id": version_id, "scenario_set_id": selected_scenario_set_id},  # type: ignore[arg-type]
        )
        run_id = sim.get("run_id")
        if not run_id:
            rprint("[red]Failed to start simulation run[/red]")
            raise typer.Exit(code=1)
        live.update(Text.from_markup(f"[green]Run created[/green] {run_id}"))

    run = V3Run(
        run_id=run_id,
        created_at=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        status=V3SessionStatus.in_progress,
        agent_id=agent_id,  # type: ignore[arg-type]
        version_id=version_id,  # type: ignore[arg-type]
        scenario_set_id=selected_scenario_set_id,  # type: ignore[arg-type]
        sessions=[],
    )
    store = RunsStore(project_dir)
    store.save_run(run)  # type: ignore[arg-type]

    # =========================
    # V3: WATCH LOOP
    # =========================
    if watch:
        try:
            sim_start = time.time()

            def _fmt_secs(total: int) -> str:
                mins, secs = divmod(total, 60)
                hours, mins = divmod(mins, 60)
                return f"{hours:d}:{mins:02d}:{secs:02d}"

            with Live("", refresh_per_second=4, transient=False) as live:
                while True:
                    elapsed = int(time.time() - sim_start)
                    header = f"[cyan]Elapsed:[/cyan] {_fmt_secs(elapsed)}"
                    run = query_run(agent_id, run_id, live=live, header_prefix=header)  # type: ignore[arg-type]
                    if run.status in (V3SessionStatus.completed, V3SessionStatus.failed):
                        total = int(time.time() - sim_start)
                        footer = f"[green]All sessions completed in {_fmt_secs(total)}[/green]"
                        live.update(Text.from_markup(header + "\n" + footer))
                        break
                    time.sleep(2.0)
        except KeyboardInterrupt:
            rprint(
                "[yellow]Stopped watching. Check later with: "
                f"veris sim status --run {run.run_id}[/yellow]"
            )
    else:
        query_run(agent_id, run_id)  # type: ignore[arg-type]


@sim_app.command("create", help="Create agent or agent version")
def create_agent(
    agent_path: Annotated[
        Path | None,
        typer.Option("--agent-path", help="Path to agent.json for new agent or version"),
    ] = None,
    agent_id: Annotated[
        str | None,
        typer.Option("--agent-id", help="Existing agent ID (to create a new version)"),
    ] = None,
    agent_version: Annotated[
        str | None,
        typer.Option("--agent-version", help="Version label to create (e.g., v1.1.0)"),
    ] = None,
    commit_message: Annotated[
        str | None,
        typer.Option("--commit-message", help="Commit message for the new version"),
    ] = None,
):
    """Create a new agent or a new agent version.

    Interactive rules:
    - If nothing provided: ask to either create a new agent or create a version for an existing agent.
    - If only --agent-path provided: assume create new agent using the provided spec file.
    - If --agent-id provided (with or without --agent-path): assume create new version for that agent.
      - If --agent-version missing: prompt and ensure it is not equal to an existing version.
      - If --commit-message missing: prompt for it.
    """
    api = ApiClient()
    project_dir = Path.cwd()
    veris_dir = ensure_veris_dir(project_dir)

    import json as _json

    def _load_spec_from_path(p: Path) -> dict:
        try:
            return _json.loads(p.read_text(encoding="utf-8"))
        except Exception as e:
            rprint(f"[red]Failed to read agent spec at {p}: {e}[/red]")
            raise typer.Exit(code=1)

    # If nothing provided, ask user which path to take
    if not agent_path and not agent_id and not agent_version and not commit_message:
        rprint("[bold]What would you like to do?[/bold]")
        rprint("  1. Create a new agent")
        rprint("  2. Create a new version for an existing agent")
        choice = typer.prompt("Select option", default="1")
        if str(choice).strip() == "1":
            # Create new agent: require agent_path
            if not agent_path:
                inp = typer.prompt("Path to agent.json", default=str(veris_dir / "agent.json"))
                agent_path = Path(inp)
            spec = _load_spec_from_path(agent_path)
            # Use agent spec version if provided, else prompt
            version = spec.get("version") if isinstance(spec, dict) else None
            if not version:
                version = typer.prompt("New agent version (e.g., v1.0.0)", default="v1.0.0")
            with Live(
                "[cyan]Creating agent...[/cyan]", refresh_per_second=4, transient=False
            ) as live:
                created = api.v3_create_agent(spec, version=version)  # type: ignore[arg-type]
                new_agent_id = created.get("agent_id")
                if not new_agent_id:
                    rprint("[red]Agent creation did not return agent_id[/red]")
                    raise typer.Exit(code=1)
                live.update(
                    Text.from_markup(f"[green]Agent created[/green] {new_agent_id} {version}")
                )
            # Optionally set config agent_id
            cfg = load_config(project_dir)
            cfg.agent_id = new_agent_id
            save_config(project_dir, cfg, overwrite=True)
            rprint(f"[green]Saved agent_id to .veris/config.json[/green] {new_agent_id}")
            return
        else:
            # Create version for existing agent: request agent_id
            if not agent_id:
                agent_id = typer.prompt("Enter existing agent_id")
            # Validate that the agent exists before proceeding
            try:
                agent_info = api.v3_get_agent(agent_id)
                if not agent_info or not agent_info.get("agent_id"):
                    rprint(f"[red]Agent with id '{agent_id}' does not exist.[/red]")
                    raise typer.Exit(code=1)
            except Exception as e:
                rprint(f"[red]Failed to fetch agent with id '{agent_id}': {e}[/red]")
                raise typer.Exit(code=1)

    # If agent_id provided (or requested), create new version
    if agent_id:
        # Load spec if provided; else optionally prompt for path (blank allowed -> server may accept None)
        spec_data: dict | None = None
        if agent_path:
            spec_data = _load_spec_from_path(agent_path)
        else:
            # Offer to supply a spec override
            resp = typer.prompt(
                "Provide a path to agent.json for this version (default .veris/agent.json)",
                default=str(veris_dir / "agent.json"),
            )
            if resp.strip():
                spec_data = _load_spec_from_path(Path(resp))

        # Ensure version provided or prompt; ensure it differs from existing
        versions = api.v3_list_agent_versions(agent_id)
        existing = {v.get("version") for v in versions} if isinstance(versions, list) else set()
        if not agent_version:
            if existing:
                rprint(
                    "[yellow]Existing versions:[/yellow] "
                    + ", ".join(sorted(str(v) for v in existing if v))
                )
            agent_version = typer.prompt("New version (e.g., v1.1.0)")
        if agent_version in existing:
            rprint("[red]Version already exists for this agent. Choose a different version.[/red]")
            raise typer.Exit(code=1)

        # Ensure commit message
        if not commit_message:
            commit_message = typer.prompt("Commit message", default="updated")

        with Live(
            "[cyan]Creating agent version...[/cyan]", refresh_per_second=4, transient=False
        ) as live:
            res = api.v3_create_agent_version(
                agent_id,
                spec_json=spec_data,
                version=agent_version,
                commit_message=commit_message,
            )
            ver = res.get("version")
            if not ver:
                rprint("[red]Agent version creation failed[/red]")
                raise typer.Exit(code=1)
            live.update(Text.from_markup(f"[green]Agent version created[/green] {agent_id} {ver}"))
        return

    # Else if only agent_path provided → create new agent
    if agent_path and not agent_id:
        print("Creating new agent from path", agent_path)
        spec = _load_spec_from_path(agent_path)
        version = agent_version or spec.get("version") if isinstance(spec, dict) else None
        if not version:
            version = typer.prompt("New agent version (e.g., v1.0.0)", default="v1.0.0")
        with Live("[cyan]Creating agent...[/cyan]", refresh_per_second=4, transient=False) as live:
            created = api.v3_create_agent(spec, version=version)  # type: ignore[arg-type]
            new_agent_id = created.get("agent_id")
            if not new_agent_id:
                rprint("[red]Agent creation did not return agent_id[/red]")
                raise typer.Exit(code=1)
            live.update(Text.from_markup(f"[green]Agent created[/green] {new_agent_id} {version}"))
        cfg = load_config(project_dir)
        cfg.agent_id = new_agent_id
        save_config(project_dir, cfg, overwrite=True)
        rprint(f"[green]Saved agent_id to .veris/config.json[/green] {new_agent_id}")
        return

    # If we reached here, inputs were insufficient
    rprint(
        "[red]Nothing to do. Provide --agent-path to create an agent or --agent-id to create a version.[/red]"
    )
    raise typer.Exit(code=1)
