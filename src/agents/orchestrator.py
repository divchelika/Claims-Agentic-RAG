from src.agents.medical_agent import MedicalAgent
from src.agents.planner_agent import PlannerAgent
from src.agents.policy_agent import PolicyAgent


class AgentOrchestrator:
    """
    Routes questions to the correct specialist agent.
    """

    def __init__(self):
        self.planner = PlannerAgent()
        self.medical = MedicalAgent()
        self.policy = PolicyAgent()

    def ask(self, question: str):

        category = self.planner.plan(question)

        print(f"\nPlanner selected: {category}")

        if category == "MEDICAL":
            return self.medical.answer(question)

        if category == "POLICY":
            return self.policy.answer(question)

        return self.policy.answer(question)