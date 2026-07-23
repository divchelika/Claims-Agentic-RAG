from typing import List

from openai import OpenAI

from src.config.settings import settings
from src.utils.logger import logger


class EmbeddingService:
    """
    Service responsible for generating embeddings
    using Azure AI Foundry.
    """

    def __init__(self):

        self.client = OpenAI(
            base_url=settings.AZURE_OPENAI_ENDPOINT,
            api_key=settings.AZURE_OPENAI_KEY,
        )

    def embed(self, text: str) -> List[float]:
        """
        Converts text into an embedding vector.
        """

        try:
            logger.info("Generating embedding...")

            response = self.client.embeddings.create(
                model=settings.AZURE_OPENAI_EMBEDDING_DEPLOYMENT,
                input=text,
            )

            embedding = response.data[0].embedding

            logger.info(
                f"Embedding generated ({len(embedding)} dimensions)."
            )

            return embedding

        except Exception:
            logger.exception("Embedding generation failed.")
            raise