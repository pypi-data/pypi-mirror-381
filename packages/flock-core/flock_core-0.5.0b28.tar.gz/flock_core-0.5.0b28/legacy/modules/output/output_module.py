"""Output formatting and display functionality for agents."""

from typing import TYPE_CHECKING, Any

from pydantic import Field

from flock.core.context.context_vars import FLOCK_BATCH_SILENT_MODE
from flock.core.flock_registry import flock_component

if TYPE_CHECKING:
    from flock.core import FlockAgent

from flock.core.context.context import FlockContext
from flock.core.flock_module import FlockModule, FlockModuleConfig
from flock.core.logging.formatters.themed_formatter import (
    ThemedAgentResultFormatter,
)
from flock.core.logging.formatters.themes import OutputTheme
from flock.core.logging.logging import get_logger

# from flock.core.logging.formatters.themes import OutputTheme
# from flock.core.logging.logging import get_logger
# from flock.core.serialization.json_encoder import FlockJSONEncoder

logger = get_logger("module.output")


class OutputModuleConfig(FlockModuleConfig):
    """Configuration for output formatting and display."""

    theme: OutputTheme = Field(
        default=OutputTheme.afterglow, description="Theme for output formatting"
    )
    render_table: bool = Field(
        default=False, description="Whether to render output as a table"
    )
    max_length: int = Field(
        default=1000, description="Maximum length for displayed output"
    )
    truncate_long_values: bool = Field(
        default=True, description="Whether to truncate long values in display"
    )
    show_metadata: bool = Field(
        default=True, description="Whether to show metadata like timestamps"
    )
    format_code_blocks: bool = Field(
        default=True,
        description="Whether to apply syntax highlighting to code blocks",
    )
    custom_formatters: dict[str, str] = Field(
        default_factory=dict,
        description="Custom formatters for specific output types",
    )
    no_output: bool = Field(
        default=False,
        description="Whether to suppress output",
    )
    print_context: bool = Field(
        default=False,
        description="Whether to print the context",
    )


@flock_component(config_class=OutputModuleConfig)
class OutputModule(FlockModule):
    """Module that handles output formatting and display."""

    name: str = "output"
    config: OutputModuleConfig = Field(
        default_factory=OutputModuleConfig, description="Output configuration"
    )

    def __init__(self, name: str, config: OutputModuleConfig):
        super().__init__(name=name, config=config)
        self._formatter = ThemedAgentResultFormatter(
            theme=self.config.theme,
            max_length=self.config.max_length,
            render_table=self.config.render_table,
        )

    def _format_value(self, value: Any, key: str) -> str:
        """Format a single value based on its type and configuration."""
        # Check for custom formatter
        if key in self.config.custom_formatters:
            formatter_name = self.config.custom_formatters[key]
            if hasattr(self, f"_format_{formatter_name}"):
                return getattr(self, f"_format_{formatter_name}")(value)

        # Default formatting based on type
        if isinstance(value, dict):
            return self._format_dict(value)
        elif isinstance(value, list):
            return self._format_list(value)
        elif isinstance(value, str) and self.config.format_code_blocks:
            return self._format_potential_code(value)
        else:
            return str(value)

    def _format_dict(self, d: dict[str, Any], indent: int = 0) -> str:
        """Format a dictionary with proper indentation."""
        lines = []
        for k, v in d.items():
            formatted_value = self._format_value(v, k)
            if (
                self.config.truncate_long_values
                and len(formatted_value) > self.config.max_length
            ):
                formatted_value = (
                    formatted_value[: self.config.max_length] + "..."
                )
            lines.append(f"{'  ' * indent}{k}: {formatted_value}")
        return "\n".join(lines)

    def _format_list(self, lst: list[Any]) -> str:
        """Format a list with proper indentation."""
        return "\n".join(f"- {self._format_value(item, '')}" for item in lst)

    def _format_potential_code(self, text: str) -> str:
        """Format text that might contain code blocks."""
        import re

        def replace_code_block(match):
            code = match.group(2)
            lang = match.group(1) if match.group(1) else ""
            # Here you could add syntax highlighting
            return f"```{lang}\n{code}\n```"

        # Replace code blocks with formatted versions
        text = re.sub(
            r"```(\w+)?\n(.*?)\n```", replace_code_block, text, flags=re.DOTALL
        )
        return text

    async def on_post_evaluate(
        self,
        agent: "FlockAgent",
        inputs: dict[str, Any],
        context: FlockContext | None = None,
        result: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Format and display the output."""
        logger.debug("Formatting and displaying output")

        # Determine if output should be suppressed
        is_silent = self.config.no_output or (
            context and context.get_variable(FLOCK_BATCH_SILENT_MODE, False)
        )

        if is_silent:
            logger.debug("Output suppressed (config or batch silent mode).")
            return result  # Skip console output

        logger.debug("Formatting and displaying output to console.")

        if self.config.print_context and context:
            # Add context snapshot if requested (be careful with large contexts)
            try:
                # Create a copy or select relevant parts to avoid modifying original result dict directly
                display_result = result.copy()
                display_result["context_snapshot"] = (
                    context.to_dict()
                )  # Potential performance hit
            except Exception:
                display_result = result.copy()
                display_result["context_snapshot"] = (
                    "[Error serializing context]"
                )
            result_to_display = display_result
        else:
            result_to_display = result

        if not hasattr(self, "_formatter") or self._formatter is None:
            self._formatter = ThemedAgentResultFormatter(
                theme=self.config.theme,
                max_length=self.config.max_length,
                render_table=self.config.render_table,
                wait_for_input=self.config.wait_for_input,
            )
        model = agent.model if agent.model else context.get_variable("model")
        self._formatter.display_result(result_to_display, agent.name + " - " + model)

        return result  # Return the original, unmodified result

    def update_theme(self, new_theme: OutputTheme) -> None:
        """Update the output theme."""
        self.config.theme = new_theme
        self._formatter = ThemedAgentResultFormatter(
            theme=self.config.theme,
            max_length=self.config.max_length,
            render_table=self.config.render_table,
            wait_for_input=self.config.wait_for_input,
            write_to_file=self.config.write_to_file,
        )

    def add_custom_formatter(self, key: str, formatter_name: str) -> None:
        """Add a custom formatter for a specific output key."""
        self.config.custom_formatters[key] = formatter_name
