from src.services.openai_service import OpenAIService
from src.services.conversation_memory import ConversationMemory


class QueryRewriter:
    """
    Rewrites follow-up questions into standalone questions
    using the conversation history.
    """

    def __init__(
        self,
        llm: OpenAIService | None = None,
    ):
        self.llm = llm or OpenAIService()

    def rewrite(
        self,
        question: str,
        memory: ConversationMemory,
    ) -> str:

        history = "\n".join(
            f"{m.role.upper()}: {m.content}"
            for m in memory.get_history()
        )

        prompt = f"""
You rewrite follow-up questions into standalone questions.

Conversation:

{history}

Current Question:

{question}

Rewrite the question so it is fully understandable without
the previous conversation.

If it is already standalone,
return it unchanged.

Return ONLY the rewritten question.
"""

        return self.llm.chat(prompt).strip()