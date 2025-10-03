"""API client for the Veris CLI."""

from __future__ import annotations

import os
from typing import Any

import httpx
from httpx import HTTPStatusError
from veris_cli.errors import UpstreamServiceError
from dotenv import load_dotenv

from veris_cli.errors import ConfigurationError


class ApiClient:
    """API client for the Veris CLI."""

    def __init__(self, base_url: str | None = None, *, timeout: float = 30.0):
        """Initialize API client.

        This ensures .env file is loaded and validates API key is present.
        """
        # pdb.set_trace()
        load_dotenv(override=True)

        if not os.environ.get("VERIS_API_KEY"):
            print(
                "VERIS_API_KEY environment variable is not set. Please set it in your environment or create a .env file with VERIS_API_KEY=your-key-here"
            )
            raise ConfigurationError(
                message="VERIS_API_KEY environment variable is not set. "
                "Please set it in your environment or create a .env file with VERIS_API_KEY=your-key-here"
            )
        # Resolve base URL precedence: constructor > VERIS_API_URL > default
        if base_url:
            self.base_url = base_url
        else:
            env_url = os.environ.get("VERIS_API_URL")
            if not env_url:
                env_url = "https://simulator.api.veris.ai"
                os.environ["VERIS_API_URL"] = env_url
            self.base_url = env_url

        # Read API key from environment variable
        api_key = os.environ.get("VERIS_API_KEY")

        # Validate API key
        if api_key is None:
            raise ValueError(
                "VERIS_API_KEY environment variable is not set. "
                "Please set it in your environment or create a .env file with VERIS_API_KEY=your-key-here"
            )

        if not api_key.strip():
            raise ValueError(
                "VERIS_API_KEY environment variable is empty. Please provide a valid API key."
            )

        default_headers: dict[str, str] = {"X-API-Key": api_key}

        self._client = httpx.Client(
            base_url=self.base_url,
            timeout=timeout,
            headers=default_headers,
        )

    # Internal request helper to standardize error handling
    def _request(
        self,
        method: str,
        path: str,
        *,
        json: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        user_message: str | None = None,
    ) -> httpx.Response:
        try:
            response = self._client.request(method, path, json=json, params=params, headers=headers)
            response.raise_for_status()
            return response
        except HTTPStatusError as exc:
            raise UpstreamServiceError.from_httpx_error(
                exc,
                endpoint=f"{method} {path}",
                user_message=user_message or "The upstream service returned an error.",
            ) from exc

    # Scenario generation (V2)
    def start_scenario_generation(self, payload: dict[str, Any]) -> dict[str, str]:
        """Kick off scenario generation and return generation metadata.

        Expected response: { generation_id: str, status: str, message: str }
        """
        response = self._request(
            "POST",
            "/v2/scenarios/generate",
            json=payload,
            user_message=(
                "Failed to start scenario generation. This appears to be an upstream service issue."
            ),
        )
        return response.json()

    def get_generation_status(self, generation_id: str) -> dict[str, Any]:
        """Get status for a generation job."""
        response = self._request(
            "GET",
            f"/v2/scenarios/generation/{generation_id}/status",
            user_message="Failed to fetch scenario generation status.",
        )
        return response.json()

    def get_generated_scenarios(
        self, generation_id: str, include_failed: bool = False
    ) -> dict[str, Any]:
        """Retrieve generated scenarios for a generation job."""
        params = {"include_failed": str(include_failed).lower()}
        response = self._request(
            "GET",
            f"/v2/scenarios/generation/{generation_id}/scenarios",
            params=params,
            user_message="Failed to retrieve generated scenarios.",
        )
        return response.json()

    # Simulations
    def start_simulation(self, run_id: str, payload: dict[str, Any]) -> str:
        """Start a simulation."""
        response = self._request(
            "POST",
            "/v2/simulations",
            json=payload,
            headers={"X-Run-Id": run_id},
            user_message="Failed to start a simulation. This may be an upstream issue.",
        )
        data = response.json()
        simulation_id = data.get("simulation_id") or data.get("session_id")
        if not simulation_id:
            raise ValueError("Missing simulation_id/session_id in response")
        return simulation_id

    def get_simulation_status(self, simulation_id: str) -> str:
        """Get the status of a simulation."""
        response = self._request(
            "GET",
            f"/v2/simulations/{simulation_id}/status",
            user_message="Failed to fetch simulation status.",
        )
        data = response.json()
        # Expect e.g. { status: PENDING|IN_PROGRESS|COMPLETED|FAILED }
        return data.get("status", "UNKNOWN")

    def get_simulation_logs(self, simulation_id: str) -> dict[str, Any]:
        """Get the logs of a simulation."""
        response = self._request(
            "GET",
            f"/v2/simulations/{simulation_id}/logs",
            user_message="Failed to retrieve simulation logs.",
        )
        return response.json()

    def kill_simulation(self, simulation_id: str) -> None:
        """Kill a simulation."""
        self._request(
            "POST",
            f"/v2/simulations/{simulation_id}/kill",
            user_message="Failed to kill simulation.",
        )

    # Evaluations
    def start_evaluation(self, session_id: str) -> str:
        """Start an evaluation."""
        response = self._request(
            "POST",
            "/evals/evaluate",
            json={"session_id": session_id},
            user_message="Failed to start evaluation.",
        )
        data = response.json()
        eval_id = data.get("evaluation_id") or data.get("eval_id")
        if not eval_id:
            raise ValueError("Missing eval_id/evaluation_id in response")
        return eval_id

    def get_evaluation_status(self, eval_id: str) -> str:
        """Get the status of an evaluation."""
        response = self._request(
            "GET",
            f"/evals/{eval_id}/status",
            user_message="Failed to fetch evaluation status.",
        )
        data = response.json()
        return data.get("status", "UNKNOWN")

    def get_evaluation_results(self, eval_id: str) -> dict[str, Any]:
        """Get the results of an evaluation."""
        response = self._request(
            "GET",
            f"/evals/{eval_id}",
            user_message="Failed to retrieve evaluation results.",
        )
        return response.json()

    def kill_evaluation(self, eval_id: str) -> None:
        """Kill an evaluation."""
        self._request(
            "POST",
            f"/evals/{eval_id}/kill",
            user_message="Failed to kill evaluation.",
        )

    # Grading endpoint (server-level, not agent-scoped)
    def grade(self, spec: dict[str, Any], sample: Any) -> dict[str, Any]:
        """Run a grader spec against a sample and return the result."""
        response = self._request(
            "POST",
            "/grade",
            json={"spec": spec, "sample": sample},
            user_message="Failed to grade sample.",
        )
        return response.json()

    # -----------------------------
    # V3 API (agent-scoped)
    # -----------------------------

    # Agents
    def v3_create_agent(self, spec: dict[str, Any], version: str = "v1.0.0") -> dict[str, str]:
        """Create an agent and return { agent_id, version }."""
        payload = dict(spec)
        payload["version"] = version
        res = self._request(
            "POST", "/v3/agents", json=payload, user_message="Failed to create agent."
        )
        return res.json()

    def v3_get_agent(self, agent_id: str) -> dict[str, Any]:
        """Get an agent by ID."""
        res = self._request("GET", f"/v3/agents/{agent_id}")
        return res.json()

    # Scenario sets
    def v3_create_scenario_set(self, agent_id: str, payload: dict[str, Any]) -> dict[str, Any]:
        """Create a scenario set."""
        res = self._request(
            "POST",
            f"/v3/agents/{agent_id}/scenario-sets",
            json=payload,
            user_message="Failed to create scenario set.",
        )
        return res.json()

    def v3_get_latest_scenario_sets(self, agent_id: str) -> dict[str, Any]:
        """Get the latest scenario set for an agent."""
        res = self._request("GET", f"/v3/agents/{agent_id}/scenario-sets")
        return res.json()

    def v3_get_scenario_set(self, agent_id: str, scenario_set_id: str) -> dict[str, Any]:
        """Get a scenario set by ID."""
        res = self._request("GET", f"/v3/agents/{agent_id}/scenario-sets/{scenario_set_id}")
        return res.json()

    def v3_list_scenarios(self, agent_id: str, scenario_set_id: str) -> list[dict[str, Any]]:
        """List scenarios in a scenario set."""
        res = self._request(
            "GET", f"/v3/agents/{agent_id}/scenario-sets/{scenario_set_id}/scenarios"
        )
        data = res.json()
        # API returns a list
        return data

    # Simulations
    def v3_start_simulation(self, agent_id: str, payload: dict[str, Any]) -> dict[str, Any]:
        """Start a simulation."""
        res = self._request(
            "POST",
            f"/v3/agents/{agent_id}/simulations",
            json=payload,
            user_message="Failed to start simulation run.",
        )
        return res.json()

    def v3_list_sessions(self, agent_id: str, run_id: str) -> list[dict[str, Any]]:
        """List sessions in a simulation."""
        res = self._request("GET", f"/v3/agents/{agent_id}/simulations/{run_id}/sessions")
        data = res.json()
        return data.get("sessions", [])

    def v3_get_session_logs(
        self, agent_id: str, run_id: str, session_id: str
    ) -> list[dict[str, Any]]:
        """Get logs for a session."""
        res = self._request(
            "GET", f"/v3/agents/{agent_id}/simulations/{run_id}/sessions/{session_id}/logs"
        )
        data = res.json()
        # API returns a list of log dicts
        return data

    def v3_get_session_details(self, agent_id: str, run_id: str, session_id: str) -> dict[str, Any]:
        """Get details for a session."""
        res = self._request(
            "GET", f"/v3/agents/{agent_id}/simulations/{run_id}/sessions/{session_id}"
        )
        data = res.json()
        return data

    def v3_list_agent_versions(self, agent_id: str) -> list[dict[str, Any]]:
        """List versions for an agent.

        Returns a list of version dicts, most-recent last as returned by the server.
        """
        res = self._request(
            "GET",
            f"/v3/agents/{agent_id}/versions",
            user_message="Failed to fetch agent versions.",
        )
        data = res.json()
        return data.get("versions", [])

    def v3_list_scenario_sets(self, agent_id: str) -> list[dict[str, Any]]:
        """List scenario sets for an agent (most recent first)."""
        res = self._request(
            "GET",
            f"/v3/agents/{agent_id}/scenario-sets",
            user_message="Failed to fetch scenario sets.",
        )
        data = res.json()
        return data

    def v3_create_agent_version(
        self,
        agent_id: str,
        *,
        spec_json: dict[str, Any] | None,
        version: str,
        commit_message: str,
    ) -> dict[str, Any]:
        """Create a new agent version with multipart form data.

        Equivalent to:
        curl -X POST /v3/agents/{agent_id}/versions \
          -F spec=@agent.json;type=application/json \
          -F version=<version> -F commit_message=<msg>
        """
        # Use httpx directly for multipart to avoid custom _request json logic
        files = {}
        if spec_json is not None:
            import json as _json

            files["spec"] = (
                "agent.json",
                _json.dumps(spec_json),
                "application/json",
            )
        data = {"version": version, "commit_message": commit_message}
        try:
            resp = self._client.post(
                f"/v3/agents/{agent_id}/versions",
                files=files if files else None,
                data=data,
            )
            resp.raise_for_status()
            return resp.json()
        except HTTPStatusError as exc:
            raise UpstreamServiceError.from_httpx_error(
                exc,
                endpoint=f"POST /v3/agents/{agent_id}/versions",
                user_message="Failed to create agent version.",
            ) from exc

    # -----------------------------
    # V3 Evaluations
    # -----------------------------

    def v3_start_evaluations(self, agent_id: str, run_id: str) -> dict[str, Any]:
        """Start evaluations for a completed simulation run.

        POST /v3/agents/{agent_id}/evaluations { run_id }
        Returns: { evaluation_run_id }
        """
        res = self._request(
            "POST",
            f"/v3/agents/{agent_id}/evaluations",
            json={"run_id": run_id},
            user_message="Failed to start evaluations.",
        )
        return res.json()

    def v3_get_evaluations(self, agent_id: str, evaluation_run_id: str) -> dict[str, Any]:
        """Get evaluation run details by ID."""
        res = self._request(
            "GET",
            f"/v3/agents/{agent_id}/evaluations/{evaluation_run_id}",
            user_message="Failed to fetch evaluation run.",
        )
        return res.json()
