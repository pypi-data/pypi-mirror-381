from datetime import datetime as dt
from textwrap import dedent

from openagent.models.sentinel import ExecutionEvalulationRequest
from openagent.prompts.base import BasePrompt

SYSTEM_PROMPT = """
    You are an Execution Sentinel Agent that can evaluate results of sub-agents and decide if the goals were met.

    You are a sub-agent of a larger multi-agent system and work in an automated fashion. You can not perform actions like file reading or
    writing. Your goal is just to evaluate quality and completeness of the response from other agents.
    
    You have access to the current system datetime: {current_iso_time}.
    You have no other access to external information or APIs. Only raw LLM capabilities.
    """


class ExecutionSentinelAgentPrompt(BasePrompt):
    """Prompt for generating an general all purpose AI response."""

    system_prompt = dedent(SYSTEM_PROMPT).strip()

    def __init__(self, query: ExecutionEvalulationRequest) -> None:
        self.query = query.to_markdown()

    @property
    def parametrized_sys_prompt(self) -> str:
        return self.system_prompt.format(current_iso_time=dt.now().isoformat())

    def to_markdown(self) -> str:
        return dedent(
            f"""
        ### System Prompt
        {self.parametrized_sys_prompt}

        ### Task Prompt
        {self.query}
        """
        ).strip()

    def to_text(self) -> str:
        return dedent(
            f"""
        {self.parametrized_sys_prompt}

        {self.query}
        """
        ).strip()

    def to_message_chain(self) -> list[dict[str, str]]:
        return [
            {"role": "system", "content": self.parametrized_sys_prompt},
            {"role": "user", "content": self.query},
        ]
