"""Factory for creating pre-configured Flock agents.

Deprecated: Prefer explicit `DefaultAgent` class for new code. This factory
remains as a thin adapter to ease migration and preserve backward compatibility.
"""

import os
import warnings
from collections.abc import Callable
from pathlib import Path
from typing import Any, Literal

import httpx
from pydantic import AnyUrl, BaseModel, ConfigDict, Field, FileUrl

from flock.components.utility.metrics_utility_component import (
    MetricsUtilityComponent,
    MetricsUtilityConfig,
)
from flock.core.agent.default_agent import DefaultAgent

# New unified components imported locally to avoid circular imports
from flock.core.config.scheduled_agent_config import ScheduledAgentConfig
from flock.core.flock_agent import DynamicStr, FlockAgent
from flock.core.logging.formatters.themes import OutputTheme
from flock.core.logging.logging import get_logger
from flock.core.mcp.flock_mcp_server import FlockMCPServer
from flock.core.mcp.mcp_config import (
    FlockMCPCachingConfiguration,
    FlockMCPCallbackConfiguration,
    FlockMCPFeatureConfiguration,
)
from flock.core.mcp.types.types import (
    FlockListRootsMCPCallback,
    FlockLoggingMCPCallback,
    FlockMessageHandlerMCPCallback,
    FlockSamplingMCPCallback,
    MCPRoot,
    SseServerParameters,
    StdioServerParameters,
    StreamableHttpServerParameters,
    WebsocketServerParameters,
)
from flock.mcp.servers.sse.flock_sse_server import (
    FlockSSEConfig,
    FlockSSEConnectionConfig,
    FlockSSEServer,
)
from flock.mcp.servers.stdio.flock_stdio_server import (
    FlockMCPStdioServer,
    FlockStdioConfig,
    FlockStdioConnectionConfig,
)
from flock.mcp.servers.streamable_http.flock_streamable_http_server import (
    FlockStreamableHttpConfig,
    FlockStreamableHttpConnectionConfig,
    FlockStreamableHttpServer,
)
from flock.mcp.servers.websockets.flock_websocket_server import (
    FlockWSConfig,
    FlockWSConnectionConfig,
    FlockWSServer,
)
from flock.workflow.temporal_config import TemporalActivityConfig

LoggingLevel = Literal[
    "debug",
    "info",
    "notice",
    "warning",
    "error",
    "critical",
    "alert",
    "emergency",
]


