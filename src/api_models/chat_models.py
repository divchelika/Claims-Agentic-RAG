from pydantic import BaseModel


class QuestionRequest(BaseModel):
    question: str


class SourceResponse(BaseModel):
    source: str
    chunk_id: int


class QuestionResponse(BaseModel):
    planner: str
    answer: str
    verified: bool
    confidence: str
    sources: list[SourceResponse]