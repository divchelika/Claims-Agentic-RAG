from src.models.document import Document


def test_document_to_dict():

    document = Document(
        id="1",
        content="MRI requires preauthorization.",
        source="policy.pdf",
        chunk_id=0,
        embedding=[0.1, 0.2, 0.3],
    )

    expected = {
        "id": "1",
        "content": "MRI requires preauthorization.",
        "source": "policy.pdf",
        "chunk_id": 0,
        "embedding": [0.1, 0.2, 0.3],
    }

    assert document.to_dict() == expected