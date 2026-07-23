from src.services.document_ingestion_service import (
    DocumentIngestionService,
)


def main():
    ingestion = DocumentIngestionService()
    ingestion.ingest_folder("data")


if __name__ == "__main__":
    main()