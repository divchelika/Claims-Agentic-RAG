from src.agents.planner_agent import PlannerAgent

planner = PlannerAgent()

questions = [
    "Does MRI require preauthorization?",
    "Who is the claims adjuster?",
    "What is the deductible?",
    "Is knee replacement covered?",
]

for q in questions:
    print("-" * 50)
    print(q)
    print(planner.plan(q))