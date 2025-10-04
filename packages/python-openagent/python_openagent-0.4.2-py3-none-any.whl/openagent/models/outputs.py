from typing import Any

from openagent.models.execution import (
    BaseExecutionOutput,
)


class WebSearchOutput(BaseExecutionOutput):
    """Output model for web search operations."""

    search_results: list[dict[str, Any]] = []
    query: str = ""
    results_count: int = 0


class PythonRuntimeOutput(BaseExecutionOutput):
    """Output model for Python runtime operations."""

    stdout: str = ""
    stderr: str = ""
    return_code: int = 0
    variables: dict[str, Any] = {}


class PowerpointAgentOutput(BaseExecutionOutput):
    """Output model for PowerPoint agent operations."""

    file_path: str = ""
    slide_count: int = 0
    content_summary: str = ""


class GeneralAgentOutput(BaseExecutionOutput):
    """Output model for general agent operations."""

    response: str = ""
    confidence: float = 0.0
    reasoning: str = ""


class EmailAgentOutput(BaseExecutionOutput):
    """Output model for email agent operations."""

    sent_count: int = 0
    failed_addresses: list[str] = []
    message_id: str = ""


class FileReaderAgentOutput(BaseExecutionOutput):
    """Output model for file reading operations."""

    file_content: str = ""
    file_size: int = 0
    file_type: str = ""
    metadata: dict[str, Any] = {}
