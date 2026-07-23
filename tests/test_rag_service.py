from unittest.mock import MagicMock

from src.services.rag_service import RAGService


def test_rag_service_returns_answer_and_sources():

    # Create RAG service
    rag = RAGService()

    # Mock RetrievalService
    rag.retriever.retrieve = MagicMock(
        return_value=[
            {
                "content": "MRI requires pre-certification.",
                "source": "policy.pdf",
                "chunk_id": 0,
            }
        ]
    )

    # Mock OpenAIService
    rag.llm.chat = MagicMock(
        side_effect=[
            # Query rewriter response
            "Does MRI require preauthorization?",

            # Final answer
            "Yes, MRI requires pre-certification.",
        ]
    )

    # Ask question
    result = rag.ask(
        "Does MRI require preauthorization?"
    )

    # Assertions
    assert result["answer"] == "Yes, MRI requires pre-certification."

    assert len(result["sources"]) == 1

    assert result["sources"][0]["source"] == "policy.pdf"

    # Verify mocked methods were called
    rag.retriever.retrieve.assert_called_once()

    assert rag.llm.chat.call_count >= 2