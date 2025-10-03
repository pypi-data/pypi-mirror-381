import traceback
from collections.abc import Sequence

from autogen_agentchat.base._termination import (
    TerminatedException,
    TerminationCondition,
)
from autogen_agentchat.messages import (
    AgentEvent,
    ChatMessage,
    StopMessage,
    TextMessage,
    ToolCallExecutionEvent,
    ToolCallSummaryMessage,
)
from autogen_core.models import ChatCompletionClient, SystemMessage

from .logging_utils import get_logger, trace  # noqa: F401

logger = get_logger(__name__)


class SmartReflectorTermination(TerminationCondition):
    """
    A termination condition that tries to identify if an agent is done.
    """

    terminator_prompt = (
        "Below is a conversation between 'user' and '{agent}'. "
        "Look at the user's statement and the last message from "
        "{agent} and determine if {agent} is still working on "
        "responding to the user. Follow these instructions: "
        "1) If {agent} is asking a question to user or is asking "
        "for input, respond with 'END' "
        "2) If {agent} is still working on a response and has "
        "another step to take, reply with '{agent}' "
        "3) Otherwise, reply with 'END'. "
        "Here is the conversation: {history}"
    )

    def __init__(
        self,
        model_client: ChatCompletionClient,
        agent_name: str = "ai",
        oneshot: bool = True,
    ):
        self.agent_name = agent_name
        self.oneshot = oneshot
        self.model_client = model_client
        self._terminated = False
        self._message_history: list[ChatMessage] = []

    async def __call__(
        self, messages: Sequence[AgentEvent | ChatMessage]
    ) -> StopMessage | None:
        if self._terminated:
            raise TerminatedException("Termination condition has already been reached")
        if not messages:
            return None
        self._message_history.extend(messages)

        last_message = self._message_history[-1]

        # last message was from the user, let it through
        if isinstance(last_message, TextMessage) and last_message.source == "user":
            return None

        # Oneshot - always end the conversation
        if self.oneshot:
            return StopMessage(
                content="done",
                source="SmartReflectorTermination",
            )

        # this will force a reflection on the tool call
        if isinstance(last_message, ToolCallSummaryMessage | ToolCallExecutionEvent):
            return None

        # get up to the last 6 messages
        history = ""
        for message in self._message_history[-6:]:
            history += f"{message.source}: {message.content}\n"
        context = [
            SystemMessage(
                content=self.terminator_prompt.format(
                    agent=self.agent_name, history=history
                )
            )
        ]
        try:
            result = await self.model_client.create(
                messages=context,
            )
            logger.debug(f"smart reflecting back: {result.content}")
            if result.content == "END":
                return StopMessage(
                    content="done",
                    source="SmartReflectorTermination",
                )
            else:
                return None
        except Exception as e:
            logger.error(f"SmartReflectorTermination Error from model client: {e}")
            traceback.print_exc()
            return StopMessage(
                content="error",
                source="SmartReflectorTermination",
            )

    @property
    def terminated(self) -> bool:
        return self._terminated

    async def reset(self) -> None:
        self._terminated = False