class FlockFactory:
    """Factory for creating pre-configured Flock agents and pre-configured Flock MCPServers with common module setups."""

    # Classes for type-hints.
    class StdioParams(BaseModel):
        """Factory-Params for Stdio-Servers."""

        command: str = Field(
            ...,
            description="Command for starting the local script. (e.g. 'uvx', 'bun', 'npx', 'bunx', etc.)",
        )

        args: list[str] = Field(
            ...,
            description="Arguments for starting the local script. (e.g. ['run', './mcp-server.py'])",
        )

        env: dict[str, Any] | None = Field(
            default=None,
            description="Environment variables to pass to the server. (e.g. {'GOOGLE_API_KEY': 'MY_SUPER_SECRET_API_KEY'})",
        )

        cwd: str | Path | None = Field(
            default_factory=os.getcwd,
            description="The working directory to start the script in.",
        )

        encoding: str = Field(
            default="utf-8",
            description="The char-encoding to use when talking to a stdio server. (e.g. 'utf-8', 'ascii', etc.)",
        )

        encoding_error_handler: Literal["strict", "ignore", "replace"] = Field(
            default="strict",
            description="The text encoding error handler. See https://docs.python.org/3/library/codecs.html#codec-base-classes for explanations of possible values",
        )

    class StreamableHttpParams(BaseModel):
        """Factory-Params for Streamable Http Servers."""

        url: str | AnyUrl = Field(..., description="Url the server listens at.")

        headers: dict[str, Any] | None = Field(
            default=None,
            description="Additional Headers to pass to the client.",
        )

        auth: httpx.Auth | None = Field(
            default=None, description="Httpx Auth Schema."
        )

        timeout_seconds: float | int = Field(
            default=5, description="Http Timeout in Seconds"
        )

        sse_read_timeout_seconds: float | int = Field(
            default=60 * 5,
            description="How many seconds to wait for server-sent events until closing the connection.",
        )

        terminate_on_close: bool = Field(
            default=True,
            description="Whether or not to terminate the underlying connection on close.",
        )

        model_config = ConfigDict(
            arbitrary_types_allowed=True,
            extra="allow",
        )

    class SSEParams(BaseModel):
        """Factory-Params for SSE-Servers."""

        url: str | AnyUrl = Field(
            ...,
            description="Url the server listens at. (e.g. https://my-mcp-server.io/sse)",
        )

        headers: dict[str, Any] | None = Field(
            default=None,
            description="Additional Headers to pass to the client.",
        )

        timeout_seconds: float | int = Field(
            default=5, description="Http Timeout in Seconds."
        )

        sse_read_timeout_seconds: float | int = Field(
            default=60 * 5,
            description="How many seconds to wait for server-sent events until closing the connection. (connections will be automatically re-established.)",
        )

        auth: httpx.Auth | None = Field(
            default=None, description="Httpx Auth Scheme."
        )

        model_config = ConfigDict(
            arbitrary_types_allowed=True,
            extra="allow",
        )

    class WebsocketParams(BaseModel):
        """Factory-Params for Websocket Servers."""

        url: str | AnyUrl = Field(
            ...,
            description="The url the server listens at. (e.g. ws://my-mcp-server.io/messages)",
        )

    @staticmethod
    def create_mcp_server(
        name: str,
        connection_params: StreamableHttpParams
        | SSEParams
        | StdioParams
        | WebsocketParams,
        max_retries: int = 3,
        mount_points: list[str | MCPRoot] | None = None,
        timeout_seconds: int | float = 10,
        server_logging_level: LoggingLevel = "error",
        enable_roots_feature: bool = False,
        enable_tools_feature: bool = False,
        enable_sampling_feature: bool = False,
        enable_prompts_feature: bool = False,
        sampling_callback: FlockSamplingMCPCallback | None = None,
        list_roots_callback: FlockListRootsMCPCallback | None = None,
        logging_callback: FlockLoggingMCPCallback | None = None,
        message_handler: FlockMessageHandlerMCPCallback | None = None,
        tool_cache_size: float = 100,
        tool_cache_ttl: float = 60,
        resource_contents_cache_size=10,
        resource_contents_cache_ttl=60 * 5,
        resource_list_cache_size=100,
        resource_list_cache_ttl=100,
        tool_result_cache_size=100,
        tool_result_cache_ttl=100,
        description: str | Callable[..., str] | None = None,
        alert_latency_threshold_ms: int = 30000,
        tool_whitelist: list[str] | None = None,
        allow_all_tools: bool = True,
    ) -> FlockMCPServer:
        """Create a default MCP Server with common modules.

        Allows for creating one of the three default-implementations provided
        by Flock:
        - SSE-Server (specify "sse" in type)
        - Stdio-Server (specify "stdio" in type)
        - Websockets-Server (specifiy "websockets" in type)

        Args:
            name: Unique identifier for the MCP server
            connection_params: Connection configuration (StdioParams, SSEParams, etc.)
            tool_whitelist: List of tool names to allow from this server. If provided,
                          only tools with these names will be available. Used with
                          allow_all_tools=False for strict filtering. Agent-level
                          filtering is generally preferred over server-level filtering.
            allow_all_tools: Whether to allow all tools from the server. When True
                           (default), all tools are available. When False, only tools
                           in tool_whitelist (if provided) are available.
            Other args: Various configuration options for caching, callbacks, etc.

        Returns:
            FlockMCPServer: Configured MCP server instance

        Note:
            For security and flexibility, prefer using agent-level tool_whitelist
            over server-level filtering. This allows different agents to access
            different tool subsets from the same server.
        """
        # infer server type from the pydantic model class
        if isinstance(connection_params, FlockFactory.StdioParams):
            server_kind = "stdio"
            concrete_server_cls = FlockMCPStdioServer
        if isinstance(connection_params, FlockFactory.SSEParams):
            server_kind = "sse"
            concrete_server_cls = FlockSSEServer
        if isinstance(connection_params, FlockFactory.WebsocketParams):
            server_kind = "websockets"
            concrete_server_cls = FlockWSServer
        if isinstance(connection_params, FlockFactory.StreamableHttpParams):
            server_kind = "streamable_http"
            concrete_server_cls = FlockStreamableHttpServer

        # convert mount points.
        mounts: list[MCPRoot] = []
        if mount_points:
            for item in mount_points:
                if isinstance(item, MCPRoot):
                    mounts.append(item)
                elif isinstance(item, str):
                    try:
                        conv = MCPRoot(uri=FileUrl(url=item))
                        mounts.append(conv)
                    except Exception:
                        continue  # ignore
                else:
                    continue  # ignore

        # build generic configs
        feature_config = FlockMCPFeatureConfiguration(
            roots_enabled=enable_roots_feature,
            tools_enabled=enable_tools_feature,
            prompts_enabled=enable_prompts_feature,
            sampling_enabled=enable_sampling_feature,
            tool_whitelist=tool_whitelist,
        )
        callback_config = FlockMCPCallbackConfiguration(
            sampling_callback=sampling_callback,
            list_roots_callback=list_roots_callback,
            logging_callback=logging_callback,
            message_handler=message_handler,
        )
        caching_config = FlockMCPCachingConfiguration(
            tool_cache_max_size=tool_cache_size,
            tool_cache_max_ttl=tool_cache_ttl,
            resource_contents_cache_max_size=resource_contents_cache_size,
            resource_contents_cache_max_ttl=resource_contents_cache_ttl,
            resource_list_cache_max_size=resource_list_cache_size,
            resource_list_cache_max_ttl=resource_list_cache_ttl,
            tool_result_cache_max_size=tool_result_cache_size,
            tool_result_cache_max_ttl=tool_result_cache_ttl,
        )
        connection_config = None
        server_config: (
            FlockStdioConfig | FlockSSEConfig | FlockWSConfig | None
        ) = None

        # Instantiate correct server + config
        if server_kind == "stdio":
            # build stdio config
            connection_config = FlockStdioConnectionConfig(
                max_retries=max_retries,
                connection_parameters=StdioServerParameters(
                    command=connection_params.command,
                    args=connection_params.args,
                    env=connection_params.env,
                    encoding=connection_params.encoding,
                    encoding_error_handler=connection_params.encoding_error_handler,
                    cwd=connection_params.cwd,
                ),
                mount_points=mounts,
                read_timeout_seconds=timeout_seconds,
                server_logging_level=server_logging_level,
            )
            server_config = FlockStdioConfig(
                name=name,
                connection_config=connection_config,
                feature_config=feature_config,
                caching_config=caching_config,
                callback_config=callback_config,
            )
        elif server_kind == "streamable_http":
            # build streamable http config
            connection_config = FlockStreamableHttpConnectionConfig(
                max_retries=max_retries,
                connection_parameters=StreamableHttpServerParameters(
                    url=connection_params.url,
                    headers=connection_params.headers,
                    auth=connection_params.auth,
                    timeout=connection_params.timeout_seconds,
                    sse_read_timeout=connection_params.sse_read_timeout_seconds,
                    terminate_on_close=connection_params.terminate_on_close,
                ),
                mount_points=mounts,
                server_logging_level=server_logging_level,
            )

            server_config = FlockStreamableHttpConfig(
                name=name,
                connection_config=connection_config,
                feature_config=feature_config,
                caching_config=caching_config,
                callback_config=callback_config,
                allow_all_tools=allow_all_tools,
            )

        elif server_kind == "sse":
            # build sse config
            connection_config = FlockSSEConnectionConfig(
                max_retries=max_retries,
                connection_parameters=SseServerParameters(
                    url=connection_params.url,
                    auth=connection_params.auth,
                    headers=connection_params.headers,
                    timeout=connection_params.timeout_seconds,
                    sse_read_timeout=connection_params.sse_read_timeout_seconds,
                ),
                mount_points=mounts,
                server_logging_level=server_logging_level,
            )

            server_config = FlockSSEConfig(
                name=name,
                connection_config=connection_config,
                feature_config=feature_config,
                caching_config=caching_config,
                callback_config=callback_config,
                allow_all_tools=allow_all_tools,
            )

        elif server_kind == "websockets":
            # build websocket config
            connection_config = FlockWSConnectionConfig(
                max_retries=max_retries,
                connection_parameters=WebsocketServerParameters(
                    url=connection_params.url,
                ),
                mount_points=mounts,
                server_logging_level=server_logging_level,
            )

            server_config = FlockWSConfig(
                name=name,
                connection_config=connection_config,
                feature_config=feature_config,
                caching_config=caching_config,
                callback_config=callback_config,
                allow_all_tools=allow_all_tools,
            )

        else:
            raise ValueError(
                f"Unsupported connection_params type: {type(connection_params)}"
            )

        if not server_config:
            raise ValueError(
                "Unable to create server configuration for passed params."
            )

        server = concrete_server_cls(config=server_config)

        metrics_component_config = MetricsUtilityConfig(
            latency_threshold_ms=alert_latency_threshold_ms
        )

        metrics_component = MetricsUtilityComponent("metrics", config=metrics_component_config)

        server.add_component(metrics_component)

        return server

    @staticmethod
    def create_default_agent(
        name: str,
        description: DynamicStr| None = None,
        model: str | Callable[..., str] | None = None,
        input: DynamicStr = None,
        output: DynamicStr = None,
        tools: list[Callable[..., Any] | Any] | None = None,
        servers: list[str | FlockMCPServer] | None = None,
        use_cache: bool = True,
        enable_rich_tables: bool = False,
        output_theme: OutputTheme = OutputTheme.abernathy,
        wait_for_input: bool = False,
        temperature: float = 1.0,
        max_tokens: int = 8192,
        max_tool_calls: int = 10,
        max_retries: int = 3,
        alert_latency_threshold_ms: int = 30000,
        no_output: bool = False,
        print_context: bool = False,
        write_to_file: bool = False,
        stream: bool = False,
        include_thought_process: bool = False,
        include_reasoning: bool = False,
        next_agent: DynamicStr | None = None,
        temporal_activity_config: TemporalActivityConfig | None = None,
        # Feedback parameters
        enable_feedback: bool = False,
        feedback_storage_type: Literal["sqlite", "azure"] = "sqlite",
        feedback_max_items: int = 5,
        feedback_timeframe_days: int = 30,
        feedback_input_key: str = "feedback_context",
        feedback_include_expected_responses: bool = True,
        feedback_include_actual_responses: bool = False,
        feedback_filter_keywords: list[str] | None = None,
        feedback_exclude_keywords: list[str] | None = None,
        feedback_sqlite_db_path: str = "./flock_feedback.db",
        feedback_azure_connection_string: str | None = None,
        feedback_azure_table_name: str = "flockfeedback",
        # Example parameters
        enable_examples: bool = False,
        example_storage_type: Literal["sqlite", "azure"] = "sqlite",
        example_max_examples: int = 5,
        example_timeframe_days: int = 30,
        example_input_key: str = "examples_context",
        example_filter_keywords: list[str] | None = None,
        example_exclude_keywords: list[str] | None = None,
        example_sqlite_db_path: str = "./flock_examples.db",
        example_azure_connection_string: str | None = None,
        example_azure_table_name: str = "flockexamples",
    ) -> FlockAgent:
        """Create a default FlockAgent.

        Deprecated: Use `DefaultAgent(...)` instead. This method now delegates to
        `DefaultAgent` and emits an optional one-time deprecation warning if the
        environment variable `FLOCK_WARN_FACTORY_DEPRECATION` is truthy (default).
        """
        _maybe_warn_factory_deprecation()

        # Configure feedback if enabled
        feedback_config = None
        if enable_feedback:
            from flock.components.utility.feedback_utility_component import FeedbackUtilityConfig
            feedback_config = FeedbackUtilityConfig(
                storage_type=feedback_storage_type,
                max_feedback_items=feedback_max_items,
                feedback_timeframe_days=feedback_timeframe_days,
                feedback_input_key=feedback_input_key,
                include_expected_responses=feedback_include_expected_responses,
                include_actual_responses=feedback_include_actual_responses,
                feedback_filter_keywords=feedback_filter_keywords or [],
                feedback_exclude_keywords=feedback_exclude_keywords or [],
                sqlite_db_path=feedback_sqlite_db_path,
                azure_connection_string=feedback_azure_connection_string,
                azure_table_name=feedback_azure_table_name,
            )
        
        # Configure examples if enabled
        example_config = None
        if enable_examples:
            from flock.components.utility.example_utility_component import ExampleUtilityConfig
            example_config = ExampleUtilityConfig(
                storage_type=example_storage_type,
                max_examples=example_max_examples,
                example_timeframe_days=example_timeframe_days,
                example_input_key=example_input_key,
                example_filter_keywords=example_filter_keywords or [],
                example_exclude_keywords=example_exclude_keywords or [],
                sqlite_db_path=example_sqlite_db_path,
                azure_connection_string=example_azure_connection_string,
                azure_table_name=example_azure_table_name,
            )

        return DefaultAgent(
            name=name,
            description=description,
            model=model,
            input=input,
            output=output,
            tools=tools,
            servers=servers,
            use_cache=use_cache,
            temperature=temperature,
            max_tokens=max_tokens,
            max_tool_calls=max_tool_calls,
            max_retries=max_retries,
            stream=stream,
            include_thought_process=include_thought_process,
            include_reasoning=include_reasoning,
            enable_rich_tables=enable_rich_tables,
            output_theme=output_theme,
            no_output=no_output,
            print_context=print_context,
            write_to_file=write_to_file,
            wait_for_input=wait_for_input,
            alert_latency_threshold_ms=alert_latency_threshold_ms,
            next_agent=next_agent,
            temporal_activity_config=temporal_activity_config,
            enable_feedback=enable_feedback,
            feedback_config=feedback_config,
            enable_examples=enable_examples,
            example_config=example_config,
        )

    @staticmethod
    def create_scheduled_agent(
        name: str,
        schedule_expression: str,  # e.g., "every 1h", "0 0 * * *"
        description: DynamicStr | None = None,
        model: str | None = None,
        output: DynamicStr | None = None,  # Input might be implicit or none
        tools: list[Callable[..., Any] | Any] | None = None,
        servers: list[str | FlockMCPServer] | None = None,
        use_cache: bool = False,  # Whether to cache results
        temperature: float = 0.7,  # Temperature for model responses
        # ... other common agent params from create_default_agent ...
        next_agent: DynamicStr | None = None,
        temporal_activity_config: TemporalActivityConfig
        | None = None,  # If you want scheduled tasks to be Temporal activities
        **kwargs,  # Forward other standard agent params
    ) -> FlockAgent:
        """Creates a FlockAgent configured to run on a schedule."""
        agent_config = ScheduledAgentConfig(  # Use the new config type
            schedule_expression=schedule_expression,
            enabled=True,
            initial_run=True,
            max_runs=0,
            **kwargs,
        )

        agent = DefaultAgent(
            name=name,
            description=description,
            model=model,
            input="trigger_time: str | Time of scheduled execution",
            output=output,
            tools=tools,
            servers=servers,
            temporal_activity_config=temporal_activity_config,
            use_cache=use_cache,
            temperature=temperature,
            next_agent=next_agent,
            **kwargs,
        )
        agent.config = agent_config  # Assign the scheduled agent config

        return agent


# ---- one-time deprecation warning helper ----
_FACTORY_DEPRECATION_WARNED = False
_factory_logger = get_logger("core.factory")


def _maybe_warn_factory_deprecation() -> None:  # pragma: no cover - side-effect
    global _FACTORY_DEPRECATION_WARNED
    if _FACTORY_DEPRECATION_WARNED:
        return
    flag = os.getenv("FLOCK_WARN_FACTORY_DEPRECATION", "1").strip()
    enabled = flag not in {"0", "false", "False", "off", "OFF"}
    if not enabled:
        _FACTORY_DEPRECATION_WARNED = True
        return
    msg = (
        "FlockFactory.create_default_agent is deprecated and will be removed in a future release. "
        "Please use DefaultAgent(...) instead. Set FLOCK_WARN_FACTORY_DEPRECATION=0 to disable this notice."
    )
    # Log and emit a warnings.warn once
    try:
        _factory_logger.warning(msg)
    except Exception:
        pass
    warnings.warn(msg, DeprecationWarning, stacklevel=2)
    _FACTORY_DEPRECATION_WARNED = True
