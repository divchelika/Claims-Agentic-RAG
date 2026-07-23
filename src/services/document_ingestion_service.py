from pathlib import Path

from src.ingestion.pdf_reader import PDFReader
from src.ingestion.text_chunker import TextChunker
from src.models.document import Document
from src.services.embedding_service import EmbeddingService
from src.services.search_service import SearchService
from src.utils.logger import logger


class DocumentIngestionService:
    """
    Reads every PDF in the data folder and uploads it to Azure AI Search.
    """

    def __init__(self):
        self.reader = PDFReader()
        self.chunker = TextChunker()
        self.embedding_service = EmbeddingService()
        self.search_service = SearchService()

    def ingest_folder(self, folder_path: str):

        folder = Path(folder_path)

        logger.info(f"Scanning folder: {folder.resolve()}")

        pdf_files = sorted(folder.glob("*.pdf"))

        if not pdf_files:
            logger.warning("No PDF files found.")
            return

        logger.info(f"Found {len(pdf_files)} PDF(s).")

        for pdf in pdf_files:

            logger.info(f"Processing {pdf.name}")

            text = self.reader.extract_text(pdf)

            logger.info(
                f"Extracted {len(text)} characters from {pdf.name}"
            )

            chunks = self.chunker.chunk(text)

            logger.info(
                f"Created {len(chunks)} chunks"
            )

            documents = []

            for i, chunk in enumerate(chunks):

                logger.info(
                    f"Generating embedding for chunk {i}"
                )

                embedding = self.embedding_service.embed(chunk)

                documents.append(
                    Document(
                        id=f"{pdf.stem}_{i}",
                        content=chunk,
                        source=pdf.name,
                        chunk_id=i,
                        embedding=embedding,
                    )
                )

            logger.info(
                f"Uploading {len(documents)} documents to Azure AI Search"
            )

            self.search_service.upload_documents(documents)

            logger.info(
                f"Finished processing {pdf.name}"
            )

        logger.info("Document ingestion completed successfully.")