from typing import List


class TextChunker:
    """
    Splits raw text into overlapping chunks.

    This class is responsible only for chunking text.
    It knows nothing about PDFs, embeddings, or Azure AI Search.
    """

    def __init__(
        self,
        chunk_size: int = 800,
        overlap: int = 100,
    ):
        if overlap >= chunk_size:
            raise ValueError(
                "overlap must be smaller than chunk_size."
            )

        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, text: str) -> List[str]:
        """
        Splits text into overlapping chunks while trying
        to avoid breaking words.

        Args:
            text: Raw document text.

        Returns:
            List[str]: List of text chunks.
        """

        chunks = []

        start = 0
        text_length = len(text)

        while start < text_length:

            # Initial chunk boundary
            tentative_end = min(
                start + self.chunk_size,
                text_length
            )

            # If we're not at the end of the document,
            # move the boundary back to the last whitespace.
            if tentative_end < text_length:
                last_space = text.rfind(
                    " ",
                    start,
                    tentative_end
                )

                if last_space != -1:
                    end = last_space
                else:
                    end = tentative_end
            else:
                end = tentative_end

            chunk = text[start:end].strip()

            if chunk:
                chunks.append(chunk)

            # Stop if we've reached the end
            if end == text_length:
                break

            # Move forward while preserving overlap
            start = max(
                end - self.overlap,
                0
            )

        return chunks