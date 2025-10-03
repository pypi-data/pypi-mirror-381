import asyncio
import inspect
import os
import re
import socket
import subprocess
import threading
import time
import urllib.parse
from datetime import datetime
from functools import wraps
from typing import Any, Callable, List, Optional, Union, get_type_hints, Type, Dict, Literal
from brain_sdk.agent_ai import AgentAI
from brain_sdk.agent_brain import AgentBrain
from brain_sdk.agent_mcp import AgentMCP
from brain_sdk.agent_registry import clear_current_agent, set_current_agent
from brain_sdk.agent_server import AgentServer
from brain_sdk.agent_workflow import AgentWorkflow
from brain_sdk.client import BrainClient
from brain_sdk.dynamic_skills import DynamicMCPSkillManager
from brain_sdk.execution_context import ExecutionContext, get_current_context, set_execution_context, reset_execution_context
from brain_sdk.did_manager import DIDManager, DIDExecutionContext
from brain_sdk.vc_generator import VCGenerator
from brain_sdk.mcp_client import MCPClientRegistry
from brain_sdk.mcp_manager import MCPManager
from brain_sdk.memory import MemoryClient, MemoryInterface
from brain_sdk.memory_events import MemoryEventClient
from brain_sdk.logger import log_debug, log_error, log_info, log_warn
from brain_sdk.router import AgentRouter
from brain_sdk.connection_manager import ConnectionManager, ConnectionConfig
from brain_sdk.types import AgentStatus, AIConfig, MemoryConfig
from brain_sdk.multimodal_response import MultimodalResponse
from brain_sdk.async_config import AsyncConfig
from brain_sdk.async_execution_manager import AsyncExecutionManager
from brain_sdk.pydantic_utils import convert_function_args, should_convert_args
from fastapi import FastAPI, Request, HTTPException
from fastapi.routing import APIRoute
from pydantic import create_model, BaseModel, ValidationError

# Import aiohttp for fire-and-forget HTTP calls
try:
    import aiohttp
except ImportError:
    aiohttp = None


def _detect_container_ip() -> Optional[str]:
    """
    Detect the external IP address when running in a containerized environment.
    
    Returns:
        External IP address if detected, None otherwise
    """
    try:
        # Try to get IP from container metadata (works in many hosted environments)
        import requests
        
        # Try AWS metadata service
        try:
            response = requests.get(
                "http://169.254.169.254/latest/meta-data/public-ipv4",
                timeout=2
            )
            if response.status_code == 200:
                return response.text.strip()
        except:
            pass
        
        # Try Google metadata service
        try:
            response = requests.get(
                "http://metadata.google.internal/computeMetadata/v1/instance/network-interfaces/0/access-configs/0/external-ip",
                headers={"Metadata-Flavor": "Google"},
                timeout=2
            )
            if response.status_code == 200:
                return response.text.strip()
        except:
            pass
        
        # Try Azure metadata service
        try:
            response = requests.get(
                "http://169.254.169.254/metadata/instance/network/interface/0/ipv4/ipAddress/0/publicIpAddress?api-version=2021-02-01",
                headers={"Metadata": "true"},
                timeout=2
            )
            if response.status_code == 200:
                import json
                data = json.loads(response.text)
                return data
        except:
            pass
        
        # Fallback: try to get external IP via external service
        try:
            response = requests.get("https://api.ipify.org", timeout=5)
            if response.status_code == 200:
                return response.text.strip()
        except:
            pass
            
    except ImportError:
        pass
    
    return None


def _detect_local_ip() -> Optional[str]:
    """
    Detect the local IP address of the machine.
    
    Returns:
        Local IP address if detected, None otherwise
    """
    try:
        # Connect to a remote address to determine local IP
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except:
        return None


def _is_running_in_container() -> bool:
    """
    Detect if the application is running inside a container.
    
    Returns:
        True if running in a container, False otherwise
    """
    try:
        # Check for Docker container indicators
        if os.path.exists("/.dockerenv"):
            return True
        
        # Check cgroup for container indicators
        try:
            with open("/proc/1/cgroup", "r") as f:
                content = f.read()
                if "docker" in content or "containerd" in content or "kubepods" in content:
                    return True
        except:
            pass
        
        # Check for Kubernetes environment variables
        if any(key.startswith("KUBERNETES_") for key in os.environ):
            return True
            
        # Check for common container environment variables
        container_vars = ["CONTAINER", "DOCKER_CONTAINER", "RAILWAY_ENVIRONMENT"]
        if any(var in os.environ for var in container_vars):
            return True
            
    except:
        pass
    
    return False


def _normalize_candidate(candidate: str, port: int) -> Optional[str]:
    """Normalize a callback candidate into scheme://host:port form."""
    if not candidate:
        return None

    candidate = candidate.strip()
    if not candidate:
        return None

    # Ensure we have a scheme so urlparse behaves predictably
    if "://" not in candidate:
        candidate = f"http://{candidate}"

    try:
        parsed = urllib.parse.urlparse(candidate)
    except Exception:
        return None

    scheme = parsed.scheme or "http"

    host = parsed.hostname or ""
    if not host:
        # Some inputs might be bare hostnames found in .path
        host = parsed.path

    host = host.strip("[]")  # We'll add brackets for IPv6 later if needed
    if not host:
        return None

    # Determine port precedence: explicit candidate port, fallback parameter
    candidate_port = parsed.port
    if not candidate_port and port:
        candidate_port = port

    # IPv6 addresses need brackets
    if ":" in host and not host.startswith("[") and not host.endswith("]"):
        host = f"[{host}]"

    if candidate_port:
        netloc = f"{host}:{candidate_port}"
    else:
        netloc = host

    return f"{scheme}://{netloc}"


def _build_callback_candidates(
    callback_url: Optional[str], port: int, *, include_defaults: bool = True
) -> List[str]:
    """Assemble a prioritized list of callback URL candidates."""

    candidates: List[str] = []
    seen: set[str] = set()

    def add_candidate(raw: Optional[str]):
        normalized = _normalize_candidate(raw or "", port)
        if normalized and normalized not in seen:
            candidates.append(normalized)
            seen.add(normalized)

    # 1. Explicit configuration
    add_candidate(callback_url)

    # 2. Environment override
    env_callback_url = os.getenv("AGENT_CALLBACK_URL")
    add_candidate(env_callback_url)

    # 3. Container/platform-specific hints
    if _is_running_in_container():
        railway_service_name = os.getenv("RAILWAY_SERVICE_NAME")
        railway_environment = os.getenv("RAILWAY_ENVIRONMENT")
        if railway_service_name and railway_environment:
            add_candidate(f"http://{railway_service_name}.railway.internal:{port}")

        external_ip = _detect_container_ip()
        if external_ip:
            add_candidate(f"http://{external_ip}:{port}")

    # 4. Local network hints
    local_ip = _detect_local_ip()
    if local_ip and local_ip not in {"127.0.0.1", "0.0.0.0"}:
        add_candidate(f"http://{local_ip}:{port}")

    hostname = socket.gethostname()
    if hostname:
        add_candidate(f"http://{hostname}:{port}")

    # Make host.docker.internal available even on Linux once mapped via extra_hosts
    add_candidate(f"http://host.docker.internal:{port}")

    # 5. Default fallbacks
    if include_defaults:
        add_candidate(f"http://localhost:{port}")
        add_candidate(f"http://127.0.0.1:{port}")

    return candidates


def _resolve_callback_url(callback_url: Optional[str], port: int) -> str:
    """
    Resolve the callback URL using the configuration hierarchy.
    
    Priority:
    1. Explicit callback_url parameter
    2. AGENT_CALLBACK_URL environment variable
    3. Auto-detection for containerized environments
    4. Fallback to localhost
    
    Args:
        callback_url: Explicit callback URL from constructor
        port: Port the agent will listen on
        
    Returns:
        Resolved callback URL
    """
    candidates = _build_callback_candidates(callback_url, port)
    if candidates:
        return candidates[0]
    return f"http://localhost:{port}"


