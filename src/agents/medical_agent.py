from src.services.rag_service import RAGService


MEDICAL_PROMPT = """
You are the Medical Review Agent.

You specialize in:

- Medical necessity
- MRI
- CT Scan
- Knee replacement
- Surgery
- Physical therapy
- Rehabilitation
- Treatment guidelines
- Clinical review
- Utilization review
- Preauthorization

Always answer ONLY from the retrieved context.

If the answer is unavailable, reply:

"I don't have enough information to answer that."

Do not guess.
"""


MEDICAL_FILTER = (
    "source eq 'medical_necessity.pdf' "
    "or source eq 'knee_replacement_guideline.pdf'"
)


class MedicalAgent:

    def __init__(self):

        self.rag = RAGService(
            system_prompt=MEDICAL_PROMPT,
            filter_expression=MEDICAL_FILTER,
        )

    def answer(self, question: str):

        return self.rag.ask(question)