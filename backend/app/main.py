"""
Quiz Service Backend - FastAPI Application
A modern backend for interactive quizzes with progressive hints system.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

# Import quiz data from separate modules
from app.science_quizzes import SCIENCE_QUIZZES
from app.history_quizzes import HISTORY_QUIZZES
from app.celebrity_quizzes import CELEBRITY_QUIZZES

# Initialize FastAPI app
app = FastAPI(
    title="Quiz Service API",
    description="Interactive Quiz Service with Progressive Hints",
    version="1.0.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Endpoints
@app.get("/", tags=["Health"])
async def root():
    """Root endpoint - Health check"""
    return {
        "status": "ok",
        "message": "Quiz Service API is running",
        "version": "1.0.0",
    }


@app.get("/nature", tags=["Quizzes"])
async def nature_quiz():
    """
    Science Quiz Endpoint
    Returns a random science quiz with 5 progressive hints.

    Returns:
        - hints: List of 5 hints from general to specific
        - answer: The correct answer
    """
    quiz = random.choice(SCIENCE_QUIZZES)
    return quiz.to_dict()


@app.get("/old", tags=["Quizzes"])
async def history_quiz():
    """
    History Quiz Endpoint
    Returns a random history quiz with 5 progressive hints.

    Returns:
        - hints: List of 5 hints from general to specific
        - answer: The correct answer
    """
    quiz = random.choice(HISTORY_QUIZZES)
    return quiz.to_dict()


@app.get("/fame", tags=["Quizzes"])
async def celebrity_quiz():
    """
    Celebrity Quiz Endpoint
    Returns a random celebrity quiz with 5 progressive hints.

    Returns:
        - hints: List of 5 hints from general to specific
        - answer: The correct answer
    """
    quiz = random.choice(CELEBRITY_QUIZZES)
    return quiz.to_dict()


# Additional endpoints for documentation
@app.get("/quizzes/all", tags=["Documentation"])
async def get_all_quizzes():
    """Get all available quizzes (for documentation purposes)"""
    return {
        "science": len(SCIENCE_QUIZZES),
        "history": len(HISTORY_QUIZZES),
        "celebrity": len(CELEBRITY_QUIZZES),
        "total": len(SCIENCE_QUIZZES) + len(HISTORY_QUIZZES) + len(CELEBRITY_QUIZZES),
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
