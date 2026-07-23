from pathlib import Path

from pypdf import PdfReader


class PDFReader:
    """
    Responsible for extracting raw text from PDF documents.

    This class has a single responsibility:
    Convert a PDF into one continuous text string.

    It does NOT:
    - Chunk text
    - Generate embeddings
    - Upload to Azure Search
    """

    def extract_text(self, pdf_path):
        """
        Extracts all text from a PDF.

        Args:
            pdf_path (str):
                Path to the PDF file.

        Returns:
            str:
                Complete extracted text from the PDF.
        """

        path = Path(pdf_path)

        if not path.exists():
            raise FileNotFoundError(f"PDF not found: {pdf_path}")

        reader = PdfReader(path)

        pages = []

        for page in reader.pages:
            text = page.extract_text()

            if text:
                pages.append(text)

        return "\n".join(pages)