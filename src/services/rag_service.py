from src.services.openai_service import OpenAIService
from src.services.retrieval_service import RetrievalService
from src.services.verifier_service import VerifierService
from src.services.conversation_memory import ConversationMemory
from src.services.query_rewriter import QueryRewriter


class RAGService:
    """
    Retrieves relevant context, generates a grounded answer,
    and verifies the answer using the retrieved context.
    """

    def __init__(
        self,
        system_prompt: str = "You are an insurance claims assistant.",
        filter_expression: str | None = None,
        retriever: RetrievalService | None = None,
        llm: OpenAIService | None = None,
        memory: ConversationMemory | None = None,
        rewriter: QueryRewriter | None = None,
    ):
        self.system_prompt = system_prompt
        self.filter_expression = filter_expression

        self.retriever = retriever or RetrievalService()
        self.llm = llm or OpenAIService()
        self.memory = memory or ConversationMemory()
        self.rewriter = rewriter or QueryRewriter(self.llm)
        self.verifier = VerifierService()

    def ask(self, question: str):

        # Save the user's question
        self.memory.add_user_message(question)

        # Rewrite follow-up questions
        rewritten_question = self.rewriter.rewrite(
            question,
            self.memory,
        )

        print(f"\nRewritten Question: {rewritten_question}")

        # Retrieve documents
        results = self.retriever.retrieve(
            rewritten_question,
            filter_expression=self.filter_expression,
        )

        # Build context
        context = "\n\n".join(
            doc["content"] for doc in results
        )

        # Build conversation history
        history = "\n".join(
            f"{message.role.upper()}: {message.content}"
            for message in self.memory.get_history()
        )

        # Build prompt
        prompt = f"""
{self.system_prompt}

Use the previous conversation whenever it helps answer follow-up questions.

Answer ONLY using the retrieved context below.

If the answer cannot be found in the retrieved context, reply exactly:

"I don't have enough information to answer that."

Conversation History:
{history}

Retrieved Context:
{context}

Current Question:
{rewritten_question}
"""

        # Generate answer
        answer = self.llm.chat(prompt)

        # Save assistant response
        self.memory.add_assistant_message(answer)

        # Verify answer
        verification = self.verifier.verify(
            question=rewritten_question,
            answer=answer,
            context=context,
        )

        return {
            "answer": answer,
            "sources": results,
            "verified": verification["verified"],
            "confidence": verification["confidence"],
        }