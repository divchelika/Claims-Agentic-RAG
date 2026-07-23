from unittest.mock import MagicMock

from src.services.document_ingestion_service import (
    DocumentIngestionService,
)


def test_ingest_folder_uploads_documents(tmp_path):

    # Create fake PDF
    pdf = tmp_path / "policy.pdf"
    pdf.write_text("fake")

    ingestion = DocumentIngestionService()

    # Mock PDF reader
    ingestion.reader.extract_text = MagicMock(
        return_value="MRI requires authorization."
    )

    # Mock chunker
    ingestion.chunker.chunk = MagicMock(
        return_value=[
            "MRI requires authorization."
        ]
    )

    # Mock embedding service
    ingestion.embedding_service.embed = MagicMock(
        return_value=[0.1, 0.2, 0.3]
    )

    # Mock upload
    ingestion.search_service.upload_documents = MagicMock()

    # Execute
    ingestion.ingest_folder(tmp_path)

    # Verify workflow
    ingestion.reader.extract_text.assert_called_once()

    ingestion.chunker.chunk.assert_called_once()

    ingestion.embedding_service.embed.assert_called_once()

    ingestion.search_service.upload_documents.assert_called_once()