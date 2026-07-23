from src.services.embedding_service import EmbeddingService
from src.services.search_service import SearchService


class RetrievalService:
    """
    Retrieves relevant chunks using Hybrid Search.
    """

    def __init__(self):

        self.embedding_service = EmbeddingService()
        self.search_service = SearchService()

    def retrieve(
        self,
        question: str,
        top_k: int = 3,
        filter_expression: str | None = None,
    ):

        embedding = self.embedding_service.embed(question)

        return self.search_service.hybrid_search(
            query=question,
            embedding=embedding,
            top=top_k,
            filter_expression=filter_expression,
        )