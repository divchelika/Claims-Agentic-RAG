from src.agents.orchestrator import AgentOrchestrator


orchestrator = AgentOrchestrator()

questions = [
    "Does MRI require preauthorization?",
    "Who is the claims adjuster?",
    "What is the deductible?",
    "Is knee replacement covered?",
]

for question in questions:

    print("\n" + "=" * 60)
    print(question)

    result = orchestrator.ask(question)

    print("\nAnswer:")
    print(result["answer"])

    print("\nVerified:")
    print(result["verified"])

    print("\nConfidence:")
    print(result["confidence"])

    print("\nSources:")

    for source in result["sources"]:
        print(
            f'{source["source"]} | Chunk {source["chunk_id"]}'
        )