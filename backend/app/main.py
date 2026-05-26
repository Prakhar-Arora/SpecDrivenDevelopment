"""FastAPI Quiz Service application.

Main entry point for the Quiz Service API. Configures FastAPI app,
CORS middleware, logging, error handling, and exposes three quiz endpoints.

Run with: uvicorn backend.app.main:app --reload
"""

import logging
from datetime import datetime
from typing import Dict

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from backend.app.models import AnswerSubmission, AnswerValidation, ErrorResponse, Quiz
from backend.app.exceptions import InvalidCategoryError, InvalidInputError, QuizError
from backend.app.quiz_service import QuizService

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app with enhanced metadata for OpenAPI
app = FastAPI(
    title="Quiz Service API",
    description="Interactive quiz service with three categories: Science, History, and Celebrity. "
    "Each quiz presents 5 progressive hints to help you guess the correct answer.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    contact={
        "name": "Quiz Service Team",
        "email": "support@quizservice.example.com",
    },
    license_info={
        "name": "MIT",
    },
)

# Configure CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex="http(s)?://(localhost|127\\.0\\.0\\.1)(:\\d+)?",  # Allow all localhost ports
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================================
# Exception Handlers (Task 5.2: Exception handler middleware)
# ============================================================================


@app.exception_handler(QuizError)
async def quiz_error_handler(request: Request, exc: QuizError) -> JSONResponse:
    """Handle QuizError exceptions with standardized error response.

    Args:
        request: The HTTP request.
        exc: The QuizError exception.

    Returns:
        JSON response with error details and HTTP status code.
    """
    logger.warning(f"Quiz error on {request.url}: {exc.message}")
    error_response = ErrorResponse(
        status=exc.status_code,
        error=exc.error_code,
        message=exc.message,
    )
    return JSONResponse(
        status_code=exc.status_code,
        content=error_response.model_dump(),
    )


@app.exception_handler(Exception)
async def general_error_handler(request: Request, exc: Exception) -> JSONResponse:
    """Handle unexpected exceptions with standardized error response.

    Args:
        request: The HTTP request.
        exc: The exception.

    Returns:
        JSON response with generic error message.
    """
    logger.error(f"Unexpected error on {request.url}: {str(exc)}")
    error_response = ErrorResponse(
        status=500,
        error="internal_error",
        message="An unexpected error occurred. Please try again later.",
    )
    return JSONResponse(
        status_code=500,
        content=error_response.model_dump(),
    )


# ============================================================================
# Health Check Endpoint
# ============================================================================


@app.get(
    "/health",
    response_model=Dict[str, str],
    tags=["Health"],
    summary="Health Check",
    description="Verify that the API is running and healthy.",
)
def health_check() -> Dict[str, str]:
    """Health check endpoint for deployment verification.

    Returns:
        Dictionary with status and timestamp indicating service health.
    """
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
    }


# ============================================================================
# Quiz Endpoints (Tasks 4.1-4.3: Three quiz category endpoints)
# ============================================================================


@app.get(
    "/nature",
    response_model=Quiz,
    responses={
        200: {
            "description": "A science quiz with 5 progressive hints",
            "model": Quiz,
        },
        500: {
            "description": "Internal server error",
            "model": ErrorResponse,
        },
    },
    tags=["Quiz Endpoints"],
    summary="Get a Science Quiz",
    description="Returns a random science/nature quiz with 5 progressive hints ordered from general to specific.",
)
def get_nature_quiz() -> Quiz:
    """Retrieve a science (nature) quiz.

    Returns a random quiz from the science category with five hints
    ordered progressively from general (hint 1) to specific (hint 5).
    Each hint provides additional context to help guess the correct answer.

    Returns:
        Quiz object containing:
        - id: Unique quiz identifier
        - category: "science"
        - hints: Array of exactly 5 Hint objects with order and text
        - answer: The correct answer to the quiz

    Raises:
        Exception: If an unexpected error occurs retrieving the quiz.

    Task 4.1: Implement GET /nature endpoint
    Task 4.4: Add response model decorators for OpenAPI documentation
    Task 4.5: Add docstrings explaining what the endpoint does
    Task 4.6: Verify consistent Quiz object structure
    """
    try:
        logger.info("Retrieving science quiz")
        quiz = QuizService.get_quiz("science")
        logger.info(f"Successfully retrieved quiz: {quiz.id}")
        return quiz
    except ValueError as e:
        logger.error(f"Failed to retrieve science quiz: {str(e)}")
        raise InvalidCategoryError("science", QuizService.VALID_CATEGORIES)


