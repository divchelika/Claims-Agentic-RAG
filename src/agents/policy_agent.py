from src.services.rag_service import RAGService


POLICY_PROMPT = """
You are the Insurance Policy Agent.

You specialize in:

- Insurance policy coverage
- Policy limits
- Deductibles
- Claims adjusters
- Contact information
- Employer liability
- Workers' Compensation policy

Always answer ONLY from the retrieved context.

If the answer is unavailable, reply:

"I don't have enough information to answer that."

Do not guess.
"""


POLICY_FILTER = (
    "source eq 'insurance_policy.pdf'"
)


class PolicyAgent:

    def __init__(self):

        self.rag = RAGService(
            system_prompt=POLICY_PROMPT,
            filter_expression=POLICY_FILTER,
        )

    def answer(self, question: str):

        return self.rag.ask(question)