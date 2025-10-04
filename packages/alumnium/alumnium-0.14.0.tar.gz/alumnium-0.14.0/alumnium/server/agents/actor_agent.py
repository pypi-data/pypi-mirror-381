from typing import Dict, Type

from langchain_core.language_models import BaseChatModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import BaseTool

from ..logutils import get_logger
from .base_agent import BaseAgent

logger = get_logger(__name__)


class ActorAgent(BaseAgent):
    def __init__(self, llm: BaseChatModel, tools: Dict[str, Type[BaseTool]]):
        super().__init__()

        llm = llm.bind_tools(list(tools.values()))

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", self.prompts["system"]),
                ("human", self.prompts["user"]),
            ]
        )

        self.chain = prompt | llm

    def invoke(
        self,
        goal: str,
        step: str,
        accessibility_tree_xml: str,
    ):
        if not step.strip():
            return

        logger.info("Starting action:")
        logger.info(f"  -> Goal: {goal}")
        logger.info(f"  -> Step: {step}")
        logger.debug(f"  -> Accessibility tree: {accessibility_tree_xml}")

        message = self._invoke_chain(
            self.chain,
            {"goal": goal, "step": step, "accessibility_tree": accessibility_tree_xml},
        )

        logger.info(f"  <- Tools: {message.tool_calls}")
        logger.info(f"  <- Usage: {message.usage_metadata}")

        # Return tool calls for the client to execute
        return message.tool_calls
