from openai import OpenAI

from src.config.settings import settings
from src.utils.logger import logger


class OpenAIService:
    """
    Service responsible for communicating with Azure AI Foundry Models.
    """

    def __init__(self):
        self.client = OpenAI(
            base_url=settings.AZURE_OPENAI_ENDPOINT,
            api_key=settings.AZURE_OPENAI_KEY,
        )

    def chat(self, prompt: str) -> str:
        """
        Sends a prompt to Azure AI Foundry and returns the response.
        """

        try:
            logger.info("Sending prompt to Azure OpenAI...")

            response = self.client.responses.create(
                model=settings.AZURE_OPENAI_DEPLOYMENT,
                input=prompt,
                max_output_tokens=500,
            )

            logger.info("Response received successfully.")

            return response.output_text

        except Exception:
            logger.exception("Azure OpenAI request failed.")
            raise