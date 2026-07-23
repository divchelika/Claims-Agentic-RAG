from src.services.openai_service import OpenAIService


class VerifierService:
    """
    Verifies whether the generated answer is supported
    by the retrieved context.
    """

    def __init__(self):
        self.llm = OpenAIService()

    def verify(
        self,
        question: str,
        answer: str,
        context: str,
    ) -> dict:
        """
        Returns:
            {
                "verified": bool,
                "confidence": "HIGH" | "MEDIUM" | "LOW"
            }
        """

        prompt = f"""
You are an AI quality assurance reviewer.

Question:
{question}

Retrieved Context:
{context}

Generated Answer:
{answer}

Determine whether the answer is completely supported
by the retrieved context.

Respond ONLY in this format:

VERIFIED: YES or NO
CONFIDENCE: HIGH, MEDIUM, or LOW

Do not explain.
"""

        result = self.llm.chat(prompt)

        verified = "VERIFIED: YES" in result.upper()

        if "HIGH" in result.upper():
            confidence = "HIGH"
        elif "MEDIUM" in result.upper():
            confidence = "MEDIUM"
        else:
            confidence = "LOW"

        return {
            "verified": verified,
            "confidence": confidence,
        }