import base64
import importlib.metadata
from contextlib import asynccontextmanager
from typing import List

from fastapi import APIRouter, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .api_models import (
    AddExampleRequest,
    AddExampleResponse,
    AreaRequest,
    AreaResponse,
    ClearExamplesResponse,
    ErrorResponse,
    FindRequest,
    FindResponse,
    PlanRequest,
    PlanResponse,
    SessionRequest,
    SessionResponse,
    StatementRequest,
    StatementResponse,
    StepRequest,
    StepResponse,
)
from .logutils import get_logger
from .models import Model
from .session_manager import SessionManager

logger = get_logger(__name__)

# Global session manager
session_manager = SessionManager()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager."""
    logger.info("Starting Alumnium Server")
    yield
    logger.info("Shutting down Alumnium Server")


# FastAPI app
app = FastAPI(
    title="Alumnium Server",
    description="AI-powered test automation server",
    version=importlib.metadata.version("alumnium"),
    lifespan=lifespan,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create v1 API router
v1_router = APIRouter(prefix="/v1")


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "model": f"{Model.current.provider.value}/{Model.current.name}"}


@v1_router.post("/sessions", response_model=SessionResponse)
async def create_session(request: SessionRequest):
    """Create a new session."""
    try:
        session_id = session_manager.create_session(request.provider, request.name, request.tools)
        return SessionResponse(sessionId=session_id)
    except Exception as e:
        logger.error(f"Failed to create session: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Failed to create session: {str(e)}"
        )


@v1_router.delete("/sessions/{session_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_session(session_id: str):
    """Delete a session."""
    if not session_manager.delete_session(session_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Session not found")


@v1_router.get("/sessions", response_model=List[str])
async def list_sessions():
    """List all active sessions."""
    return session_manager.list_sessions()


@v1_router.get("/sessions/{session_id}/stats")
async def get_session_stats(session_id: str):
    """Get session statistics."""
    session = session_manager.get_session(session_id)
    if session is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Session not found")
    return session.stats


@v1_router.post("/sessions/{session_id}/plans", response_model=PlanResponse)
async def plan_actions(session_id: str, request: PlanRequest):
    """Plan actions to achieve a goal."""
    session = session_manager.get_session(session_id)
    if not session:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Session not found")

    try:
        steps = session.planner_agent.invoke(request.goal, request.accessibility_tree)
        return PlanResponse(steps=steps)

    except Exception as e:
        logger.error(f"Failed to plan actions for session {session_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Failed to plan actions: {str(e)}"
        )


@v1_router.post("/sessions/{session_id}/steps", response_model=StepResponse)
async def plan_step_actions(session_id: str, request: StepRequest):
    """Plan exact actions for a step."""
    session = session_manager.get_session(session_id)
    if not session:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Session not found")

    try:
        actions = session.actor_agent.invoke(request.goal, request.step, request.accessibility_tree)
        return StepResponse(actions=actions)

    except Exception as e:
        logger.error(f"Failed to execute actions for session {session_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Failed to execute actions: {str(e)}"
        )


@v1_router.post("/sessions/{session_id}/statements", response_model=StatementResponse)
async def execute_statement(session_id: str, request: StatementRequest):
    """Execute a statement against the current page state."""
    session = session_manager.get_session(session_id)
    if not session:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Session not found")

    try:
        # Decode screenshot if provided
        screenshot_bytes = None
        if request.screenshot:
            try:
                screenshot_bytes = base64.b64decode(request.screenshot)
            except Exception as e:
                logger.warning(f"Failed to decode screenshot: {e}")

        # Use retriever agent to execute the statement
        explanation, value = session.retriever_agent.invoke(
            request.statement,
            request.accessibility_tree,
            title=request.title,
            url=request.url,
            screenshot=screenshot_bytes,
        )

        return StatementResponse(result=str(value), explanation=explanation)

    except Exception as e:
        logger.error(f"Failed to execute statement for session {session_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Failed to verify statement: {str(e)}"
        )


@v1_router.post("/sessions/{session_id}/areas", response_model=AreaResponse)
async def choose_area(session_id: str, request: AreaRequest):
    """Choose the accessibility area."""
    session = session_manager.get_session(session_id)
    if not session:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Session not found")

    try:
        area = session.area_agent.invoke(request.description, request.accessibility_tree)
        return AreaResponse(**area)

    except Exception as e:
        logger.error(f"Failed to choose accessibility area for session {session_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Failed to choose accessibility area: {str(e)}"
        )


@v1_router.post("/sessions/{session_id}/examples", response_model=AddExampleResponse)
async def add_example(session_id: str, request: AddExampleRequest):
    """Add an example goal and actions to the planner agent."""
    session = session_manager.get_session(session_id)
    if not session:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Session not found")

    try:
        session.planner_agent.add_example(request.goal, request.actions)
        return AddExampleResponse(success=True, message="Example added successfully")

    except Exception as e:
        logger.error(f"Failed to add example for session {session_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Failed to add example: {str(e)}"
        )


@v1_router.post("/sessions/{session_id}/elements", response_model=FindResponse)
async def find_element(session_id: str, request: FindRequest):
    """Find an element in the accessibility tree."""
    session = session_manager.get_session(session_id)
    if not session:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Session not found")

    try:
        elements = session.locator_agent.invoke(request.description, request.accessibility_tree)
        return FindResponse(elements=elements)

    except Exception as e:
        logger.error(f"Failed to find element for session {session_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Failed to find element: {str(e)}"
        )


@v1_router.delete("/sessions/{session_id}/examples", response_model=ClearExamplesResponse)
async def clear_examples(session_id: str):
    """Clear all examples from the planner agent."""
    session = session_manager.get_session(session_id)
    if not session:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Session not found")

    try:
        session.planner_agent.prompt_with_examples.examples.clear()
        return ClearExamplesResponse(success=True, message="All examples cleared successfully")

    except Exception as e:
        logger.error(f"Failed to clear examples for session {session_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Failed to clear examples: {str(e)}"
        )


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Handle HTTP exceptions."""
    _ = request  # Unused parameter
    error_response = ErrorResponse(error=exc.detail, detail=str(exc.status_code))
    return JSONResponse(status_code=exc.status_code, content=error_response.model_dump())


@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    """Handle general exceptions."""
    _ = request  # Unused parameter
    logger.error(f"Unhandled exception: {exc}")
    error_response = ErrorResponse(error="Internal server error", detail=str(exc))
    return JSONResponse(status_code=500, content=error_response.model_dump())


# Include the v1 router after all routes are defined
app.include_router(v1_router)


def main():
    """Main entry point for running the server."""
    import uvicorn

    uvicorn.run("alumnium.server.main:app", host="0.0.0.0", port=8013, reload=True, log_level="info")


if __name__ == "__main__":
    main()
