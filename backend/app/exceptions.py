"""Custom exceptions for Quiz Service.

Provides domain-specific exceptions for error handling and standardized responses.
"""


class QuizError(Exception):
    """Base exception for quiz service errors.

    Attributes:
        message: Human-readable error message.
        status_code: HTTP status code for the error.
        error_code: Machine-readable error identifier.
    """

    def __init__(
        self, message: str, status_code: int = 400, error_code: str = "quiz_error"
    ):
        """Initialize QuizError.

        Args:
            message: Error message.
            status_code: HTTP status code (default: 400).
            error_code: Error code identifier (default: quiz_error).
        """
        self.message = message
        self.status_code = status_code
        self.error_code = error_code
        super().__init__(self.message)


class InvalidCategoryError(QuizError):
    """Raised when an invalid quiz category is requested."""

    def __init__(self, category: str, valid_categories: list):
        """Initialize InvalidCategoryError.

        Args:
            category: The invalid category provided.
            valid_categories: List of valid category names.
        """
        message = f"Invalid category: '{category}'. Must be one of {valid_categories}"
        super().__init__(message, status_code=400, error_code="invalid_category")


class InvalidInputError(QuizError):
    """Raised when input validation fails."""

    def __init__(self, field: str, reason: str):
        """Initialize InvalidInputError.

        Args:
            field: The field that failed validation.
            reason: Reason for validation failure.
        """
        message = f"Invalid {field}: {reason}"
        super().__init__(message, status_code=400, error_code="invalid_input")


class QuizNotFoundError(QuizError):
    """Raised when a requested quiz is not found."""

    def __init__(self, quiz_id: str):
        """Initialize QuizNotFoundError.

        Args:
            quiz_id: ID of the quiz that was not found.
        """
        message = f"Quiz not found: {quiz_id}"
        super().__init__(message, status_code=404, error_code="not_found")
