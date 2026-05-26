"""Quiz Service business logic layer.

Provides stateless functions for retrieving quizzes and validating answers.
All operations are deterministic and thread-safe.
"""

import random
from typing import Optional

from backend.app.models import AnswerValidation, Quiz, Hint
from backend.app.quiz_data import QUIZ_POOLS


class QuizService:
    """Service for managing quiz operations.

    All methods are static to ensure stateless design. Each request
    operates independently without side effects.
    """

    VALID_CATEGORIES = ["science", "history", "celebrity"]

    @staticmethod
    def get_quiz(category: str) -> Optional[Quiz]:
        """Retrieve a random quiz from the specified category.

        Args:
            category: Quiz category identifier (science, history, celebrity).

        Returns:
            Quiz object with id, category, hints (ordered 1-5), and answer.
            Returns None if category is invalid.

        Raises:
            ValueError: If category is not supported.

        Example:
            >>> quiz = QuizService.get_quiz("science")
            >>> quiz.category
            'science'
            >>> len(quiz.hints)
            5
        """
        if category not in QuizService.VALID_CATEGORIES:
            raise ValueError(
                f"Invalid category: {category}. Must be one of {QuizService.VALID_CATEGORIES}"
            )

        # Get random quiz from category pool
        pool = QUIZ_POOLS.get(category, [])
        if not pool:
            raise ValueError(f"No quizzes available for category: {category}")

        quiz_data = random.choice(pool)

        # Convert hints to Hint objects with proper ordering
        hints = [
            Hint(order=hint["order"], text=hint["text"]) for hint in quiz_data["hints"]
        ]
        hints.sort(key=lambda h: h.order)

        return Quiz(
            id=quiz_data["id"],
            category=quiz_data["category"],
            hints=hints,
            answer=quiz_data["answer"],
        )

    @staticmethod
    def validate_answer(quiz_id: str, user_answer: str) -> AnswerValidation:
        """Validate a user's answer against the correct answer for a quiz.

        Performs case-insensitive and whitespace-trimmed comparison.

        Args:
            quiz_id: ID of the quiz being answered.
            user_answer: The user's submitted answer text.

        Returns:
            AnswerValidation object with is_correct, message, and optional correct_answer.

        Example:
            >>> result = QuizService.validate_answer("science_001", "Water")
            >>> result.is_correct
            True
            >>> result.message
            'Correct! The answer is water.'
        """
        # Find the quiz in all pools
        correct_answer = None
        for category_pool in QUIZ_POOLS.values():
            for quiz in category_pool:
                if quiz["id"] == quiz_id:
                    correct_answer = quiz["answer"]
                    break
            if correct_answer:
                break

        if not correct_answer:
            return AnswerValidation(
                is_correct=False,
                message="Quiz not found.",
                correct_answer=None,
            )

        # Normalize both answers: lowercase and strip whitespace
        normalized_user_answer = user_answer.strip().lower()
        normalized_correct_answer = correct_answer.strip().lower()

        if normalized_user_answer == normalized_correct_answer:
            return AnswerValidation(
                is_correct=True,
                message=f"Correct! The answer is {correct_answer}.",
                correct_answer=None,
            )
        else:
            return AnswerValidation(
                is_correct=False,
                message="Incorrect. Try again!",
                correct_answer=correct_answer,
            )
