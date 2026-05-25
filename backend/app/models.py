"""
Shared Quiz Data Model
"""

from typing import List


class QuizData:
    """Model for quiz questions with hints and answers"""

    def __init__(self, hints: List[str], answer: str):
        self.hints = hints
        self.answer = answer

    def to_dict(self):
        return {"hints": self.hints, "answer": self.answer}
