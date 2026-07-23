from fastapi import FastAPI, HTTPException

from src.agents.orchestrator import AgentOrchestrator
from src.api_models.chat_models import (
    QuestionRequest,
    QuestionResponse,
    SourceResponse,
)

app = FastAPI(
    title="Agentic Insurance Claims Assistant",
    version="1.0.0",
)

orchestrator = AgentOrchestrator()


@app.get("/")
def root():
    return {
        "status": "running"
    }


@app.post(
    "/ask",
    response_model=QuestionResponse,
)
def ask(request: QuestionRequest):

    try:

        result = orchestrator.ask(request.question)

        planner = orchestrator.planner.plan(
            request.question
        )

        return QuestionResponse(
            planner=planner,
            answer=result["answer"],
            verified=result["verified"],
            confidence=result["confidence"],
            sources=[
                SourceResponse(
                    source=s["source"],
                    chunk_id=s["chunk_id"],
                )
                for s in result["sources"]
            ],
        )

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex),
        )