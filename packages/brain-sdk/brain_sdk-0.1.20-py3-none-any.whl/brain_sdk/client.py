import asyncio
import datetime
import importlib
import random
import sys
import time
import uuid
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple, TYPE_CHECKING

import requests

from .types import AgentStatus, ExecutionMetadata, HeartbeatData, WorkflowContext
from .async_config import AsyncConfig
from .execution_state import ExecutionState, ExecutionStatus
from .http_connection_manager import ConnectionManager
from .result_cache import ResultCache
from .async_execution_manager import AsyncExecutionManager
from .logger import get_logger
from .status import normalize_status

httpx = None  # type: ignore


def _ensure_httpx(force_reload: bool = False):
    """Load httpx lazily, allowing tests to monkeypatch the module."""
    global httpx

    if not force_reload and httpx is not None:
        return httpx

    try:
        module = importlib.import_module("httpx")
    except ImportError:
        httpx = None
    else:
        httpx = module

    return httpx


if TYPE_CHECKING:  # pragma: no cover - imported for type hints only
    import httpx  # noqa: F401


# Prime optional dependency cache at import time when available
_ensure_httpx()

# Set up logger for this module
logger = get_logger(__name__)

SUCCESS_STATUSES = {ExecutionStatus.SUCCEEDED.value}
FAILURE_STATUSES = {
    ExecutionStatus.FAILED.value,
    ExecutionStatus.CANCELLED.value,
    ExecutionStatus.TIMEOUT.value,
}


@dataclass
class _Submission:
    execution_id: str
    workflow_id: str
    target: str
    status: str
    target_type: Optional[str] = None


