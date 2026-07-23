import pytest

from src.ingestion.text_chunker import TextChunker


def test_small_text_returns_single_chunk():
    """
    Text smaller than chunk_size should produce one chunk.
    """

    chunker = TextChunker(
        chunk_size=100,
        overlap=20,
    )

    text = "Hello World"

    chunks = chunker.chunk(text)

    assert len(chunks) == 1
    assert chunks[0] == text


def test_large_text_returns_multiple_chunks():
    """
    Large text should be split into multiple chunks.
    """

    chunker = TextChunker(
        chunk_size=50,
        overlap=10,
    )

    text = "Python " * 100

    chunks = chunker.chunk(text)

    assert len(chunks) > 1


def test_invalid_overlap_raises_error():
    """
    overlap cannot be larger than chunk_size.
    """

    with pytest.raises(ValueError):

        TextChunker(
            chunk_size=100,
            overlap=100,
        )


def test_chunks_do_not_exceed_chunk_size():
    """
    Every chunk should be less than or equal to chunk_size.
    """

    chunker = TextChunker(
        chunk_size=80,
        overlap=20,
    )

    text = "Azure AI Search " * 100

    chunks = chunker.chunk(text)

    for chunk in chunks:
        assert len(chunk) <= 80