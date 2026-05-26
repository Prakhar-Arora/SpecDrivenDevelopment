"""Pydantic models for Quiz Service API.

Provides type-safe data models for quiz questions, hints, and responses.
All models include type hints and validation for automatic OpenAPI documentation.
"""

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class Hint(BaseModel):
    """A single hint in a quiz sequence.

    Attributes:
        order: Sequential position of hint (1-5, where 1 is most general).
        text: The hint content that guides users toward the answer.
    """

    order: int = Field(..., ge=1, le=5, description="Hint sequence number (1-5)")
    text: str = Field(..., min_length=1, max_length=500, description="Hint content")

    model_config = {
        "json_schema_extra": {
            "examples": [{"order": 1, "text": "I am found throughout nature"}]
        }
    }


class Quiz(BaseModel):
    """A complete quiz object with hints and answer.

    Attributes:
        id: Unique identifier for the quiz.
        category: Quiz category (science, history, celebrity).
        hints: List of 5 progressive hints ordered from general to specific.
        answer: The correct answer to the quiz.
    """

    id: str = Field(..., description="Unique quiz identifier")
    category: str = Field(
        ..., description="Quiz category: science, history, or celebrity"
    )
    hints: List[Hint] = Field(
        ..., min_length=5, max_length=5, description="Exactly 5 progressive hints"
    )
    answer: str = Field(..., min_length=1, max_length=200, description="Correct answer")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "science_001",
                    "category": "science",
                    "hints": [
                        {"order": 1, "text": "I am found throughout nature"},
                        {"order": 2, "text": "I am essential to all living organisms"},
                        {"order": 3, "text": "I can exist in three states"},
                        {"order": 4, "text": "I make up 70% of Earth's surface"},
                        {"order": 5, "text": "Chemical formula: H2O"},
                    ],
                    "answer": "water",
                }
            ]
        }
    }


class AnswerSubmission(BaseModel):
    """User's answer submission.

    Attributes:
        quiz_id: ID of the quiz being answered.
        user_answer: The user's submitted answer text.
    """

    quiz_id: str = Field(..., description="ID of the quiz being answered")
    user_answer: str = Field(
        ..., min_length=1, max_length=500, description="User's submitted answer"
    )


class AnswerValidation(BaseModel):
    """Result of answer validation.

    Attributes:
        is_correct: Whether the answer matches the correct answer.
        message: Human-readable result message.
        correct_answer: The correct answer (included when incorrect).
    """

    is_correct: bool = Field(..., description="True if answer is correct")
    message: str = Field(..., description="Result message")
    correct_answer: Optional[str] = Field(
        None, description="Correct answer (when incorrect)"
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "is_correct": True,
                    "message": "Correct! The answer is water.",
                    "correct_answer": None,
                },
                {
                    "is_correct": False,
                    "message": "Incorrect. Try again!",
                    "correct_answer": "water",
                },
            ]
        }
    }


class ErrorResponse(BaseModel):
    """Standardized error response.

    Attributes:
        status: HTTP status code.
        error: Error identifier (e.g., invalid_input, not_found).
        message: Human-readable error message.
        timestamp: ISO 8601 timestamp when error occurred.
    """

    status: int = Field(..., description="HTTP status code")
    error: str = Field(..., description="Error code identifier")
    message: str = Field(..., description="Human-readable error message")
    timestamp: str = Field(
        default_factory=lambda: datetime.utcnow().isoformat(),
        description="Timestamp in ISO 8601 format",
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "status": 400,
                    "error": "invalid_input",
                    "message": "Answer cannot be empty",
                    "timestamp": "2026-05-26T10:30:00",
                }
            ]
        }
    }
