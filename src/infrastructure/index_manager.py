from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchIndex,
    SimpleField,
    SearchableField,
    SearchField,
    SearchFieldDataType,
    VectorSearch,
    HnswAlgorithmConfiguration,
    VectorSearchProfile,
)

from src.config.settings import settings
from src.utils.logger import logger


class IndexManager:
    """
    Responsible for creating and managing Azure AI Search indexes.
    """

    def __init__(self):
        self.client = SearchIndexClient(
            endpoint=settings.AZURE_SEARCH_ENDPOINT,
            credential=AzureKeyCredential(
                settings.AZURE_SEARCH_KEY
            ),
        )

    def list_indexes(self):
        """
        Returns all existing indexes.
        """
        try:
            indexes = list(self.client.list_index_names())
            logger.info(f"Found {len(indexes)} index(es).")
            return indexes

        except Exception:
            logger.exception("Failed to retrieve index list.")
            raise

    def create_index(self):
        """
        Creates the Azure AI Search index if it does not already exist.
        """

        try:
            # Check if the index already exists
            if settings.AZURE_SEARCH_INDEX in self.list_indexes():
                logger.info(
                    f"Index '{settings.AZURE_SEARCH_INDEX}' already exists."
                )
                return

            logger.info(
                f"Creating index '{settings.AZURE_SEARCH_INDEX}'..."
            )

            fields = [
                SimpleField(
                    name="id",
                    type=SearchFieldDataType.String,
                    key=True,
                ),

                SearchableField(
                    name="content",
                    type=SearchFieldDataType.String,
                    retrievable=True,
                ),

                SimpleField(
                    name="source",
                    type=SearchFieldDataType.String,
                    filterable=True,
                ),
                SimpleField(
                    name="chunk_id",
                    type=SearchFieldDataType.Int32,
                ),

                SearchField(
                    name="embedding",
                    type=SearchFieldDataType.Collection(
                        SearchFieldDataType.Single
                    ),
                    searchable=True,
                    vector_search_dimensions=1536,
                    vector_search_profile_name="claims-vector-profile",
                ),
            ]

            vector_search = VectorSearch(
                algorithms=[
                    HnswAlgorithmConfiguration(
                        name="claims-hnsw"
                    )
                ],
                profiles=[
                    VectorSearchProfile(
                        name="claims-vector-profile",
                        algorithm_configuration_name="claims-hnsw",
                    )
                ],
            )

            index = SearchIndex(
                name=settings.AZURE_SEARCH_INDEX,
                fields=fields,
                vector_search=vector_search,
            )

            self.client.create_index(index)

            logger.info(
                f"Index '{settings.AZURE_SEARCH_INDEX}' created successfully."
            )

        except Exception:
            logger.exception("Failed to create Azure AI Search index.")
            raise