@app.get(
    "/old",
    response_model=Quiz,
    responses={
        200: {
            "description": "A history quiz with 5 progressive hints",
            "model": Quiz,
        },
        500: {
            "description": "Internal server error",
            "model": ErrorResponse,
        },
    },
    tags=["Quiz Endpoints"],
    summary="Get a History Quiz",
    description="Returns a random history quiz with 5 progressive hints ordered from general to specific.",
)
def get_history_quiz() -> Quiz:
    """Retrieve a history (old) quiz.

    Returns a random quiz from the history category with five hints
    ordered progressively from general (hint 1) to specific (hint 5).
    Each hint provides additional context to help guess the correct answer.

    Returns:
        Quiz object containing:
        - id: Unique quiz identifier
        - category: "history"
        - hints: Array of exactly 5 Hint objects with order and text
        - answer: The correct answer to the quiz

    Raises:
        Exception: If an unexpected error occurs retrieving the quiz.

    Task 4.2: Implement GET /old endpoint
    Task 4.4: Add response model decorators for OpenAPI documentation
    Task 4.5: Add docstrings explaining what the endpoint does
    Task 4.6: Verify consistent Quiz object structure
    """
    try:
        logger.info("Retrieving history quiz")
        quiz = QuizService.get_quiz("history")
        logger.info(f"Successfully retrieved quiz: {quiz.id}")
        return quiz
    except ValueError as e:
        logger.error(f"Failed to retrieve history quiz: {str(e)}")
        raise InvalidCategoryError("history", QuizService.VALID_CATEGORIES)


@app.get(
    "/fame",
    response_model=Quiz,
    responses={
        200: {
            "description": "A celebrity quiz with 5 progressive hints",
            "model": Quiz,
        },
        500: {
            "description": "Internal server error",
            "model": ErrorResponse,
        },
    },
    tags=["Quiz Endpoints"],
    summary="Get a Celebrity Quiz",
    description="Returns a random celebrity quiz with 5 progressive hints ordered from general to specific.",
)
def get_celebrity_quiz() -> Quiz:
    """Retrieve a celebrity (fame) quiz.

    Returns a random quiz from the celebrity category with five hints
    ordered progressively from general (hint 1) to specific (hint 5).
    Each hint provides additional context to help guess the correct answer.

    Returns:
        Quiz object containing:
        - id: Unique quiz identifier
        - category: "celebrity"
        - hints: Array of exactly 5 Hint objects with order and text
        - answer: The correct answer to the quiz

    Raises:
        Exception: If an unexpected error occurs retrieving the quiz.

    Task 4.3: Implement GET /fame endpoint
    Task 4.4: Add response model decorators for OpenAPI documentation
    Task 4.5: Add docstrings explaining what the endpoint does
    Task 4.6: Verify consistent Quiz object structure
    """
    try:
        logger.info("Retrieving celebrity quiz")
        quiz = QuizService.get_quiz("celebrity")
        logger.info(f"Successfully retrieved quiz: {quiz.id}")
        return quiz
    except ValueError as e:
        logger.error(f"Failed to retrieve celebrity quiz: {str(e)}")
        raise InvalidCategoryError("celebrity", QuizService.VALID_CATEGORIES)


# ============================================================================
# Answer Validation Endpoint
# ============================================================================


@app.post(
    "/validate",
    response_model=AnswerValidation,
    responses={
        200: {
            "description": "Answer validation result",
            "model": AnswerValidation,
        },
        400: {
            "description": "Invalid input",
            "model": ErrorResponse,
        },
    },
    tags=["Answer Validation"],
    summary="Validate a Quiz Answer",
    description="Submit an answer for a quiz and receive validation result.",
)
def validate_answer(submission: AnswerSubmission) -> AnswerValidation:
    """Validate a user's answer to a quiz.

    Task 5.3: Add validation for empty/null inputs
    Task 5.4: Implement error responses with standardized format
    Task 5.5: Add logging for all errors
    Task 5.6: Verify error handling works with invalid inputs

    Args:
        submission: AnswerSubmission with quiz_id and user_answer

    Returns:
        AnswerValidation with is_correct, message, and optional correct_answer

    Raises:
        InvalidInputError: If quiz_id or user_answer is invalid
    """
    # Task 5.3: Validation for empty/null inputs
    if not submission.quiz_id or not submission.quiz_id.strip():
        logger.warning("Answer validation attempted with empty quiz_id")
        raise InvalidInputError("quiz_id", "cannot be empty")

    if not submission.user_answer or not submission.user_answer.strip():
        logger.warning(
            f"Answer validation attempted for {submission.quiz_id} with empty answer"
        )
        raise InvalidInputError("user_answer", "cannot be empty")

    # Task 5.5: Add logging
    logger.info(f"Validating answer for quiz: {submission.quiz_id}")

    try:
        result = QuizService.validate_answer(submission.quiz_id, submission.user_answer)
        logger.info(
            f"Answer validation result for {submission.quiz_id}: {result.is_correct}"
        )
        return result
    except Exception as e:
        logger.error(f"Error validating answer for {submission.quiz_id}: {str(e)}")
        raise


# ============================================================================
# Application Entry Point (Task 6: API Documentation)
# ============================================================================
# FastAPI automatically generates OpenAPI documentation at /docs (Swagger UI)
# and /redoc (ReDoc) based on the endpoints and models defined above.
#
# Task 6.1-6.6: API Documentation verification:
# - /docs: Interactive Swagger UI with request/response examples
# - /redoc: ReDoc documentation view
# - OpenAPI schema automatically generated from:
#   * Response models (Quiz, AnswerValidation, ErrorResponse)
#   * Endpoint summaries and descriptions
#   * Example responses in @app.get/@app.post decorators
#   * Error response models (500, 400 status codes)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info",
    )
