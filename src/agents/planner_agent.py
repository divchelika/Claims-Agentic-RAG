from src.services.openai_service import OpenAIService


class PlannerAgent:
    """
    Determines which specialist agent should answer the user's question.
    """

    def __init__(self, llm=None):
        self.llm = llm or OpenAIService()

    def plan(self, question: str) -> str:

        prompt = f"""
You are a routing agent for an insurance claims assistant.

Your job is NOT to answer the question.

Your ONLY job is to classify it into ONE category.

Categories:

POLICY
- insurance policy
- deductible
- claims adjuster
- contact information
- policy limits
- coverage details
- employer liability

MEDICAL
- MRI
- CT Scan
- surgery
- knee replacement
- physical therapy
- medical necessity
- treatment guidelines
- authorization
- pre-certification
- rehabilitation

GENERAL
- greetings
- thanks
- unrelated questions

Examples:

Question:
Does MRI require preauthorization?
Category:
MEDICAL

Question:
Who is the claims adjuster?
Category:
POLICY

Question:
What is the deductible?
Category:
POLICY

Question:
Is knee replacement covered?
Category:
MEDICAL

Question:
Hello
Category:
GENERAL

Now classify this question.

Question:
{question}

Return ONLY one word.

POLICY
MEDICAL
GENERAL
"""

        category = self.llm.chat(prompt).strip().upper()

        if category not in ["POLICY", "MEDICAL", "GENERAL"]:
            category = "GENERAL"

        return category