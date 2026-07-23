from src.services.rag_service import RAGService


def main():

    rag = RAGService()

    while True:

        question = input(
            "\nAsk a question (or type 'exit'): "
        )

        if question.lower() == "exit":
            break

        response = rag.ask(question)

        print("\nAnswer\n")
        print(response["answer"])

        print("\nSources\n")

        for source in response["sources"]:
            print(
                f"{source['source']} | Chunk {source['chunk_id']}"
            )


if __name__ == "__main__":
    main()