class BrainClient:
    def __init__(self, base_url: str = "http://localhost:8080", async_config: Optional[AsyncConfig] = None):
        self.base_url = base_url
        self.api_base = f"{base_url}/api/v1"
        self._current_workflow_context: Optional[WorkflowContext] = None

        # Async execution components
        self.async_config = async_config or AsyncConfig()
        self._async_execution_manager: Optional[AsyncExecutionManager] = None
        self._async_http_client: Optional["httpx.AsyncClient"] = None
        self._async_http_client_lock: Optional[asyncio.Lock] = None
        self._result_cache = ResultCache(self.async_config)
        self._latest_event_stream_headers: Dict[str, str] = {}

    def _generate_id(self, prefix: str) -> str:
        """Generates a unique ID with a given prefix."""
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        unique_id = uuid.uuid4().hex[:8]
        return f"{prefix}_{timestamp}_{unique_id}"

    def _get_headers_with_context(
        self, headers: Optional[Dict[str, str]] = None
    ) -> Dict[str, str]:
        """Combines provided headers with current workflow context headers."""
        if headers is None:
            headers = {}

        if self._current_workflow_context:
            context_headers = self._current_workflow_context.to_headers()
            headers.update(context_headers)

        return headers

    def _build_event_stream_headers(self, source_headers: Optional[Dict[str, str]]) -> Dict[str, str]:
        """Return headers that should be forwarded to the SSE event stream."""

        headers = source_headers or self._get_headers_with_context({})
        if not headers:
            return {}

        allowed = {"authorization", "cookie"}
        event_headers: Dict[str, str] = {}
        for key, value in headers.items():
            if value is None:
                continue
            lower = key.lower()
            if lower.startswith("x-") or lower in allowed:
                event_headers[key] = value
        return event_headers

    def _maybe_update_event_stream_headers(self, source_headers: Optional[Dict[str, str]]) -> None:
        """Update stored SSE headers and propagate to the manager when enabled."""

        if not self.async_config.enable_event_stream:
            return

        new_headers = self._build_event_stream_headers(source_headers)
        if new_headers:
            self._latest_event_stream_headers = new_headers
        elif not self._latest_event_stream_headers and source_headers is None:
            # No headers from context yet; keep empty state.
            self._latest_event_stream_headers = {}

        if self._async_execution_manager is not None:
            self._async_execution_manager.set_event_stream_headers(self._latest_event_stream_headers)

    async def get_async_http_client(self) -> "httpx.AsyncClient":
        """Lazily create and return a shared httpx.AsyncClient."""
        current_module = sys.modules.get("httpx")
        reload_needed = httpx is None or current_module is not httpx
        httpx_module = _ensure_httpx(force_reload=reload_needed)
        if httpx_module is None:
            raise RuntimeError("httpx is required for async HTTP operations")

        if self._async_http_client and not getattr(self._async_http_client, "is_closed", False):
            return self._async_http_client

        if self._async_http_client_lock is None:
            self._async_http_client_lock = asyncio.Lock()

        async with self._async_http_client_lock:
            if self._async_http_client and not getattr(self._async_http_client, "is_closed", False):
                return self._async_http_client

            client_kwargs = {
                "headers": {
                    "User-Agent": "BrainSDK/1.0",
                    "Accept": "application/json",
                }
            }

            limits_factory = getattr(httpx_module, "Limits", None)
            if limits_factory:
                client_kwargs["limits"] = limits_factory(
                    max_connections=self.async_config.connection_pool_size,
                    max_keepalive_connections=self.async_config.connection_pool_per_host,
                )

            timeout_factory = getattr(httpx_module, "Timeout", None)
            if timeout_factory:
                client_kwargs["timeout"] = timeout_factory(10.0, connect=5.0)
            else:
                client_kwargs["timeout"] = 10.0

            try:
                self._async_http_client = httpx_module.AsyncClient(**client_kwargs)
            except TypeError:
                # Test doubles may not accept keyword arguments
                self._async_http_client = httpx_module.AsyncClient()
                headers = client_kwargs.get("headers")
                if headers and hasattr(self._async_http_client, "headers"):
                    try:
                        self._async_http_client.headers.update(headers)
                    except Exception:
                        pass

            return self._async_http_client

    async def _async_request(self, method: str, url: str, **kwargs):
        """Perform an HTTP request using the shared async client with sync fallback."""
        try:
            client = await self.get_async_http_client()
        except RuntimeError:
            return await asyncio.to_thread(self._sync_request, method, url, **kwargs)

        return await client.request(method, url, **kwargs)

    @staticmethod
    def _sync_request(method: str, url: str, **kwargs):
        """Blocking HTTP request helper used when httpx is unavailable."""
        # DIAGNOSTIC: Add request size logging
        if 'json' in kwargs:
            import json
            json_size = len(json.dumps(kwargs['json']).encode('utf-8'))
            logger.debug(f"🔍 SYNC_REQUEST: Making {method} request to {url} with JSON payload size: {json_size} bytes")

        # Configure session with proper settings for large payloads
        session = requests.Session()

        # Configure adapter with larger buffer sizes for handling large JSON responses
        from requests.adapters import HTTPAdapter
        from urllib3.util.retry import Retry

        # Create custom adapter with larger buffer sizes
        adapter = HTTPAdapter(
            max_retries=Retry(total=3, backoff_factor=0.3)
        )
        session.mount('http://', adapter)
        session.mount('https://', adapter)

        # Set default headers if not provided
        if 'headers' not in kwargs:
            kwargs['headers'] = {}

        # Ensure proper content type for JSON requests
        if 'json' in kwargs and 'Content-Type' not in kwargs['headers']:
            kwargs['headers']['Content-Type'] = 'application/json'

        # Add User-Agent if not present
        if 'User-Agent' not in kwargs['headers']:
            kwargs['headers']['User-Agent'] = 'BrainSDK/1.0'

        # DIAGNOSTIC: Log request details
        logger.debug(f"🔍 SYNC_REQUEST: Headers: {kwargs.get('headers', {})}")

        # Configure stream=False to ensure we read the full response
        # This prevents truncation issues with large JSON responses
        if 'stream' not in kwargs:
            kwargs['stream'] = False

        try:
            response = session.request(method, url, **kwargs)

            # DIAGNOSTIC: Log response details
            logger.debug(f"🔍 SYNC_RESPONSE: Status {response.status_code}, Content-Length: {response.headers.get('Content-Length', 'unknown')}")

            # Check if response might be truncated
            content_length = response.headers.get('Content-Length')
            if content_length and len(response.content) != int(content_length):
                logger.error(f"🚨 RESPONSE_TRUNCATION: Expected {content_length} bytes, got {len(response.content)} bytes")

            # Check for exactly 4096 bytes which indicates truncation
            if len(response.content) == 4096:
                logger.error(f"🚨 POSSIBLE_TRUNCATION: Response is exactly 4096 bytes - likely truncated!")

            return response
        finally:
            session.close()


    async def aclose(self) -> None:
        """Close shared resources such as async HTTP clients and managers."""
        if self._async_execution_manager is not None:
            try:
                await self._async_execution_manager.stop()
            finally:
                self._async_execution_manager = None

        if self._async_http_client is not None:
            try:
                await self._async_http_client.aclose()
            finally:
                self._async_http_client = None
                self._async_http_client_lock = None

    def register_node(self, node_data: Dict[str, Any]) -> Dict[str, Any]:
        """Register agent node with Brain server"""
        response = requests.post(f"{self.api_base}/nodes/register", json=node_data)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()

    def update_health(
        self, node_id: str, health_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Update node health status"""
        response = requests.put(
            f"{self.api_base}/nodes/{node_id}/health", json=health_data
        )
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()

    def get_nodes(self) -> Dict[str, Any]:
        """Get all registered nodes"""
        response = requests.get(f"{self.api_base}/nodes")
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()

    def execute_reasoner(
        self,
        reasoner_id: str,
        input_data: Dict[str, Any],
        context: Optional[WorkflowContext] = None,
    ) -> Dict[str, Any]:
        """
        Executes a reasoner on the Brain server, including workflow tracking.
        If context is provided, it overrides the current client context for this call.
        """
        headers = {}
        if context:
            headers.update(context.to_headers())

        # Ensure a workflow ID exists for this request
        if "X-Workflow-ID" not in headers:
            if (
                self._current_workflow_context
                and self._current_workflow_context.workflow_id
            ):
                headers["X-Workflow-ID"] = self._current_workflow_context.workflow_id
            else:
                headers["X-Workflow-ID"] = self._generate_id("wf")

        # Ensure a brain request ID exists for this request
        if "X-Brain-Request-ID" not in headers:
            headers["X-Brain-Request-ID"] = self._generate_id("req")

        # Add other context headers if available in current client context
        headers = self._get_headers_with_context(headers)

        payload = {"input": input_data}
        response = requests.post(
            f"{self.api_base}/reasoners/{reasoner_id}", json=payload, headers=headers
        )
        response.raise_for_status()

        result = response.json()
        # Extract execution metadata from response headers
        execution_metadata = ExecutionMetadata.from_headers(dict(response.headers))
        if execution_metadata:
            result["execution_metadata"] = (
                execution_metadata.to_dict()
            )  # Convert dataclass to dict

        return result

    def execute_skill(
        self,
        skill_id: str,
        input_data: Dict[str, Any],
        context: Optional[WorkflowContext] = None,
    ) -> Dict[str, Any]:
        """
        Executes a skill on the Brain server, including workflow tracking.
        If context is provided, it overrides the current client context for this call.
        """
        headers = {}
        if context:
            headers.update(context.to_headers())

        # Ensure a workflow ID exists for this request
        if "X-Workflow-ID" not in headers:
            if (
                self._current_workflow_context
                and self._current_workflow_context.workflow_id
            ):
                headers["X-Workflow-ID"] = self._current_workflow_context.workflow_id
            else:
                headers["X-Workflow-ID"] = self._generate_id("wf")

        # Ensure a brain request ID exists for this request
        if "X-Brain-Request-ID" not in headers:
            headers["X-Brain-Request-ID"] = self._generate_id("req")

        # Add other context headers if available in current client context
        headers = self._get_headers_with_context(headers)

        payload = {"input": input_data}
        response = requests.post(
            f"{self.api_base}/skills/{skill_id}", json=payload, headers=headers
        )
        response.raise_for_status()

        result = response.json()
        # Extract execution metadata from response headers
        execution_metadata = ExecutionMetadata.from_headers(dict(response.headers))
        if execution_metadata:
            result["execution_metadata"] = (
                execution_metadata.to_dict()
            )  # Convert dataclass to dict

        return result

    def set_workflow_context(self, context: WorkflowContext):
        """Sets the current workflow context for subsequent calls."""
        self._current_workflow_context = context

    def clear_workflow_context(self):
        """Clears the current workflow context."""
        self._current_workflow_context = None

    def get_workflow_context(self) -> Optional[WorkflowContext]:
        """Returns the current workflow context."""
        return self._current_workflow_context

    async def register_agent(
        self,
        node_id: str,
        reasoners: List[dict],
        skills: List[dict],
        base_url: str,
        discovery: Optional[Dict[str, Any]] = None,
    ) -> Tuple[bool, Optional[Dict[str, Any]]]:
        """Register or update agent information with Brain server."""
        try:
            registration_data = {
                "id": node_id,
                "team_id": "default",
                "base_url": base_url,
                "version": "1.0.0",
                "reasoners": reasoners,
                "skills": skills,
                "communication_config": {
                    "protocols": ["http"],
                    "websocket_endpoint": "",
                    "heartbeat_interval": "5s",
                },
                "health_status": "healthy",
                "last_heartbeat": datetime.datetime.now().isoformat() + "Z",
                "registered_at": datetime.datetime.now().isoformat() + "Z",
                "features": {
                    "ab_testing": False,
                    "advanced_metrics": False,
                    "compliance": False,
                    "audit_logging": False,
                    "role_based_access": False,
                    "experimental": {},
                },
                "metadata": {
                    "deployment": {
                        "environment": "development",
                        "platform": "python",
                        "region": "local",
                        "tags": {"sdk_version": "1.0.0", "language": "python"},
                    },
                    "performance": {"latency_ms": 0, "throughput_ps": 0},
                    "custom": {},
                },
            }

            if discovery:
                registration_data["callback_discovery"] = discovery

            response = await self._async_request(
                "POST",
                f"{self.api_base}/nodes/register",
                json=registration_data,
                timeout=30.0,
            )
            payload: Optional[Dict[str, Any]] = None
            try:
                if getattr(response, "content", None):
                    payload = response.json()
            except Exception:
                payload = None

            if response.status_code not in (200, 201):
                return False, payload

            return True, payload

        except Exception as e:
            # self.logger.error(f"Failed to register agent: {e}")
            return False, None

    async def execute(
        self,
        target: str,
        input_data: Dict[str, Any],
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """
        Execute a reasoner or skill via the durable execution gateway.

        The public signature remains unchanged, but internally we now submit the
        execution, poll for completion with adaptive backoff, and return the final
        result once the worker finishes processing.
        """

        execution_headers = self._prepare_execution_headers(headers)
        submission = await self._submit_execution_async(target, input_data, execution_headers)
        status_payload = await self._await_execution_async(submission, execution_headers)
        result_value, metadata = self._format_execution_result(submission, status_payload)
        return self._build_execute_response(submission, status_payload, result_value, metadata)

    def execute_sync(
        self,
        target: str,
        input_data: Dict[str, Any],
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """
        Blocking version of execute used by synchronous callers.
        """

        execution_headers = self._prepare_execution_headers(headers)
        submission = self._submit_execution_sync(target, input_data, execution_headers)
        status_payload = self._await_execution_sync(submission, execution_headers)
        result_value, metadata = self._format_execution_result(submission, status_payload)
        return self._build_execute_response(submission, status_payload, result_value, metadata)

    def _prepare_execution_headers(self, headers: Optional[Dict[str, str]]) -> Dict[str, str]:
        final_headers = {"Content-Type": "application/json"}
        if headers:
            final_headers.update(headers)

        # Merge in workflow context headers (session, actor, etc.)
        final_headers = self._get_headers_with_context(final_headers)

        if "X-Workflow-ID" not in final_headers:
            if (
                self._current_workflow_context
                and self._current_workflow_context.workflow_id
            ):
                final_headers["X-Workflow-ID"] = self._current_workflow_context.workflow_id
            else:
                final_headers["X-Workflow-ID"] = self._generate_id("wf")

        if "X-Brain-Request-ID" not in final_headers:
            final_headers["X-Brain-Request-ID"] = self._generate_id("req")

        self._maybe_update_event_stream_headers(final_headers)

        return final_headers

    def _submit_execution_sync(
        self,
        target: str,
        input_data: Dict[str, Any],
        headers: Dict[str, str],
    ) -> _Submission:
        payload = {"input": input_data}
        try:
            response = requests.post(
                f"{self.api_base}/execute/async/{target}",
                json=payload,
                headers=headers,
                timeout=self.async_config.polling_timeout,
            )
        except requests.RequestException as exc:
            raise RuntimeError(f"Failed to submit execution: {exc}") from exc
        response.raise_for_status()
        body = response.json()
        return self._parse_submission(body, headers, target)

    async def _submit_execution_async(
        self,
        target: str,
        input_data: Dict[str, Any],
        headers: Dict[str, str],
    ) -> _Submission:
        payload = {"input": input_data}
        response = await self._async_request(
            "POST",
            f"{self.api_base}/execute/async/{target}",
            json=payload,
            headers=headers,
            timeout=self.async_config.polling_timeout,
        )
        response.raise_for_status()
        body = response.json()
        return self._parse_submission(body, headers, target)

    def _parse_submission(
        self,
        body: Dict[str, Any],
        headers: Dict[str, str],
        target: str,
    ) -> _Submission:
        execution_id = body.get("execution_id")
        workflow_id = body.get("workflow_id") or headers.get("X-Workflow-ID")
        status = (body.get("status") or "pending").lower()
        target_type = body.get("type") or body.get("target_type")

        if not execution_id or not workflow_id:
            raise RuntimeError("Execution submission missing identifiers")

        return _Submission(
            execution_id=execution_id,
            workflow_id=workflow_id,
            target=target,
            status=status,
            target_type=target_type,
        )

    def _await_execution_sync(
        self,
        submission: _Submission,
        headers: Dict[str, str],
    ) -> Dict[str, Any]:
        cached = self._result_cache.get_execution_result(submission.execution_id)
        if cached is not None:
            return {"result": cached, "status": "succeeded", "workflow_id": submission.workflow_id}

        interval = max(self.async_config.initial_poll_interval, 0.25)
        start = time.time()

        while True:
            response = requests.get(
                f"{self.api_base}/executions/{submission.execution_id}",
                headers=headers,
                timeout=self.async_config.polling_timeout,
            )
            response.raise_for_status()
            payload = response.json()
            normalized_status = normalize_status(payload.get("status"))
            payload["status"] = normalized_status

            if normalized_status in SUCCESS_STATUSES:
                return payload

            if normalized_status in FAILURE_STATUSES:
                if not payload.get("error_message") and payload.get("error"):
                    payload["error_message"] = payload["error"]
                return payload

            if (time.time() - start) > self.async_config.max_execution_timeout:
                raise TimeoutError(
                    f"Execution {submission.execution_id} exceeded timeout"
                )

            time.sleep(self._next_poll_interval(interval))
            interval = min(interval * 2, self.async_config.max_poll_interval)

    async def _await_execution_async(
        self,
        submission: _Submission,
        headers: Dict[str, str],
    ) -> Dict[str, Any]:
        cached = self._result_cache.get_execution_result(submission.execution_id)
        if cached is not None:
            return {"result": cached, "status": "succeeded", "workflow_id": submission.workflow_id}

        interval = max(self.async_config.initial_poll_interval, 0.25)
        start = time.time()

        while True:
            response = await self._async_request(
                "GET",
                f"{self.api_base}/executions/{submission.execution_id}",
                headers=headers,
                timeout=self.async_config.polling_timeout,
            )
            response.raise_for_status()
            payload = response.json()
            normalized_status = normalize_status(payload.get("status"))
            payload["status"] = normalized_status

            if normalized_status in SUCCESS_STATUSES:
                return payload

            if normalized_status in FAILURE_STATUSES:
                if not payload.get("error_message") and payload.get("error"):
                    payload["error_message"] = payload["error"]
                return payload

            if (time.time() - start) > self.async_config.max_execution_timeout:
                raise TimeoutError(
                    f"Execution {submission.execution_id} exceeded timeout"
                )

            await asyncio.sleep(self._next_poll_interval(interval))
            interval = min(interval * 2, self.async_config.max_poll_interval)

    def _format_execution_result(
        self,
        submission: _Submission,
        payload: Dict[str, Any],
    ) -> Tuple[Any, Dict[str, Any]]:
        result_value = payload.get("result")
        if result_value is None:
            result_value = payload

        normalized_status = normalize_status(payload.get("status"))
        target = payload.get("target") or submission.target
        node_id = payload.get("node_id")
        if not node_id and target and "." in target:
            node_id = target.split(".", 1)[0]

        metadata = {
            "execution_id": submission.execution_id,
            "workflow_id": payload.get("workflow_id") or submission.workflow_id,
            "brain_request_id": payload.get("brain_request_id"),
            "status": normalized_status,
            "target": target,
            "type": payload.get("type") or submission.target_type,
            "duration_ms": payload.get("duration_ms") or payload.get("duration"),
            "started_at": payload.get("started_at"),
            "completed_at": payload.get("completed_at"),
            "node_id": node_id,
            "error_message": payload.get("error_message") or payload.get("error"),
        }

        if metadata.get("completed_at"):
            metadata["timestamp"] = metadata["completed_at"]
        elif metadata.get("started_at"):
            metadata["timestamp"] = metadata["started_at"]
        else:
            metadata["timestamp"] = datetime.datetime.utcnow().isoformat()

        # Cache successful results for reuse
        if normalized_status in SUCCESS_STATUSES:
            try:
                self._result_cache.set_execution_result(submission.execution_id, result_value)
            except Exception:
                logger.debug("Failed to cache execution result", exc_info=True)

        return result_value, {k: v for k, v in metadata.items() if v is not None}

    def _build_execute_response(
        self,
        submission: _Submission,
        payload: Dict[str, Any],
        result_value: Any,
        metadata: Dict[str, Any],
    ) -> Dict[str, Any]:
        status = (metadata.get("status") or "").lower()

        normalized_status = normalize_status(metadata.get("status"))
        error_message = metadata.get("error_message")

        if normalized_status in SUCCESS_STATUSES:
            response_result = result_value
        elif normalized_status in FAILURE_STATUSES:
            response_result = None
        else:
            response_result = result_value

        response = {
            "execution_id": metadata.get("execution_id"),
            "workflow_id": metadata.get("workflow_id"),
            "brain_request_id": metadata.get("brain_request_id"),
            "node_id": metadata.get("node_id"),
            "type": metadata.get("type"),
            "target": metadata.get("target") or submission.target,
            "status": normalized_status,
            "duration_ms": metadata.get("duration_ms"),
            "timestamp": metadata.get("timestamp") or datetime.datetime.utcnow().isoformat(),
            "result": response_result,
            "error_message": error_message,
            "cost": payload.get("cost"),
        }

        return response

    def _next_poll_interval(self, current: float) -> float:
        jitter = random.uniform(0.8, 1.2)
        return max(0.05, min(current * jitter, self.async_config.max_poll_interval))

    async def send_enhanced_heartbeat(
        self, node_id: str, heartbeat_data: HeartbeatData
    ) -> bool:
        """
        Send enhanced heartbeat with status and MCP information to Brain server.

        Args:
            node_id: The agent node ID
            heartbeat_data: Enhanced heartbeat data with status and MCP info

        Returns:
            True if heartbeat was successful, False otherwise
        """
        try:
            response = await self._async_request(
                "POST",
                f"{self.api_base}/nodes/{node_id}/heartbeat",
                json=heartbeat_data.to_dict(),
                headers={"Content-Type": "application/json"},
                timeout=5.0,
            )
            response.raise_for_status()
            return True
        except Exception:
            return False

    def send_enhanced_heartbeat_sync(
        self, node_id: str, heartbeat_data: HeartbeatData
    ) -> bool:
        """
        Synchronous version of enhanced heartbeat for compatibility.

        Args:
            node_id: The agent node ID
            heartbeat_data: Enhanced heartbeat data with status and MCP info

        Returns:
            True if heartbeat was successful, False otherwise
        """
        try:
            response = requests.post(
                f"{self.api_base}/nodes/{node_id}/heartbeat",
                json=heartbeat_data.to_dict(),
                headers={"Content-Type": "application/json"},
                timeout=5.0,
            )
            response.raise_for_status()
            return True
        except Exception:
            return False

    async def notify_graceful_shutdown(self, node_id: str) -> bool:
        """
        Notify Brain server that the agent is shutting down gracefully.

        Args:
            node_id: The agent node ID

        Returns:
            True if notification was successful, False otherwise
        """
        try:
            response = await self._async_request(
                "POST",
                f"{self.api_base}/nodes/{node_id}/shutdown",
                headers={"Content-Type": "application/json"},
                timeout=5.0,
            )
            response.raise_for_status()
            return True
        except Exception:
            return False

    def notify_graceful_shutdown_sync(self, node_id: str) -> bool:
        """
        Synchronous version of graceful shutdown notification.

        Args:
            node_id: The agent node ID

        Returns:
            True if notification was successful, False otherwise
        """
        try:
            response = requests.post(
                f"{self.api_base}/nodes/{node_id}/shutdown",
                headers={"Content-Type": "application/json"},
                timeout=5.0,
            )
            response.raise_for_status()
            return True
        except Exception:
            return False

    async def register_agent_with_status(
        self,
        node_id: str,
        reasoners: List[dict],
        skills: List[dict],
        base_url: str,
        status: AgentStatus = AgentStatus.STARTING,
        discovery: Optional[Dict[str, Any]] = None,
        suppress_errors: bool = False,
    ) -> Tuple[bool, Optional[Dict[str, Any]]]:
        """Register agent with immediate status reporting for fast lifecycle."""
        try:
            registration_data = {
                "id": node_id,
                "team_id": "default",
                "base_url": base_url,
                "version": "1.0.0",
                "reasoners": reasoners,
                "skills": skills,
                "lifecycle_status": status.value,
                "communication_config": {
                    "protocols": ["http"],
                    "websocket_endpoint": "",
                    "heartbeat_interval": "2s",
                },
                "health_status": "healthy",
                "last_heartbeat": datetime.datetime.now().isoformat() + "Z",
                "registered_at": datetime.datetime.now().isoformat() + "Z",
                "features": {
                    "ab_testing": False,
                    "advanced_metrics": False,
                    "compliance": False,
                    "audit_logging": False,
                    "role_based_access": False,
                    "experimental": {},
                },
                "metadata": {
                    "deployment": {
                        "environment": "development",
                        "platform": "python",
                        "region": "local",
                        "tags": {"sdk_version": "1.0.0", "language": "python"},
                    },
                    "performance": {"latency_ms": 0, "throughput_ps": 0},
                    "custom": {},
                },
            }

            if discovery:
                registration_data["callback_discovery"] = discovery

            response = await self._async_request(
                "POST",
                f"{self.api_base}/nodes/register",
                json=registration_data,
                timeout=10.0,
            )

            payload: Optional[Dict[str, Any]] = None
            try:
                if getattr(response, "content", None):
                    payload = response.json()
            except Exception:
                payload = None

            if response.status_code not in (200, 201):
                if not suppress_errors:
                    logger.error(
                        "Fast lifecycle registration failed with status %s",
                        response.status_code,
                    )
                    logger.error(f"Response text: {getattr(response, 'text', '<none>')}")
                else:
                    logger.debug(
                        "Fast lifecycle registration failed with status %s",
                        response.status_code,
                    )
                return False, payload

            logger.debug(f"Agent {node_id} registered successfully")
            return True, payload

        except Exception as e:
            if not suppress_errors:
                logger.error(
                    f"Agent registration failed for {node_id}: {type(e).__name__}: {e}"
                )
            else:
                logger.debug(
                    f"Agent registration failed for {node_id}: {type(e).__name__}"
                )
            return False, None

    # Async Execution Methods

    async def _get_async_execution_manager(self) -> AsyncExecutionManager:
            """
            Get or create the async execution manager instance.

            Returns:
                AsyncExecutionManager: Active async execution manager
            """
            if self._async_execution_manager is None:
                self._async_execution_manager = AsyncExecutionManager(
                    base_url=self.base_url,
                    config=self.async_config
                )
                await self._async_execution_manager.start()
                self._maybe_update_event_stream_headers(None)

            return self._async_execution_manager

    async def execute_async(
        self,
        target: str,
        input_data: Dict[str, Any],
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None
    ) -> str:
        """
        Submit an async execution and return execution_id.

        Args:
            target: Target in format 'node_id.reasoner_name' or 'node_id.skill_name'
            input_data: Input data for the reasoner/skill
            headers: Optional headers to include (will be merged with context headers)
            timeout: Optional execution timeout (uses config default if None)

        Returns:
            str: Execution ID for tracking the execution

        Raises:
            RuntimeError: If async execution is disabled or at capacity
            aiohttp.ClientError: For HTTP-related errors
        """
        if not self.async_config.enable_async_execution:
            raise RuntimeError("Async execution is disabled in configuration")

        try:
            final_headers = self._prepare_execution_headers(headers)

            # Get async execution manager and submit
            manager = await self._get_async_execution_manager()
            execution_id = await manager.submit_execution(
                target=target,
                input_data=input_data,
                headers=final_headers,
                timeout=timeout
            )

            logger.debug(f"Submitted async execution {execution_id[:8]}... for target {target}")
            return execution_id

        except Exception as e:
            logger.error(f"Failed to submit async execution for target {target}: {e}")

            # Fallback to sync execution if enabled
            if self.async_config.fallback_to_sync:
                logger.warn(f"Falling back to sync execution for target {target}")
                try:
                    result = await self.execute(target, input_data, headers)
                    # Create a synthetic execution ID for consistency
                    synthetic_id = self._generate_id("sync")
                    logger.debug(f"Sync fallback completed with synthetic ID {synthetic_id[:8]}...")
                    return synthetic_id
                except Exception as sync_error:
                    logger.error(f"Sync fallback also failed: {sync_error}")
                    raise e
            else:
                raise

    async def poll_execution_status(self, execution_id: str) -> Optional[Dict[str, Any]]:
        """
        Poll single execution status with connection reuse.

        Args:
            execution_id: Execution ID to poll

        Returns:
            Optional[Dict]: Execution status dictionary or None if not found

        Raises:
            RuntimeError: If async execution is disabled
            aiohttp.ClientError: For HTTP-related errors
        """
        if not self.async_config.enable_async_execution:
            raise RuntimeError("Async execution is disabled in configuration")

        try:
            manager = await self._get_async_execution_manager()
            status = await manager.get_execution_status(execution_id)

            if status:
                logger.debug(f"Polled status for execution {execution_id[:8]}...: {status.get('status')}")
            else:
                logger.debug(f"Execution {execution_id[:8]}... not found")

            return status

        except Exception as e:
            logger.error(f"Failed to poll execution status for {execution_id[:8]}...: {e}")
            raise

    async def batch_check_statuses(self, execution_ids: List[str]) -> Dict[str, Optional[Dict[str, Any]]]:
                """
                Check multiple execution statuses efficiently.

                Args:
                    execution_ids: List of execution IDs to check

                Returns:
                    Dict[str, Optional[Dict]]: Mapping of execution_id to status dict

                Raises:
                    RuntimeError: If async execution is disabled
                    ValueError: If execution_ids list is empty
                """
                if not self.async_config.enable_async_execution:
                    raise RuntimeError("Async execution is disabled in configuration")

                if not execution_ids:
                    raise ValueError("execution_ids list cannot be empty")

                try:
                    manager = await self._get_async_execution_manager()
                    results = {}

                    # Use batch processing if enabled and list is large enough
                    if (self.async_config.enable_batch_polling and
                        len(execution_ids) >= 2):  # Use batch for 2+ executions

                        # Process in batches
                        batch_size = self.async_config.batch_size
                        for i in range(0, len(execution_ids), batch_size):
                            batch_ids = execution_ids[i:i + batch_size]

                            # Get statuses for this batch
                            for exec_id in batch_ids:
                                status = await manager.get_execution_status(exec_id)
                                results[exec_id] = status

                            logger.debug(f"Batch checked {len(batch_ids)} execution statuses")
                    else:
                        # Process individually
                        for exec_id in execution_ids:
                            status = await manager.get_execution_status(exec_id)
                            results[exec_id] = status

                        logger.debug(f"Individually checked {len(execution_ids)} execution statuses")

                    return results

                except Exception as e:
                    logger.error(f"Failed to batch check execution statuses: {e}")
                    raise

    async def wait_for_execution_result(
        self,
        execution_id: str,
        timeout: Optional[float] = None
    ) -> Any:
        """
        Wait for execution completion with polling.

        Args:
            execution_id: Execution ID to wait for
            timeout: Optional timeout override (uses config default if None)

        Returns:
            Any: Execution result

        Raises:
            RuntimeError: If async execution is disabled or execution fails
            TimeoutError: If execution times out
            KeyError: If execution_id is not found
        """
        if not self.async_config.enable_async_execution:
            raise RuntimeError("Async execution is disabled in configuration")

        try:
            manager = await self._get_async_execution_manager()
            result = await manager.wait_for_result(execution_id, timeout)

            logger.debug(f"Execution {execution_id[:8]}... completed successfully")
            return result

        except Exception as e:
            logger.error(f"Failed to wait for execution result {execution_id[:8]}...: {e}")
            raise

    async def cancel_async_execution(self, execution_id: str, reason: Optional[str] = None) -> bool:
                """
                Cancel an active async execution.

                Args:
                    execution_id: Execution ID to cancel
                    reason: Optional cancellation reason

                Returns:
                    bool: True if execution was cancelled, False if not found or already terminal

                Raises:
                    RuntimeError: If async execution is disabled
                """
                if not self.async_config.enable_async_execution:
                    raise RuntimeError("Async execution is disabled in configuration")

                try:
                    manager = await self._get_async_execution_manager()
                    cancelled = await manager.cancel_execution(execution_id, reason)

                    if cancelled:
                        logger.debug(f"Cancelled execution {execution_id[:8]}... - {reason or 'No reason provided'}")
                    else:
                        logger.debug(f"Could not cancel execution {execution_id[:8]}... (not found or already terminal)")

                    return cancelled

                except Exception as e:
                    logger.error(f"Failed to cancel execution {execution_id[:8]}...: {e}")
                    raise

    async def list_async_executions(
                self,
                status_filter: Optional[str] = None,
                limit: Optional[int] = None
            ) -> List[Dict[str, Any]]:
                """
                List async executions with optional filtering.

                Args:
        status_filter: Optional status to filter by ('pending', 'queued', 'running', 'succeeded', 'failed', etc.)
                    limit: Optional limit on number of results

                Returns:
                    List[Dict]: List of execution status dictionaries

                Raises:
                    RuntimeError: If async execution is disabled
                """
                if not self.async_config.enable_async_execution:
                    raise RuntimeError("Async execution is disabled in configuration")

                try:
                    manager = await self._get_async_execution_manager()

                    # Convert string status to ExecutionStatus enum if provided
                    status_enum = None
                    if status_filter:
                        try:
                            status_enum = ExecutionStatus(status_filter.lower())
                        except ValueError:
                            logger.warning(f"Invalid status filter: {status_filter}")
                            return []

                    executions = await manager.list_executions(status_enum, limit)
                    logger.debug(f"Listed {len(executions)} async executions")

                    return executions

                except Exception as e:
                    logger.error(f"Failed to list async executions: {e}")
                    raise

    async def get_async_execution_metrics(self) -> Dict[str, Any]:
                """
                Get comprehensive metrics for async execution manager.

                Returns:
                    Dict[str, Any]: Metrics dictionary with execution statistics

                Raises:
                    RuntimeError: If async execution is disabled
                """
                if not self.async_config.enable_async_execution:
                    raise RuntimeError("Async execution is disabled in configuration")

                try:
                    if self._async_execution_manager is None:
                        return {
                            'manager_started': False,
                            'message': 'Async execution manager not yet initialized'
                        }

                    metrics = self._async_execution_manager.get_metrics()
                    logger.debug("Retrieved async execution metrics")

                    return metrics

                except Exception as e:
                    logger.error(f"Failed to get async execution metrics: {e}")
                    raise

    async def cleanup_async_executions(self) -> int:
        """
        Manually trigger cleanup of completed executions.

        Returns:
            int: Number of executions cleaned up

        Raises:
            RuntimeError: If async execution is disabled
        """
        if not self.async_config.enable_async_execution:
            raise RuntimeError("Async execution is disabled in configuration")

        try:
            if self._async_execution_manager is None:
                return 0

            cleanup_count = await self._async_execution_manager.cleanup_completed_executions()
            logger.debug(f"Cleaned up {cleanup_count} completed async executions")

            return cleanup_count

        except Exception as e:
            logger.error(f"Failed to cleanup async executions: {e}")
            raise

    async def close_async_execution_manager(self) -> None:
        """
        Close the async execution manager and cleanup resources.

        This should be called when the BrainClient is no longer needed
        to ensure proper cleanup of background tasks and connections.
        """
        if self._async_execution_manager is not None:
            try:
                await self._async_execution_manager.stop()
                self._async_execution_manager = None
                logger.debug("Async execution manager closed successfully")
            except Exception as e:
                logger.error(f"Error closing async execution manager: {e}")
                raise
