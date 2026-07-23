from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizedQuery

from src.config.settings import settings
from src.models.document import Document


class SearchService:
    """
    Service responsible for communicating with Azure AI Search.
    """

    def __init__(self):
        self.client = SearchClient(
            endpoint=settings.AZURE_SEARCH_ENDPOINT,
            index_name=settings.AZURE_SEARCH_INDEX,
            credential=AzureKeyCredential(
                settings.AZURE_SEARCH_KEY
            ),
        )

    def get_document_count(self):
        return self.client.get_document_count()

    def upload_documents(
        self,
        documents: list[Document],
    ):

        search_documents = [
            document.to_dict()
            for document in documents
        ]

        return self.client.upload_documents(
            documents=search_documents
        )

    def hybrid_search(
        self,
        query: str,
        embedding: list[float],
        top: int = 3,
        filter_expression: str | None = None,
    ):
        """
        Hybrid Search (Keyword + Vector Search)
        with optional filtering.
        """

        vector_query = VectorizedQuery(
            vector=embedding,
            k_nearest_neighbors=top,
            fields="embedding",
        )

        results = self.client.search(
            search_text=query,
            vector_queries=[vector_query],
            filter=filter_expression,
            top=top,
        )

        documents = []

        for result in results:

            documents.append(
                {
                    "content": result["content"],
                    "source": result["source"],
                    "chunk_id": result["chunk_id"],
                    "score": result["@search.score"],
                }
            )

        return documents