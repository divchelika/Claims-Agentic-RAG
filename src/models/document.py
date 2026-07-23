from dataclasses import dataclass


@dataclass
class Document:
    """
    Represents one searchable document (chunk) stored in Azure AI Search.
    """

    id: str
    content: str
    source: str
    chunk_id: int
    embedding: list[float]

    def to_dict(self) -> dict:
        """
        Converts the document into the format expected by Azure AI Search.
        """
        return {
            "id": self.id,
            "content": self.content,
            "source": self.source,
            "chunk_id": self.chunk_id,
            "embedding": self.embedding,
        }