class Agent(FastAPI):
    """
    Brain Agent - FastAPI subclass for creating AI agent nodes.
    
    The Agent class is the core component of the Brain SDK that enables developers to create
    intelligent agent nodes. It inherits from FastAPI to provide HTTP endpoints and integrates
    with the Brain ecosystem for distributed AI workflows.
    
    Key Features:
    - Decorator-based reasoner and skill registration
    - Cross-agent communication via the Brain execution gateway
    - Memory interface for persistent and session-based storage
    - MCP (Model Context Protocol) server integration
    - Automatic workflow tracking and DAG building
    - FastAPI-based HTTP API with automatic schema generation
    
    Example:
        ```python
        from brain_sdk import Agent
        
        # Create an agent instance
        app = Agent(
            node_id="my_agent",
            brain_server="http://localhost:8080"
        )
        
        # Define a reasoner (AI-powered function)
        @app.reasoner()
        async def analyze_sentiment(text: str) -> dict:
            result = await app.ai(
                prompt=f"Analyze sentiment of: {text}",
                response_model={"sentiment": "positive|negative|neutral", "confidence": "float"}
            )
            return result
        
        # Define a skill (deterministic function)
        @app.skill()
        def format_response(sentiment: str, confidence: float) -> str:
            return f"Sentiment: {sentiment} (confidence: {confidence:.2f})"
        
        # Start the agent server
        if __name__ == "__main__":
            app.serve(port=8001)
        ```
    """

    def __init__(
        self,
        node_id: str,
        brain_server: str = "http://localhost:8080",
        version: str = "1.0.0",
        ai_config: Optional[AIConfig] = None,
        memory_config: Optional[MemoryConfig] = None,
        dev_mode: bool = False,
        async_config: Optional[AsyncConfig] = None,
        callback_url: Optional[str] = None,
        **kwargs,
    ):
        """
        Initialize a new Brain Agent instance.

        Sets log level to DEBUG if dev_mode is True, else INFO.
        """
        # Set logging level based on dev_mode
        from brain_sdk.logger import set_log_level
        set_log_level("DEBUG" if dev_mode else "INFO")
        
        """
        Creates a new agent node that can host reasoners (AI-powered functions) and skills
        (deterministic functions) while integrating with the Brain ecosystem for distributed
        AI workflows and cross-agent communication.
        
        Args:
            node_id (str): Unique identifier for this agent node. Used for routing and
                          cross-agent communication. Should be descriptive and unique
                          within your Brain ecosystem.
            brain_server (str, optional): URL of the Brain server for registration and
                                        execution gateway. Defaults to "http://localhost:8080".
            version (str, optional): Version string for this agent. Used for compatibility
                                   checking and deployment tracking. Defaults to "1.0.0".
            ai_config (AIConfig, optional): Configuration for AI/LLM integration. If not
                                          provided, will be loaded from environment variables.
            memory_config (MemoryConfig, optional): Configuration for memory behavior including
                                                   auto-injection patterns and retention policies.
                                                   Defaults to session-based memory.
            dev_mode (bool, optional): Enable development mode with verbose logging and
                                     debugging features. Defaults to False.
            async_config (AsyncConfig, optional): Configuration for async execution behavior.
            callback_url (str, optional): Explicit callback URL for Brain server to reach this agent.
                                         If not provided, will use AGENT_CALLBACK_URL environment variable,
                                         auto-detection for containers, or fallback to localhost.
            **kwargs: Additional keyword arguments passed to FastAPI constructor.
        
        Example:
            ```python
            # Basic agent setup
            app = Agent(node_id="sentiment_analyzer")
            
            # Advanced configuration
            app = Agent(
                node_id="advanced_agent",
                brain_server="https://brain.company.com",
                version="2.1.0",
                ai_config=AIConfig(
                    provider="openai",
                    model="gpt-4",
                    api_key="your-key"
                ),
                memory_config=MemoryConfig(
                    auto_inject=["user_context", "conversation_history"],
                    memory_retention="persistent",
                    cache_results=True
                ),
                dev_mode=True
            )
            ```
        
        Note:
            The agent automatically initializes all necessary handlers for MCP integration,
            memory management, workflow tracking, and server functionality. MCP servers
            are discovered and started automatically if present in the agent directory.
        """
        super().__init__(**kwargs)

        self.node_id = node_id
        self.brain_server = brain_server
        self.version = version
        self.reasoners = []
        self.skills = []
        # Track declared return types separately to avoid polluting JSON metadata
        self._reasoner_return_types: Dict[str, Type] = {}
        self.base_url = None
        self.callback_candidates: List[str] = []
        self.callback_url = callback_url  # Store the explicit callback URL
        self._heartbeat_thread = None
        self._heartbeat_stop_event = threading.Event()
        self.dev_mode = dev_mode
        self.brain_connected = False
        
        # 🔥 FIX: Resolve callback URL immediately if provided
        # This ensures base_url is available before serve() is called
        if self.callback_url:
            # Use a default port for initial resolution - will be updated during serve()
            self.base_url = _resolve_callback_url(self.callback_url, 8000)
            if self.dev_mode:
                log_debug(f"Early callback URL resolution: {self.base_url}")
        
        # Initialize async configuration
        self.async_config = async_config or AsyncConfig.from_environment()
        
        # Initialize BrainClient with async configuration
        self.client = BrainClient(base_url=brain_server, async_config=self.async_config)
        self._current_execution_context: Optional[ExecutionContext] = None
        
        # Initialize async execution manager (will be lazily created when needed)
        self._async_execution_manager: Optional[AsyncExecutionManager] = None

        # Fast lifecycle management
        self._current_status: AgentStatus = AgentStatus.STARTING
        self._shutdown_requested = False
        self._mcp_initialization_complete = False
        self._start_time = time.time()  # Track start time for uptime calculation

        # Initialize AI and Memory configurations
        self.ai_config = (
            ai_config if ai_config else AIConfig.from_env()
        )
        self.memory_config = (
            memory_config
            if memory_config
            else MemoryConfig(
                auto_inject=[], memory_retention="session", cache_results=False
            )
        )

        # Add MCP management
        self.mcp_manager: Optional[MCPManager] = None
        self.mcp_client_registry: Optional[MCPClientRegistry] = None
        self.dynamic_skill_manager: Optional[DynamicMCPSkillManager] = None
        self.memory_event_client: Optional[MemoryEventClient] = None
        
        # Add DID management
        self.did_manager: Optional[DIDManager] = None
        self.vc_generator: Optional[VCGenerator] = None
        self.did_enabled = False

        # Add connection management for resilient Brain server connectivity
        self.connection_manager: Optional[ConnectionManager] = None

        # Initialize handlers
        self.ai_handler = AgentAI(self)
        self.mcp_handler = AgentMCP(self)
        self.brain_handler = AgentBrain(self)
        self.workflow_handler = AgentWorkflow(self)
        self.server_handler = AgentServer(self)
        
        # Register this agent instance for enhanced decorator system
        set_current_agent(self)

        # Initialize MCP components through the handler
        try:
            agent_dir = self.mcp_handler._detect_agent_directory()
            self.mcp_manager = MCPManager(agent_dir, self.dev_mode)
            self.mcp_client_registry = MCPClientRegistry(self.dev_mode)

            if self.dev_mode:
                log_debug(f"Initialized MCP Manager in {agent_dir}")

            # Initialize Dynamic Skill Manager when both MCP components are available
            if self.mcp_manager and self.mcp_client_registry:
                self.dynamic_skill_manager = DynamicMCPSkillManager(self, self.dev_mode)
                if self.dev_mode:
                    log_debug("Dynamic MCP skill manager initialized")

        except Exception as e:
            if self.dev_mode:
                log_error(f"Failed to initialize MCP Manager: {e}")
            self.mcp_manager = None
            self.mcp_client_registry = None
            self.dynamic_skill_manager = None

        # Initialize DID components
        self._initialize_did_system()

        # Setup standard Brain routes and memory event listeners
        self.server_handler.setup_brain_routes()
        self._register_memory_event_listeners()

        # Register this agent instance for automatic workflow tracking
        set_current_agent(self)

    def _initialize_did_system(self):
        """Initialize DID and VC components."""
        try:
            # Initialize DID Manager
            self.did_manager = DIDManager(self.brain_server, self.node_id)
            
            # Initialize VC Generator
            self.vc_generator = VCGenerator(self.brain_server)
            
            if self.dev_mode:
                log_debug("DID system initialized")
                
        except Exception as e:
            if self.dev_mode:
                log_error(f"Failed to initialize DID system: {e}")
            self.did_manager = None
            self.vc_generator = None

    def _register_memory_event_listeners(self):
        """Scans for methods decorated with @on_change and registers them as listeners."""
        if not self.memory_event_client:
            self.memory_event_client = MemoryEventClient(
                self.brain_server, self._get_current_execution_context()
            )

        for name, method in inspect.getmembers(self, predicate=inspect.ismethod):
            if hasattr(method, "_memory_event_listener"):
                patterns = getattr(method, "_memory_event_patterns", [])

                async def listener(event):
                    # This is a simplified listener, a more robust implementation
                    # would handle pattern matching on the client side as well.
                    await method(event)
                
                self.memory_event_client.subscribe(patterns, listener)

    @property
    def memory(self) -> Optional[MemoryInterface]:
        """
        Get the memory interface for the current execution context.
        
        The memory interface provides access to persistent and session-based storage
        that is automatically scoped to the current execution context. This enables
        agents to store and retrieve data across function calls, workflow steps,
        and even across different agent interactions.
        
        Memory is automatically scoped by:
        - Execution context (workflow instance)
        - Agent node ID
        - Session information
        - User context (if available)
        
        Returns:
            MemoryInterface: Interface for memory operations if execution context is available.
            None: If no execution context is available (e.g., outside of reasoner/skill execution).
            
        Example:
            ```python
            @app.reasoner()
            async def analyze_conversation(message: str) -> dict:
                '''Analyze message with conversation history context.'''
                
                # Store current message in conversation history
                history = app.memory.get("conversation.history", [])
                history.append({
                    "message": message,
                    "timestamp": datetime.now().isoformat(),
                    "role": "user"
                })
                app.memory.set("conversation.history", history)
                
                # Get user preferences for analysis
                user_prefs = app.memory.get("user.analysis_preferences", {
                    "sentiment_analysis": True,
                    "topic_extraction": True,
                    "language_detection": False
                })
                
                # Perform analysis based on preferences and history
                analysis_prompt = f'''
                Analyze this message: "{message}"
                
                Previous conversation context:
                {json.dumps(history[-5:], indent=2)}  # Last 5 messages
                
                Analysis preferences: {user_prefs}
                '''
                
                result = await app.ai(
                    system="You are a conversation analyst.",
                    user=analysis_prompt,
                    schema=ConversationAnalysis
                )
                
                # Store analysis results
                app.memory.set("conversation.last_analysis", result.model_dump())
                
                return result
            
            @app.skill()
            def get_conversation_summary() -> dict:
                '''Get summary of current conversation.'''
                
                history = app.memory.get("conversation.history", [])
                last_analysis = app.memory.get("conversation.last_analysis", {})
                
                return {
                    "message_count": len(history),
                    "last_analysis": last_analysis,
                    "conversation_started": history[0]["timestamp"] if history else None
                }
            ```
            
        Memory Operations:
            - `app.memory.get(key, default=None)`: Retrieve value by key
            - `app.memory.set(key, value)`: Store value by key
            - `app.memory.delete(key)`: Remove value by key
            - `app.memory.exists(key)`: Check if key exists
            - `app.memory.keys(pattern="*")`: List keys matching pattern
            - `app.memory.clear(pattern="*")`: Clear keys matching pattern
            
        Memory Scopes:
            - Session: Data persists for the duration of a user session
            - Workflow: Data persists for the duration of a workflow execution
            - Agent: Data persists across all executions for this agent
            - Global: Data shared across all agents (use with caution)
            
        Note:
            - Memory is automatically cleaned up based on retention policies
            - Large objects should be stored efficiently (consider serialization)
            - Memory operations are atomic and thread-safe
            - Memory events can trigger `@on_change` listeners
        """
        if not self._current_execution_context:
            return None

        memory_client = MemoryClient(self.client, self._current_execution_context)
        if not self.memory_event_client:
            self.memory_event_client = MemoryEventClient(
                self.brain_server, self._get_current_execution_context()
            )
        return MemoryInterface(memory_client, self.memory_event_client)

    def _populate_execution_context_with_did(self, execution_context, did_execution_context):
        """
        Populate the execution context with DID information.
        
        Args:
            execution_context: The main ExecutionContext
            did_execution_context: The DIDExecutionContext with DID info
        """
        if did_execution_context:
            execution_context.session_id = did_execution_context.session_id
            execution_context.caller_did = did_execution_context.caller_did
            execution_context.target_did = did_execution_context.target_did
            execution_context.agent_node_did = did_execution_context.agent_node_did

    async def _generate_vc_async(self, vc_generator, did_execution_context, function_name, input_data, output_data, status="success", error_message=None, duration_ms=0):
        """
        Generate VC asynchronously without blocking execution.
        
        Args:
            vc_generator: VCGenerator instance
            did_execution_context: DID execution context
            function_name: Name of the executed function
            input_data: Input data for the execution
            output_data: Output data from the execution
            status: Execution status
            error_message: Error message if any
            duration_ms: Execution duration in milliseconds
        """
        try:
            if vc_generator and vc_generator.is_enabled():
                vc = vc_generator.generate_execution_vc(
                    execution_context=did_execution_context,
                    input_data=input_data,
                    output_data=output_data,
                    status=status,
                    error_message=error_message,
                    duration_ms=duration_ms
                )
                if vc and self.dev_mode:
                    log_debug(f"Generated VC {vc.vc_id} for {function_name}")
        except Exception as e:
            if self.dev_mode:
                log_error(f"Failed to generate VC for {function_name}: {e}")

    def _build_callback_discovery_payload(self) -> Optional[Dict[str, Any]]:
        """Prepare discovery metadata for agent registration."""

        if not self.callback_candidates:
            return None

        payload: Dict[str, Any] = {
            "mode": "python-sdk:auto",
            "preferred": self.base_url,
            "callback_candidates": self.callback_candidates,
            "container": _is_running_in_container(),
            "submitted_at": datetime.utcnow().isoformat() + "Z",
        }

        return payload

    def _apply_discovery_response(self, payload: Optional[Dict[str, Any]]) -> None:
        """Update agent networking state from Brain discovery response."""

        if not payload:
            return

        discovery_section = payload.get("callback_discovery") if isinstance(payload, dict) else None

        resolved = None
        if isinstance(payload, dict):
            resolved = payload.get("resolved_base_url")
        if not resolved and isinstance(discovery_section, dict):
            resolved = (
                discovery_section.get("resolved")
                or discovery_section.get("selected")
                or discovery_section.get("preferred")
            )

        if resolved and resolved != self.base_url:
            log_debug(f"Applying resolved callback URL from Brain: {resolved}")
            self.base_url = resolved

        if isinstance(discovery_section, dict):
            candidates = discovery_section.get("candidates")
            if isinstance(candidates, list):
                normalized = []
                for candidate in candidates:
                    if isinstance(candidate, str):
                        normalized.append(candidate)
                # Ensure resolved URL is first when present
                if resolved and resolved in normalized:
                    normalized.remove(resolved)
                    normalized.insert(0, resolved)
                elif resolved:
                    normalized.insert(0, resolved)

                if normalized:
                    self.callback_candidates = normalized

    def _register_agent_with_did(self) -> bool:
        """
        Register agent with DID system.
        
        Returns:
            True if registration successful, False otherwise
        """
        if self.dev_mode:
            log_debug(f"Registering agent with DID system: {self.node_id}")

        if not self.did_manager:
            if self.dev_mode:
                log_debug(f"No DID manager available for agent: {self.node_id}")
            return False

        try:
            
            # Prepare reasoner and skill definitions for DID registration
            reasoner_defs = []
            for reasoner in self.reasoners:
                reasoner_defs.append({
                    "id": reasoner["id"],
                    "input_schema": reasoner["input_schema"],
                    "output_schema": reasoner["output_schema"]
                })
            
            skill_defs = []
            for skill in self.skills:
                skill_defs.append({
                    "id": skill["id"],
                    "input_schema": skill["input_schema"],
                    "tags": skill.get("tags", [])
                })
            
            log_debug(
                "Calling did_manager.register_agent() with "
                f"{len(reasoner_defs)} reasoners and {len(skill_defs)} skills"
            )
            
            # Register with DID system
            success = self.did_manager.register_agent(reasoner_defs, skill_defs)
            if success:
                self.did_enabled = True
                if self.dev_mode:
                    log_debug(f"DID registration successful for agent: {self.node_id}")
                # Enable VC generation
                if self.vc_generator:
                    self.vc_generator.set_enabled(True)
                if self.dev_mode:
                    log_info(f"Agent {self.node_id} registered with DID system")
                    log_info(f"DID: {self.did_manager.get_agent_did()}")
            else:
                if self.dev_mode:
                    log_warn(f"Failed to register agent {self.node_id} with DID system")

            return success

        except Exception as e:
            if self.dev_mode:
                log_error(f"Error registering agent with DID system: {e}")
            return False

    def _register_mcp_servers_with_registry(self) -> None:
        """
        Placeholder for MCP server registration - functionality removed.
        """
        if self.dev_mode:
            log_debug("MCP server registration disabled - old modules removed")

    def _setup_brain_routes(self):
        """Delegate to server handler for route setup"""
        return self.server_handler.setup_brain_routes()

    def reasoner(self, path: Optional[str] = None, name: Optional[str] = None):
        """
        Decorator to register a reasoner function.

        A reasoner is an AI-powered function that takes input and produces structured output using LLMs.
        It automatically handles input/output schema generation and integrates with the Brain's AI capabilities.

        Args:
            path (str, optional): The API endpoint path for this reasoner. Defaults to /reasoners/{function_name}.
            name (str, optional): Explicit Brain registration ID. Defaults to the function name.
        """

        def decorator(func: Callable) -> Callable:
            # Extract function metadata
            func_name = func.__name__
            reasoner_id = name or func_name
            endpoint_path = path or f"/reasoners/{func_name}"

            # Get type hints for input/output schemas
            type_hints = get_type_hints(func)
            sig = inspect.signature(func)

            # Create input schema from function parameters
            input_fields = {}
            for param_name, param in sig.parameters.items():
                if param_name not in ["self", "execution_context"]:
                    param_type = type_hints.get(param_name, str)
                    
                    # Check if parameter has a default value
                    if param.default != inspect.Parameter.empty:
                        # Parameter has default value - make it optional
                        input_fields[param_name] = (param_type, param.default)
                    else:
                        # Parameter is required
                        input_fields[param_name] = (param_type, ...)

            InputSchema = create_model(f"{func_name}Input", **input_fields)

            # Get output schema from return type hint
            return_type = type_hints.get("return", dict)

            # Create FastAPI endpoint
            @self.post(endpoint_path, response_model=return_type)
            async def endpoint(input_data: InputSchema, request: Request):
                import asyncio
                import time
                from brain_sdk.execution_context import set_execution_context, reset_execution_context
                
                # Extract execution context from request headers
                execution_context = ExecutionContext.from_request(request, self.node_id)
                payload_dict = input_data.model_dump()

                # 🔥 CRITICAL FIX: Synchronize BOTH context systems
                self._current_execution_context = execution_context  # Agent-level
                context_token = set_execution_context(execution_context)  # Thread-local

                # Set this agent as current for MCP skills
                self._set_as_current()

                # 🔥 NEW: Send workflow update for parent execution context
                # This ensures the parent node appears in the workflow DAG
                if hasattr(self, 'workflow_handler') and self.workflow_handler:
                    # Update reasoner name in context
                    execution_context.reasoner_name = reasoner_id

                    # Send start notification for the parent execution synchronously so ordering is preserved
                    await self.workflow_handler.notify_call_start(
                        execution_context.execution_id,
                        execution_context,
                        reasoner_id,
                        payload_dict,
                        parent_execution_id=execution_context.parent_execution_id,
                    )

                start_time = time.time()
                
                # Create DID execution context if DID system is enabled
                did_execution_context = None
                if self.did_enabled and self.did_manager:
                    did_execution_context = self.did_manager.create_execution_context(
                        execution_context.execution_id,
                        execution_context.workflow_id,
                        execution_context.workflow_id,  # Use workflow_id as session_id for now
                        "agent",  # caller function
                        reasoner_id  # target function
                    )
                    # Populate execution context with DID information
                    self._populate_execution_context_with_did(execution_context, did_execution_context)
                
                try:
                    # 🔥 NEW: Convert input to function arguments with automatic Pydantic model conversion
                    # This ensures FastAPI-like behavior for reasoner endpoints
                    try:
                        if should_convert_args(func):
                            # Use our conversion utility to convert dict arguments to Pydantic models
                            converted_args, converted_kwargs = convert_function_args(func, (), payload_dict)
                            args = converted_args
                            kwargs = converted_kwargs
                        else:
                            # No Pydantic models detected, use original behavior
                            args = ()
                            kwargs = payload_dict
                    except ValidationError as e:
                        # Re-raise validation errors with context
                        raise ValidationError(
                            f"Pydantic validation failed for reasoner '{reasoner_id}': {e}",
                            model=getattr(e, 'model', None)
                        ) from e
                    except Exception as e:
                        # Log conversion errors but continue with original args for backward compatibility
                        if self.dev_mode:
                            log_debug(f"⚠️ Warning: Failed to convert arguments for {reasoner_id}: {e}")
                        args = ()
                        kwargs = payload_dict

                    # Inject execution context if the function accepts it
                    if "execution_context" in sig.parameters:
                        kwargs["execution_context"] = execution_context

                    # Call the original function
                    if asyncio.iscoroutinefunction(func):
                        result = await func(*args, **kwargs)
                    else:
                        result = func(*args, **kwargs)

                    # Generate VC asynchronously if DID is enabled
                    if self.did_enabled and self.vc_generator and did_execution_context:
                        if self.dev_mode:
                            log_debug(f"Triggering VC generation for execution: {did_execution_context.execution_id}")
                        end_time = time.time()
                        duration_ms = int((end_time - start_time) * 1000)
                        asyncio.create_task(
                            self._generate_vc_async(
                                self.vc_generator,
                                did_execution_context,
                                reasoner_id,
                                payload_dict,
                                result,
                                "success",
                                None,
                                duration_ms
                            )
                        )

                    # 🔥 NEW: Send completion notification for parent execution
                    if hasattr(self, 'workflow_handler') and self.workflow_handler:
                        end_time = time.time()
                        await self.workflow_handler.notify_call_complete(
                            execution_context.execution_id,
                            execution_context.workflow_id,
                            result,
                            int((end_time - start_time) * 1000),
                            execution_context,  # 🔥 FIX: Pass execution_context to get parent_workflow_id
                            input_data=payload_dict,  # 🔧 FIX: Pass actual input data
                            parent_execution_id=execution_context.parent_execution_id,
                        )

                    return result
                except asyncio.CancelledError as cancel_err:
                    if hasattr(self, 'workflow_handler') and self.workflow_handler:
                        end_time = time.time()
                        await self.workflow_handler.notify_call_error(
                            execution_context.execution_id,
                            execution_context.workflow_id,
                            "Execution cancelled by upstream client",
                            int((end_time - start_time) * 1000),
                            execution_context,
                            input_data=payload_dict,
                            parent_execution_id=execution_context.parent_execution_id,
                        )
                    raise cancel_err
                except HTTPException as http_exc:
                    if hasattr(self, 'workflow_handler') and self.workflow_handler:
                        end_time = time.time()
                        detail = getattr(http_exc, "detail", None) or str(http_exc)
                        await self.workflow_handler.notify_call_error(
                            execution_context.execution_id,
                            execution_context.workflow_id,
                            detail,
                            int((end_time - start_time) * 1000),
                            execution_context,
                            input_data=payload_dict,
                            parent_execution_id=execution_context.parent_execution_id,
                        )
                    raise
                except Exception as e:
                    # 🔥 NEW: Send error notification for parent execution
                    if hasattr(self, 'workflow_handler') and self.workflow_handler:
                        end_time = time.time()
                        await self.workflow_handler.notify_call_error(
                            execution_context.execution_id,
                            execution_context.workflow_id,
                            str(e),
                            int((end_time - start_time) * 1000),
                            execution_context,  # 🔥 FIX: Pass execution_context to get parent_workflow_id
                            input_data=payload_dict,  # 🔧 FIX: Pass actual input data
                            parent_execution_id=execution_context.parent_execution_id,
                        )
                    raise
                finally:
                    # 🔥 CRITICAL: Clean up both contexts
                    reset_execution_context(context_token)  # Thread-local cleanup
                    self._current_execution_context = None   # Agent-level cleanup
                    # Clear current agent after execution
                    self._clear_current()

            # 🔥 ENHANCED: Comprehensive function replacement for unified tracking
            original_func = func

            async def tracked_func(*args, **kwargs):
                """Enhanced tracked function with unified execution pipeline and context inheritance"""
                # 🔥 CRITICAL FIX: Always use workflow tracking for direct reasoner calls
                # The previous logic was preventing workflow notifications for direct calls
                
                # Check if we're in an enhanced decorator context first
                current_context = get_current_context()
                
                if current_context:
                    # We're in a context managed by the enhanced decorator system
                    # Use the enhanced decorator's tracking mechanism
                    from brain_sdk.decorators import _execute_with_tracking
                    return await _execute_with_tracking(original_func, *args, **kwargs)
                else:
                    # 🔥 FIX: Always use the agent's workflow handler for tracking
                    # This ensures that direct reasoner calls get proper workflow notifications
                    return await self.workflow_handler.execute_with_tracking(
                        original_func, args, kwargs
                    )
            
            # 🔥 FIX: Store reference to original function for FastAPI endpoint access
            setattr(tracked_func, '_original_func', original_func)
            setattr(tracked_func, '_is_tracked_replacement', True)

            # Register reasoner metadata
            output_schema = {}
            if hasattr(return_type, "model_json_schema"):
                # If it's a Pydantic model, get its schema
                output_schema = return_type.model_json_schema()
            elif hasattr(return_type, "__annotations__"):
                # If it's a typed class, create a simple schema
                output_schema = {"type": "object", "properties": {}}
            else:
                # Default schema for basic types
                output_schema = {"type": "object"}

            # Store reasoner metadata for registration (JSON serializable only)
            reasoner_metadata = {
                "id": reasoner_id,
                "input_schema": InputSchema.model_json_schema(),
                "output_schema": output_schema,
                "memory_config": self.memory_config.to_dict(),
                "return_type_hint": getattr(return_type, "__name__", str(return_type)),
            }
            
            self.reasoners.append(reasoner_metadata)
            # Preserve the actual return type for local schema reconstruction
            self._reasoner_return_types[reasoner_id] = return_type

            # 🔥 CRITICAL: Comprehensive function replacement (re-enabled for workflow tracking)
            self.workflow_handler.replace_function_references(
                original_func, tracked_func, func_name
            )

            if reasoner_id != func_name:
                setattr(self, reasoner_id, getattr(self, func_name, tracked_func))

            # The `ai` method is available via `self.ai` within the Agent class.
            # If you need to expose it directly on the decorated function,
            # consider a different pattern (e.g., a wrapper class or a global registry).
            return tracked_func

        return decorator

    def on_change(self, pattern: Union[str, List[str]]):
        """
        Decorator to mark a function as a memory event listener.
        
        This decorator allows functions to automatically respond to changes in the agent's
        memory system. When memory data matching the specified patterns is modified,
        the decorated function will be called with the change event details.
        
        Args:
            pattern (Union[str, List[str]]): Memory path pattern(s) to listen for changes.
                                           Supports glob-style patterns for flexible matching.
                                           Examples: "user.*", ["session.current_user", "workflow.status"]
        
        Returns:
            Callable: The decorated function configured as a memory event listener.
            
        Example:
            ```python
            @app.on_change("user.preferences.*")
            async def handle_preference_change(event):
                '''React to user preference changes.'''
                log_info(f"User preference changed: {event.path} = {event.new_value}")
                
                # Update related systems
                if event.path.endswith("theme"):
                    await update_ui_theme(event.new_value)
                elif event.path.endswith("language"):
                    await update_localization(event.new_value)
            
            @app.on_change(["session.user_id", "session.permissions"])
            async def handle_session_change(event):
                '''React to session-related changes.'''
                if event.path == "session.user_id":
                    # User logged in/out
                    await initialize_user_context(event.new_value)
                elif event.path == "session.permissions":
                    # Permissions updated
                    await refresh_access_controls(event.new_value)
            
            # Memory changes trigger the listeners automatically
            app.memory.set("user.preferences.theme", "dark")  # Triggers handle_preference_change
            app.memory.set("session.user_id", 12345)          # Triggers handle_session_change
            ```
            
        Note:
            - Listeners are called asynchronously when memory changes occur
            - Multiple patterns can be specified to listen for different memory paths
            - Event object contains path, old_value, new_value, and timestamp
            - Listeners should be lightweight to avoid blocking memory operations
        """

        def decorator(func: Callable) -> Callable:
            @wraps(func)
            async def wrapper(*args, **kwargs):
                return await func(*args, **kwargs)

            # Attach metadata to the function
            setattr(wrapper, "_memory_event_listener", True)
            setattr(
                wrapper,
                "_memory_event_patterns",
                pattern if isinstance(pattern, list) else [pattern],
            )
            return wrapper

        return decorator

    def skill(
        self,
        tags: Optional[List[str]] = None,
        path: Optional[str] = None,
        name: Optional[str] = None,
    ):
        """
        Decorator to register a skill function.

        A skill is a deterministic function designed for business logic, integrations, data processing,
        and non-AI operations. Skills are ideal for tasks that require consistent, predictable behavior
        such as API calls, database operations, calculations, or data transformations.

        The decorator automatically:
        - Generates input/output schemas from type hints
        - Creates FastAPI endpoints with proper validation
        - Integrates with workflow tracking and execution context
        - Enables cross-agent communication via the Brain execution gateway
        - Provides access to execution context and memory system

        Args:
            tags (List[str], optional): A list of tags for organizing and categorizing skills.
                                      Useful for grouping related functionality (e.g., ["database", "user_management"]).
            path (str, optional): Custom API endpoint path for this skill.
                                Defaults to "/skills/{function_name}".
            name (str, optional): Explicit Brain registration ID. Defaults to the function name.

        Returns:
            Callable: The decorated function with enhanced Brain integration.

        Example:
            ```python
            from typing import Dict, List
            from pydantic import BaseModel
            
            class UserData(BaseModel):
                id: int
                name: str
                email: str
                created_at: str
            
            @app.skill(tags=["database", "user_management"])
            def get_user_profile(user_id: int) -> "UserData":
                '''Retrieve user profile from database.'''
                
                # Deterministic database operation
                user = database.get_user(user_id)
                if not user:
                    raise ValueError(f"User {user_id} not found")
                
                return UserData(
                    id=user.id,
                    name=user.name,
                    email=user.email,
                    created_at=user.created_at.isoformat()
                )
            
            @app.skill(tags=["api", "external"])
            async def send_notification(
                user_id: int,
                message: str,
                channel: str = "email"
            ) -> Dict[str, str]:
                '''Send notification via external service.'''
                
                # External API integration
                response = await notification_service.send(
                    user_id=user_id,
                    message=message,
                    channel=channel
                )
                
                return {
                    "status": "sent",
                    "notification_id": response.id,
                    "channel": channel
                }
            
            # Usage in another agent:
            user = await app.call(
                "user_agent.get_user_profile",
                user_id=123
            )
            
            await app.call(
                "notification_agent.send_notification",
                user_id=123,
                message="Welcome to our platform!",
                channel="email"
            )
            ```

        Note:
            - Skills should be deterministic and side-effect aware
            - Skills can access `app.memory` for persistent storage
            - Execution context is automatically injected if the function accepts it
            - All skills are automatically tracked in workflow DAGs
            - Use skills for reliable, repeatable operations
        """

        def decorator(func: Callable) -> Callable:
            # Extract function metadata
            func_name = func.__name__
            skill_id = name or func_name
            endpoint_path = path or f"/skills/{func_name}"

            # Get type hints for input schema
            type_hints = get_type_hints(func)
            sig = inspect.signature(func)

            # Create input schema from function parameters
            input_fields = {}
            for param_name, param in sig.parameters.items():
                if param_name not in ["self", "execution_context"]:
                    param_type = type_hints.get(param_name, str)
                    input_fields[param_name] = (param_type, ...)

            InputSchema = create_model(f"{func_name}Input", **input_fields)

            # Get output schema from return type hint
            return_type = type_hints.get("return", dict)

            # Create FastAPI endpoint
            @self.post(endpoint_path, response_model=return_type)
            async def endpoint(input_data: InputSchema, request: Request):
                # Extract execution context from request headers
                execution_context = ExecutionContext.from_request(request, self.node_id)

                # Store current context for use in app.call()
                self._current_execution_context = execution_context

                # Create DID execution context if DID system is enabled
                did_execution_context = None
                if self.did_enabled and self.did_manager:
                    did_execution_context = self.did_manager.create_execution_context(
                        execution_context.execution_id,
                        execution_context.workflow_id,
                        execution_context.workflow_id,  # Use workflow_id as session_id for now
                        "agent",  # caller function
                        skill_id  # target function
                    )
                    # Populate execution context with DID information
                    self._populate_execution_context_with_did(execution_context, did_execution_context)

                # Convert input to function arguments
                kwargs = input_data.model_dump()

                # Inject execution context if the function accepts it
                if "execution_context" in sig.parameters:
                    kwargs["execution_context"] = execution_context

                # Record start time for VC generation
                start_time = time.time()

                # 🔥 FIX: Call the original function directly to prevent double tracking
                # The FastAPI endpoint already handles tracking, so we don't want the tracked wrapper
                original_func = getattr(func, '_original_func', func)
                if asyncio.iscoroutinefunction(original_func):
                    result = await original_func(**kwargs)
                else:
                    result = original_func(**kwargs)
                
                # Generate VC asynchronously if DID is enabled
                if self.did_enabled and self.vc_generator and did_execution_context:
                    end_time = time.time()
                    duration_ms = int((end_time - start_time) * 1000)
                    asyncio.create_task(
                        self._generate_vc_async(
                            self.vc_generator,
                            did_execution_context,
                            skill_id,
                            input_data.model_dump(),
                            result,
                            "success",
                            None,
                            duration_ms
                        )
                    )

                return result

            # Register skill metadata
            self.skills.append(
                {
                    "id": skill_id,
                    "input_schema": InputSchema.model_json_schema(),
                    "tags": tags or [],
                }
            )

            if skill_id != func_name:
                setattr(self, skill_id, getattr(self, func_name, func))

            return func

        return decorator

    def include_router(
        self,
        router,
        prefix: str = "",
        tags: Optional[List[str]] = None,
    ) -> None:
        """Augment FastAPI's include_router to understand AgentRouter."""

        if isinstance(router, AgentRouter):
            router._attach_agent(self)
            normalized_prefix = prefix.rstrip("/") if prefix else ""

            def _sanitize_prefix_for_id(value: Optional[str]) -> List[str]:
                if not value:
                    return []

                cleaned = value.strip("/")
                if not cleaned:
                    return []

                segments: List[str] = []
                for segment in cleaned.split("/"):
                    sanitized = re.sub(r"[^0-9a-zA-Z]+", "_", segment)
                    sanitized = re.sub(r"_+", "_", sanitized).strip("_")
                    if sanitized:
                        segments.append(sanitized.lower())
                return segments

            def _build_prefixed_name(parts: List[str], base: str) -> str:
                if not parts:
                    return base
                prefix_part = "_".join(parts)
                return f"{prefix_part}_{base}"

            namespace_segments = _sanitize_prefix_for_id(getattr(router, "prefix", ""))

            for entry in router.reasoners:
                if entry.get("registered"):
                    continue

                func = entry["func"]
                default_path = f"/reasoners/{func.__name__}"
                resolved_path = router._combine_path(
                    default=default_path,
                    custom=entry.get("path"),
                    override_prefix=normalized_prefix,
                )

                entry_kwargs = entry.get("kwargs", {})
                explicit_reasoner_name = entry_kwargs.get("name")
                reasoner_id = explicit_reasoner_name or _build_prefixed_name(
                    namespace_segments,
                    func.__name__,
                )

                decorated = self.reasoner(path=resolved_path, name=reasoner_id)(func)
                entry["func"] = decorated
                entry["registered"] = True

            for entry in router.skills:
                if entry.get("registered"):
                    continue

                func = entry["func"]
                default_path = f"/skills/{func.__name__}"
                resolved_path = router._combine_path(
                    default=default_path,
                    custom=entry.get("path"),
                    override_prefix=normalized_prefix,
                )

                merged_tags: List[str] = []
                if tags:
                    merged_tags.extend(tags)
                merged_tags.extend(entry.get("tags", []))
                tag_arg: Optional[List[str]] = merged_tags if merged_tags else None

                entry_kwargs = entry.get("kwargs", {})
                explicit_skill_name = entry_kwargs.get("name")
                skill_id = explicit_skill_name or _build_prefixed_name(
                    namespace_segments,
                    func.__name__,
                )

                decorated = self.skill(
                    tags=tag_arg,
                    path=resolved_path,
                    name=skill_id,
                )(func)
                entry["func"] = decorated
                entry["registered"] = True

            return

        return super().include_router(router, prefix=prefix, tags=tags)

    async def ai(  # pragma: no cover - relies on external LLM services
        self,
        *args: Any,
        system: Optional[str] = None,
        user: Optional[str] = None,
        schema: Optional[Type[BaseModel]] = None,
        model: Optional[str] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        stream: Optional[bool] = None,
        response_format: Optional[Union[Literal["auto", "json", "text"], Dict]] = None,
        context: Optional[Dict] = None,
        memory_scope: Optional[List[str]] = None,
        **kwargs,
    ) -> Any:
        """
        AI interface for LLM interactions with direct keyword argument support.
        
        This method provides direct access to the AI functionality, allowing users to
        call `app.ai(...)` with keyword arguments for seamless LLM interactions.
        
        Args:
            *args: Flexible inputs - text, images, audio, files, or mixed content.
                   - str: Text content, URLs, or file paths (auto-detected).
                   - bytes: Binary data (images, audio, documents).
                   - dict: Structured input with explicit keys (e.g., {"image": "url"}).
                   - list: Multimodal conversation or content list.
            system (str, optional): System prompt for AI behavior.
            user (str, optional): User message (alternative to positional args).
            schema (Type[BaseModel], optional): Pydantic model for structured output validation.
            model (str, optional): Override default model (e.g., "gpt-4", "claude-3").
            temperature (float, optional): Creativity level (0.0-2.0).
            max_tokens (int, optional): Maximum response length.
            stream (bool, optional): Enable streaming response.
            response_format (str, optional): Desired response format ('auto', 'json', 'text').
            context (Dict, optional): Additional context data to pass to the LLM.
            memory_scope (List[str], optional): Memory scopes to inject (e.g., ['workflow', 'session', 'reasoner']).
            **kwargs: Additional provider-specific parameters to pass to the LLM.
        
        Returns:
            Any: The AI response - raw text, structured object (if schema), or a stream.
            
        Example:
            ```python
            # Direct usage with keyword arguments
            response = await app.ai(
                system="You are a helpful assistant",
                user="What is the capital of France?",
                model="gpt-4",
                temperature=0.7
            )
            
            # Structured output
            class SentimentResult(BaseModel):
                sentiment: str
                confidence: float
            
            result = await app.ai(
                "Analyze sentiment of: I love this!",
                schema=SentimentResult
            )
            
            # Multimodal input
            response = await app.ai(
                "Describe this image:",
                "https://example.com/image.jpg"
            )
            
            # Simple text input
            response = await app.ai("Summarize this document.")
            ```
        """
        return await self.ai_handler.ai(
            *args,
            system=system,
            user=user,
            schema=schema,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            stream=stream,
            response_format=response_format,
            context=context,
            memory_scope=memory_scope,
            **kwargs
        )

    async def ai_with_audio(  # pragma: no cover - relies on external audio services
        self,
        *args: Any,
        voice: Optional[str] = None,
        format: Optional[str] = None,
        model: Optional[str] = None,
        mode: Optional[str] = None,
        **kwargs
    ) -> "MultimodalResponse":
        """
        AI interface optimized for audio generation.
        
        This method is specifically designed for generating audio content from text prompts.
        It automatically configures the AI request for audio output and returns a
        MultimodalResponse with convenient audio access methods.
        
        Args:
            *args: Text prompts or multimodal inputs for audio generation.
            voice (str, optional): Voice to use for audio generation.
                                 Available options: alloy, echo, fable, onyx, nova, shimmer.
            format (str, optional): Audio format (wav, mp3). Defaults to wav.
            model (str, optional): Model to use for audio generation.
                                 Defaults to gpt-4o-audio-preview.
            **kwargs: Additional parameters passed to the AI method.
        
        Returns:
            MultimodalResponse: Response object with audio content and convenient access methods.
            
        Example:
            ```python
            # Basic audio generation
            response = await app.ai_with_audio("Explain quantum computing")
            response.audio.save("explanation.wav")
            
            # Custom voice and format
            response = await app.ai_with_audio(
                "Tell a bedtime story",
                voice="nova",
                format="mp3"
            )
            response.audio.play()
            ```
        """
        # Only pass parameters that are not None
        audio_kwargs = {}
        if voice is not None:
            audio_kwargs['voice'] = voice
        if format is not None:
            audio_kwargs['format'] = format
        if model is not None:
            audio_kwargs['model'] = model
        if mode is not None:
            audio_kwargs['mode'] = mode
        
        return await self.ai_handler.ai_with_audio(
            *args,
            **audio_kwargs,
            **kwargs
        )

    async def ai_with_vision(  # pragma: no cover - relies on external vision services
        self,
        *args: Any,
        size: Optional[str] = None,
        quality: Optional[str] = None,
        style: Optional[str] = None,
        model: Optional[str] = None,
        **kwargs
    ) -> "MultimodalResponse":
        """
        AI interface optimized for image generation and vision tasks.
        
        This method is designed for generating images from text prompts or analyzing
        visual content. It returns a MultimodalResponse with convenient image access methods.
        
        Args:
            *args: Text prompts or multimodal inputs for image generation/analysis.
            size (str, optional): Image size (e.g., "1024x1024", "1792x1024", "1024x1792").
            quality (str, optional): Image quality ("standard" or "hd").
            style (str, optional): Image style ("vivid" or "natural") for DALL-E 3.
            model (str, optional): Model to use for image generation. Defaults to dall-e-3.
            **kwargs: Additional parameters passed to the AI method.
        
        Returns:
            MultimodalResponse: Response object with image content and convenient access methods.
            
        Example:
            ```python
            # Basic image generation
            response = await app.ai_with_vision("A serene mountain landscape")
            response.images[0].save("landscape.png")
            
            # High-quality image with custom size
            response = await app.ai_with_vision(
                "Futuristic cityscape",
                size="1792x1024",
                quality="hd",
                style="vivid"
            )
            response.images[0].show()
            ```
        """
        # Only pass parameters that are not None
        vision_kwargs = {}
        if size is not None:
            vision_kwargs['size'] = size
        if quality is not None:
            vision_kwargs['quality'] = quality
        if style is not None:
            vision_kwargs['style'] = style
        if model is not None:
            vision_kwargs['model'] = model
        
        return await self.ai_handler.ai_with_vision(
            *args,
            **vision_kwargs,
            **kwargs
        )

    async def ai_with_multimodal(  # pragma: no cover - relies on external multimodal services
        self,
        *args: Any,
        modalities: Optional[List[str]] = None,
        audio_config: Optional[Dict] = None,
        image_config: Optional[Dict] = None,
        model: Optional[str] = None,
        **kwargs
    ) -> "MultimodalResponse":
        """
        AI interface with explicit multimodal control.
        
        This method provides fine-grained control over multimodal AI interactions,
        allowing you to specify exactly which output modalities you want and
        configure them individually.
        
        Args:
            *args: Multimodal inputs (text, images, audio, files).
            modalities (List[str], optional): Desired output modalities
                                            (e.g., ["text", "audio", "image"]).
            audio_config (Dict, optional): Audio generation configuration
                                         (voice, format, etc.).
            image_config (Dict, optional): Image generation configuration
                                         (size, quality, style, etc.).
            model (str, optional): Model to use for multimodal generation.
            **kwargs: Additional parameters passed to the AI method.
        
        Returns:
            MultimodalResponse: Response object with all requested modalities.
            
        Example:
            ```python
            # Request specific modalities
            response = await app.ai_with_multimodal(
                "Create a presentation about AI",
                modalities=["text", "audio"],
                audio_config={"voice": "alloy", "format": "wav"}
            )
            
            # Save all generated content
            files = response.save_all("./output", prefix="ai_presentation")
            ```
        """
        return await self.ai_handler.ai_with_multimodal(
            *args,
            modalities=modalities,
            audio_config=audio_config,
            image_config=image_config,
            model=model,
            **kwargs
        )

    async def call(self, target: str, *args, **kwargs) -> dict:
        """
        Initiates a cross-agent call to another reasoner or skill via the Brain execution gateway.

        This method allows agents to seamlessly communicate and utilize reasoners/skills
        deployed on other agent nodes within the Brain ecosystem. It properly propagates
        workflow tracking headers and maintains execution context for DAG building.

        **Return Type**: Always returns JSON/dict objects, similar to calling any REST API.
        No automatic schema conversion is performed - developers can convert to Pydantic
        models manually if needed.

        The method supports both positional and keyword arguments for maximum flexibility:
        - Pure keyword arguments (recommended): call("target", param1=value1, param2=value2)
        - Mixed positional and keyword: call("target", value1, value2, param3=value3)
        - Pure positional (auto-mapped): call("target", value1, value2, value3)

        Args:
            target (str): The full target ID in format "node_id.reasoner_name" or "node_id.skill_name"
                         (e.g., "classification_team.classify_ticket", "support_agent.send_email").
            *args: Positional arguments to pass to the target reasoner/skill. These will be
                   automatically mapped to the target function's parameter names in order.
            **kwargs: Keyword arguments to pass to the target reasoner/skill.

        Returns:
            dict: The result from the target reasoner/skill execution as JSON/dict.
                  Always returns dict objects, like calling any REST API.

        Examples:
            # Reasoner call - returns dict (convert to Pydantic manually if needed)
            result: dict = await app.call("sentiment_agent.analyze_sentiment",
                                         message="I love this product!",
                                         customer_id="cust_123")
            sentiment = SentimentResult(**result)  # Manual conversion if needed
            log_info(sentiment.confidence)

            # Skill call - returns dict
            result: dict = await app.call("notification_agent.send_email",
                                        "user@example.com",  # positional: to
                                        "Welcome!",          # positional: subject
                                        body="Thank you for signing up.")  # keyword

            # All calls return dict - consistent behavior
            analysis: dict = await app.call("content_agent.analyze_content",
                                           "This is great content!",  # content
                                           "blog_post")               # content_type

            # Error handling
            try:
                result = await app.call("some_agent.some_reasoner", data="test")
                # result is always a dict
            except Exception as e:
                log_error(f"Call failed: {e}")
        """
        # Handle argument mapping for flexibility
        final_kwargs = kwargs.copy()

        if args:
            # If positional arguments are provided, we need to map them to parameter names
            # For cross-agent calls, we don't have direct access to the target function signature,
            # so we'll use a simple mapping strategy:

            # Try to get parameter names from the target (if it's a local reasoner/skill)
            if "." in target:
                node_id, function_name = target.split(".", 1)

                # If calling a local function (same node), try to get its signature
                if node_id == self.node_id and hasattr(self, function_name):
                    try:
                        func = getattr(self, function_name)
                        sig = inspect.signature(func)
                        param_names = [
                            name
                            for name, param in sig.parameters.items()
                            if name not in ["self", "execution_context"]
                        ]

                        # Map positional args to parameter names
                        for i, arg in enumerate(args):
                            if i < len(param_names):
                                param_name = param_names[i]
                                if (
                                    param_name not in final_kwargs
                                ):  # Don't override explicit kwargs
                                    final_kwargs[param_name] = arg
                            else:
                                # More args than parameters - use generic names
                                final_kwargs[f"arg_{i}"] = arg

                    except Exception:
                        # Fallback to generic parameter names if signature inspection fails
                        for i, arg in enumerate(args):
                            final_kwargs[f"arg_{i}"] = arg
                else:
                    # Cross-agent call - use generic parameter names
                    # The receiving agent will need to handle the mapping
                    for i, arg in enumerate(args):
                        final_kwargs[f"arg_{i}"] = arg
            else:
                # Simple function name without node_id - use generic names
                for i, arg in enumerate(args):
                    final_kwargs[f"arg_{i}"] = arg

        # Get current execution context
        current_context = self._get_current_execution_context()

        # 🔧 DEBUG: Validate context before creating child
        if self.dev_mode:
            from brain_sdk.execution_context import get_current_context
            from brain_sdk.logger import log_debug
            log_debug(f"🔍 CALL_DEBUG: Making cross-agent call to {target}")
            log_debug(f"  Current execution_id: {current_context.execution_id}")
            log_debug(f"  Thread-local context exists: {get_current_context() is not None}")
            log_debug(f"  Agent-level context exists: {self._current_execution_context is not None}")

        # Create child context for the cross-agent call
        child_context = current_context.create_child_context()
        
        # Set the parent execution ID on the child context
        child_context.parent_execution_id = current_context.execution_id

        # 🔧 DEBUG: Validate child context
        if self.dev_mode:
            log_debug(f"🔍 CALL_DEBUG: Child context created")
            log_debug(f"  Child execution_id: {child_context.execution_id}")
            log_debug(f"  Parent execution_id: {child_context.parent_execution_id}")

        # Prepare headers with proper workflow tracking
        headers = child_context.to_headers()

        # DISABLED: Same-agent call detection - Force all calls through Brain server
        # This ensures all app.call() requests go through the Brain server for proper
        # workflow tracking, execution context, and distributed processing
        from brain_sdk.logger import log_debug
        
        log_debug(f"Cross-agent call to: {target}")

        # Check if Brain server is available for cross-agent calls
        if not self.brain_connected:
            from brain_sdk.logger import log_warn
            log_warn(f"Brain server unavailable - cannot make cross-agent call to {target}")
            raise Exception(f"Cross-agent call to {target} failed: Brain server unavailable. Agent is running in local mode.")

        # Use the enhanced BrainClient to make the call via execution gateway
        try:
            # Check for non-serializable parameters and convert them
            serialization_issues = []
            for key, value in final_kwargs.items():
                try:
                    import json
                    json.dumps(value, default=str)  # Test serialization
                except (TypeError, ValueError) as se:
                    serialization_issues.append(f"{key}: {type(value).__name__} - {str(se)}")
                    
                    # Try to convert common non-serializable types
                    if hasattr(value, 'value'):  # Enum with .value attribute
                        final_kwargs[key] = value.value
                    elif hasattr(value, '__dict__'):  # Object with attributes
                        final_kwargs[key] = value.__dict__
                    else:
                        final_kwargs[key] = str(value)
            
            if serialization_issues and self.dev_mode:
                log_debug(f"Converted {len(serialization_issues)} non-serializable parameters")
            
            import asyncio
            import time

            # Determine how long we're willing to wait for long-running executions.
            max_timeout = getattr(self.async_config, "max_execution_timeout", None)
            default_timeout = getattr(self.async_config, "default_execution_timeout", None)
            execution_timeout = max_timeout or default_timeout or 600.0
            # Guard against misconfiguration resulting in non-positive values.
            if execution_timeout <= 0:
                execution_timeout = 600.0

            start_time = time.time()
            
            # Check if async execution is enabled and available
            use_async_execution = (
                self.async_config.enable_async_execution and
                self.brain_connected
            )
            
            if use_async_execution:
                # Try async execution path
                try:
                    if self.dev_mode:
                        log_debug(f"Using async execution for target: {target}")
                    
                    # Submit async execution
                    execution_id = await self.client.execute_async(
                        target=target,
                        input_data=final_kwargs,
                        headers=headers,
                        timeout=execution_timeout
                    )
                    
                    # Wait for result with polling
                    result = await self.client.wait_for_execution_result(
                        execution_id=execution_id,
                        timeout=execution_timeout
                    )
                    
                    elapsed_time = time.time() - start_time
                    if self.dev_mode:
                        log_debug(f"Async execute call completed in {elapsed_time:.2f} seconds")
                    
                    # Extract the actual result from the response and return as dict
                    if isinstance(result, dict) and "result" in result:
                        extracted_result = result["result"]
                    else:
                        extracted_result = result

                    # Always return dict/JSON - no schema conversion
                    return extracted_result
                    
                except Exception as async_error:
                    if self.dev_mode:
                        log_debug(f"Async execution failed: {type(async_error).__name__}: {str(async_error)}")
                    
                    # Check if fallback to sync is enabled
                    if self.async_config.fallback_to_sync:
                        if self.dev_mode:
                            log_debug(f"Falling back to sync execution for target: {target}")
                        # Continue to sync execution below
                    else:
                        # Re-raise the async error if no fallback
                        raise async_error
            
            # Sync execution path (either by choice or as fallback)
            if self.dev_mode and use_async_execution:
                log_debug(f"Using sync execution as fallback for target: {target}")
            elif self.dev_mode:
                log_debug(f"Using sync execution for target: {target}")
            
            # Wrap the execute call with timeout and progress monitoring
            async def execute_with_monitoring():
                try:
                    result = await self.client.execute(
                        target=target, input_data=final_kwargs, headers=headers
                    )
                    return result
                except Exception as exec_error:
                    if self.dev_mode:
                        log_debug(f"Client execute failed: {type(exec_error).__name__}: {str(exec_error)}")
                    raise
            
            # Add a timeout to prevent infinite hangs using configured allowance for long workflows
            try:
                result = await asyncio.wait_for(
                    execute_with_monitoring(), timeout=execution_timeout
                )
                elapsed_time = time.time() - start_time
                if self.dev_mode:
                    log_debug(f"Sync execute call completed in {elapsed_time:.2f} seconds")
            except asyncio.TimeoutError:
                elapsed_time = time.time() - start_time
                log_debug(
                    f"Execute call timed out after {elapsed_time:.2f} seconds (limit {execution_timeout:.0f}s)"
                )
                raise Exception(
                    f"Cross-agent call to {target} timed out after {int(execution_timeout)} seconds"
                )

            # Extract the actual result from the response and return as dict
            if isinstance(result, dict) and "result" in result:
                extracted_result = result["result"]
            else:
                extracted_result = result

            # Always return dict/JSON - no schema conversion
            return extracted_result

        except Exception as e:
            if self.dev_mode:
                log_debug(f"Cross-agent call failed: {target} - {type(e).__name__}: {str(e)}")
            raise

    async def _get_async_execution_manager(self) -> AsyncExecutionManager:
        """
        Get or create the async execution manager instance.
        
        Returns:
            AsyncExecutionManager: The async execution manager instance
        """
        if self._async_execution_manager is None:
            # Create async execution manager with the same base URL as the client
            self._async_execution_manager = AsyncExecutionManager(
                base_url=self.brain_server,
                config=self.async_config
            )
            # Start the manager
            await self._async_execution_manager.start()
            
            if self.dev_mode:
                log_debug("AsyncExecutionManager initialized and started")
        
        return self._async_execution_manager

    async def _cleanup_async_resources(self) -> None:
        """
        Clean up async execution manager resources.
        
        This method should be called during agent shutdown to properly
        clean up async execution resources.
        """
        if self._async_execution_manager is not None:
            try:
                await self._async_execution_manager.stop()
                self._async_execution_manager = None
                if self.dev_mode:
                    log_debug("AsyncExecutionManager stopped and cleaned up")
            except Exception as e:
                if self.dev_mode:
                    log_debug(f"Error cleaning up AsyncExecutionManager: {e}")

        if getattr(self, "client", None) is not None:
            try:
                await self.client.aclose()
                if self.dev_mode:
                    log_debug("BrainClient resources closed")
            except Exception as e:
                if self.dev_mode:
                    log_debug(f"Error closing BrainClient resources: {e}")

    def note(self, message: str, tags: List[str] = None) -> None:
        """
        Add a note to the current execution for debugging and tracking purposes.
        
        This method sends a note to the Brain server asynchronously without blocking
        the current execution. The note is automatically associated with the current
        execution context and can be viewed in the Brain UI for debugging and monitoring.
        
        Args:
            message (str): The note message to log
            tags (List[str], optional): Optional tags to categorize the note
            
        Example:
            ```python
            @app.reasoner()
            async def process_data(data: str) -> dict:
                app.note("Starting data processing", ["debug", "processing"])
                
                # Process data...
                result = await some_processing(data)
                
                app.note(f"Processing completed with {len(result)} items", ["info"])
                return result
            ```
            
        Note:
            This method is fire-and-forget and runs asynchronously in the background.
            It will not block the current execution or raise exceptions that would
            interrupt the workflow.
        """
        if tags is None:
            tags = []
            
        # Fire-and-forget async task
        import asyncio
        
        async def _send_note():
            try:
                # Get current execution context
                current_context = self._get_current_execution_context()
                
                # Prepare headers with execution context
                headers = current_context.to_headers()
                headers["Content-Type"] = "application/json"
                
                # Prepare payload
                payload = {
                    "message": message,
                    "tags": tags,
                    "timestamp": time.time(),
                    "agent_node_id": self.node_id
                }
                
                # Make async HTTP request to backend - use UI API endpoint to match frontend
                try:
                    import aiohttp
                    timeout = aiohttp.ClientTimeout(total=5.0)  # 5 second timeout
                    # Use UI API base URL to match where frontend fetches notes from
                    # Replace the last occurrence of /api/v1 with /api/ui/v1
                    ui_api_base = self.client.api_base.replace("/api/v1", "/api/ui/v1")
                    
                    if self.dev_mode:
                        from brain_sdk.logger import log_debug
                        log_debug(f"NOTE DEBUG: Original api_base: {self.client.api_base}")
                        log_debug(f"NOTE DEBUG: UI api_base: {ui_api_base}")
                        log_debug(f"NOTE DEBUG: Full URL: {ui_api_base}/executions/note")
                        log_debug(f"NOTE DEBUG: Payload: {payload}")
                        log_debug(f"NOTE DEBUG: Headers: {headers}")
                    
                    async with aiohttp.ClientSession(timeout=timeout) as session:
                        async with session.post(
                            f"{ui_api_base}/executions/note",
                            json=payload,
                            headers=headers
                        ) as response:
                            if self.dev_mode:
                                from brain_sdk.logger import log_debug
                                response_text = await response.text()
                                log_debug(f"NOTE DEBUG: Response status: {response.status}")
                                log_debug(f"NOTE DEBUG: Response text: {response_text}")
                                if response.status == 200:
                                    log_debug(f"✅ Note successfully sent to {ui_api_base}/executions/note")
                                else:
                                    log_debug(f"❌ Note failed with status {response.status}: {response_text}")
                except ImportError:
                    # Fallback to requests if aiohttp not available
                    import requests
                    try:
                        # Use UI API base URL to match where frontend fetches notes from
                        ui_api_base = self.client.api_base.replace("/api/v1", "/api/ui/v1")
                        
                        if self.dev_mode:
                            from brain_sdk.logger import log_debug
                            log_debug(f"NOTE DEBUG (requests): Original api_base: {self.client.api_base}")
                            log_debug(f"NOTE DEBUG (requests): UI api_base: {ui_api_base}")
                            log_debug(f"NOTE DEBUG (requests): Full URL: {ui_api_base}/executions/note")
                        
                        response = requests.post(
                            f"{ui_api_base}/executions/note",
                            json=payload,
                            headers=headers,
                            timeout=5.0
                        )
                        if self.dev_mode:
                            from brain_sdk.logger import log_debug
                            log_debug(f"NOTE DEBUG (requests): Response status: {response.status_code}")
                            log_debug(f"NOTE DEBUG (requests): Response text: {response.text}")
                            if response.status_code == 200:
                                log_debug(f"✅ Note successfully sent to {ui_api_base}/executions/note")
                            else:
                                log_debug(f"❌ Note failed with status {response.status_code}: {response.text}")
                    except Exception as e:
                        if self.dev_mode:
                            from brain_sdk.logger import log_debug
                            log_debug(f"Note request failed: {type(e).__name__}: {e}")
                            
            except Exception as e:
                # Silently handle errors to avoid interrupting main workflow
                if self.dev_mode:
                    from brain_sdk.logger import log_debug
                    log_debug(f"Failed to send note: {type(e).__name__}: {e}")
        
        # Create task without awaiting (fire-and-forget)
        try:
            # Try to get current event loop
            loop = asyncio.get_event_loop()
            if loop.is_running():
                # If we're in an async context, create a task
                loop.create_task(_send_note())
            else:
                # If no loop is running, run in a new thread
                import threading
                thread = threading.Thread(target=lambda: asyncio.run(_send_note()))
                thread.daemon = True
                thread.start()
        except RuntimeError:
            # No event loop available, run in a new thread
            import threading
            thread = threading.Thread(target=lambda: asyncio.run(_send_note()))
            thread.daemon = True
            thread.start()

    def _get_current_execution_context(self) -> ExecutionContext:
        """
        Get the current execution context, creating a new one if none exists.
        
        This method checks thread-local context first (most reliable) and falls back
        to agent-level context for proper parent-child relationship tracking.

        Returns:
            ExecutionContext: Current or new execution context
        """
        # Check thread-local context first (most reliable)
        from brain_sdk.execution_context import get_current_context
        thread_local_context = get_current_context()
        
        if thread_local_context:
            # Sync agent-level with thread-local
            self._current_execution_context = thread_local_context
            return thread_local_context
        
        # Fall back to agent-level context
        if self._current_execution_context:
            return self._current_execution_context
        
        # Create new context if none exists and cache it
        new_context = ExecutionContext.create_new(
            agent_node_id=self.node_id, workflow_name=f"{self.node_id}_workflow"
        )
        self._current_execution_context = new_context
        return new_context

    def _get_target_return_type(self, target: str) -> Optional[Type]:
        """
        Get the return type for a target reasoner.
        
        Args:
            target: Target in format 'node_id.reasoner_name'
            
        Returns:
            The return type class if found, None otherwise
        """
        function_name = target.split(".", 1)[-1] if "." in target else target

        # Prefer the dedicated mapping populated during decorator registration
        return_type_map = getattr(self, "_reasoner_return_types", None)
        if return_type_map:
            return_type = return_type_map.get(function_name)
            if return_type is not None:
                return return_type

        # Fallback for legacy metadata that may still include return_type directly
        for reasoner in self.reasoners:
            if reasoner.get("id") == function_name:
                stored_type = reasoner.get("return_type")
                if stored_type is not None:
                    return stored_type

        return None

    def _convert_response_to_schema(self, response_data: Any, return_type: Type) -> Any:
        """
        Convert JSON response data back to the original Pydantic schema.
        
        Args:
            response_data: The JSON response data (usually a dict)
            return_type: The target return type to convert to
            
        Returns:
            The converted response in the original schema format
        """
        try:
            # Import here to avoid circular imports
            from pydantic import BaseModel
            
            # If return_type is a Pydantic model, convert the dict to the model
            if (isinstance(return_type, type) and
                issubclass(return_type, BaseModel) and
                isinstance(response_data, dict)):
                
                return return_type(**response_data)
            
            # If it's not a Pydantic model or not a dict, return as-is
            return response_data
            
        except Exception as e:
            # If conversion fails, log the error and return the original data
            if self.dev_mode:
                log_error(f"Schema conversion failed for {return_type}: {e}")
                log_debug(f"Schema conversion response data: {response_data}")
            return response_data

    @classmethod
    def get_current(cls) -> Optional["Agent"]:
        """
        Get the current agent instance.

        This method is used by auto-generated MCP skills to access the current
        agent's execution context. It uses a thread-local storage pattern to
        track the current agent instance.

        Returns:
            Current Agent instance or None if no agent is active
        """
        # For now, we'll use a simple class variable approach
        # In a more complex implementation, this could use thread-local storage
        return getattr(cls, "_current_agent", None)

    def _set_as_current(self) -> None:
        """Set this agent as the current agent instance."""
        Agent._current_agent = self
        set_current_agent(self)

    def _clear_current(self) -> None:
        """Clear the current agent instance."""
        if hasattr(Agent, "_current_agent"):
            delattr(Agent, "_current_agent")
        # Also clear from thread-local storage
        clear_current_agent()

    def _setup_signal_handlers(self) -> None:  # pragma: no cover - requires signal integration
        """Delegate to server handler for signal setup"""
        return self.server_handler.setup_signal_handlers()

    def _signal_handler(self, signum: int, frame) -> None:  # pragma: no cover - runtime signal handling
        """Delegate to server handler for signal handling"""
        return self.server_handler.signal_handler(signum, frame)

    def __del__(self) -> None:  # pragma: no cover - destructor best effort
        """
        Destructor to ensure cleanup happens even if signals are missed.

        This serves as a fallback cleanup mechanism.
        """
        try:
            # Cleanup async execution manager if it exists
            if hasattr(self, "_async_execution_manager") and self._async_execution_manager:
                try:
                    # Try to cleanup async resources in a new event loop
                    import asyncio
                    asyncio.run(self._cleanup_async_resources())
                except Exception:
                    # Ignore async cleanup errors in destructor
                    pass
            
            # Only attempt cleanup if we have an MCP handler
            if hasattr(self, "mcp_handler") and self.mcp_handler:
                self.mcp_handler._cleanup_mcp_servers()
            # Clear agent from thread-local storage as final cleanup
            clear_current_agent()
        except Exception:
            # Ignore errors in destructor to prevent warnings during garbage collection
            pass

    def serve(  # pragma: no cover - requires full server runtime integration
        self,
        port: Optional[int] = None,
        host: str = "0.0.0.0",
        dev: bool = False,
        heartbeat_interval: int = 2,
        auto_port: bool = False,
        **kwargs,
    ):
        """
        Start the agent node server with intelligent port management and Brain integration.

        This method launches the agent as a FastAPI server that can receive reasoner and skill
        requests from other agents via the Brain execution gateway. It handles automatic
        registration with the Brain server, heartbeat management, and graceful shutdown.
        
        The server provides:
        - RESTful endpoints for all registered reasoners and skills
        - Health check endpoints for monitoring
        - MCP server status and management endpoints
        - Automatic Brain server registration and heartbeat
        - Graceful shutdown with proper cleanup
        
        Args:
            port (int, optional): The port on which the agent server will listen.
                                If None, uses the port from agent configuration or auto-discovers.
                                Common ports: 8000, 8001, 8080, etc.
            host (str): The host address for the agent server. Defaults to "0.0.0.0".
                       Use "127.0.0.1" for localhost-only access.
            dev (bool): If True, enables development mode features including:
                       - Enhanced logging and debug output
                       - Auto-reload on code changes (if supported)
                       - Detailed error messages
                       - MCP server debugging information
            heartbeat_interval (int): The interval in seconds for sending heartbeats to the Brain server.
                                    Defaults to 2 seconds. Lower values provide faster failure detection
                                    but increase network overhead.
            auto_port (bool): If True, automatically find an available port starting from the
                            specified port (or default). Useful for development environments
                            where multiple agents may be running.
            **kwargs: Additional keyword arguments to pass to `uvicorn.run`, such as:
                     - reload: Enable auto-reload on code changes
                     - workers: Number of worker processes
                     - log_level: Logging level ("debug", "info", "warning", "error")
                     - ssl_keyfile: Path to SSL key file for HTTPS
                     - ssl_certfile: Path to SSL certificate file for HTTPS
        
        Example:
            ```python
            # Basic agent server
            app = Agent("my_agent")
            
            @app.reasoner()
            async def process_data(data: str) -> dict:
                '''Process incoming data and return results.'''
                return {"processed": data.upper(), "length": len(data)}
            
            @app.skill()
            def get_status() -> dict:
                '''Get current agent status.'''
                return {"status": "active", "timestamp": datetime.now().isoformat()}
            
            # Start server on default port
            app.serve()
            
            # Start server with custom configuration
            app.serve(
                port=8080,
                host="127.0.0.1",
                dev=True,
                heartbeat_interval=5,
                auto_port=True,
                reload=True,
                log_level="debug"
            )
            
            # Production server with SSL
            app.serve(
                port=443,
                host="0.0.0.0",
                ssl_keyfile="/path/to/key.pem",
                ssl_certfile="/path/to/cert.pem",
                workers=4
            )
            ```
            
        Server Endpoints:
            Once running, the agent exposes these endpoints:
            - `POST /reasoners/{reasoner_name}`: Execute reasoner functions
            - `POST /skills/{skill_name}`: Execute skill functions
            - `GET /health`: Health check endpoint
            - `GET /mcp/status`: MCP server status and management
            - `GET /docs`: Interactive API documentation (Swagger UI)
            - `GET /redoc`: Alternative API documentation
            
        Integration with Brain:
            - Automatically registers with Brain server on startup
            - Sends periodic heartbeats to maintain connection
            - Receives execution requests via Brain's routing system
            - Participates in workflow tracking and DAG building
            - Handles cross-agent communication seamlessly
            
        Lifecycle:
            1. Server initialization and route setup
            2. MCP server startup (if configured)
            3. Brain server registration
            4. Heartbeat loop starts
            5. Ready to receive requests
            6. Graceful shutdown on SIGINT/SIGTERM
            7. MCP server cleanup
            8. Brain server deregistration
            
        Note:
            - The server runs indefinitely until interrupted (Ctrl+C)
            - All registered reasoners and skills become available as REST endpoints
            - Memory and execution context are automatically managed
            - MCP servers are started and managed automatically
            - Use `dev=True` for development, `dev=False` for production
        """
        return self.server_handler.serve(
            port=port,
            host=host,
            dev=dev,
            heartbeat_interval=heartbeat_interval,
            auto_port=auto_port,
            **kwargs,
        )
