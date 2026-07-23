import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")

    AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")

    AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")

    AZURE_SEARCH_ENDPOINT = os.getenv("AZURE_SEARCH_ENDPOINT")

    AZURE_SEARCH_KEY = os.getenv("AZURE_SEARCH_KEY")

    AZURE_SEARCH_INDEX = os.getenv("AZURE_SEARCH_INDEX")

    AZURE_OPENAI_EMBEDDING_DEPLOYMENT = os.getenv(
        "AZURE_OPENAI_EMBEDDING_DEPLOYMENT"
    )

    AZURE_SEARCH_ENDPOINT = os.getenv("AZURE_SEARCH_ENDPOINT")
    AZURE_SEARCH_KEY = os.getenv("AZURE_SEARCH_KEY")
    AZURE_SEARCH_INDEX = os.getenv("AZURE_SEARCH_INDEX")

settings = Settings()