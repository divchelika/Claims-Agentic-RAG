from typing import List

from openai import OpenAI

from azure.identity import DefaultAzureCredential, get_bearer_token_provider

from src.config.settings import settings


class EmbeddingService:
    """
    Service responsible for generating embeddings using Azure OpenAI.
    """

    def __init__(self):

        token_provider = get_bearer_token_provider(
            DefaultAzureCredential(),
            "https://ai.azure.com/.default",
        )

        self.client = OpenAI(
            base_url=settings.AZURE_OPENAI_ENDPOINT,
            api_key=token_provider,
        )

    def embed(self, text: str) -> List[float]:
        """
        Converts text into an embedding vector.
        """

        response = self.client.embeddings.create(
            model=settings.AZURE_OPENAI_EMBEDDING_DEPLOYMENT,
            input=text,
        )

        return response.data[0].embedding