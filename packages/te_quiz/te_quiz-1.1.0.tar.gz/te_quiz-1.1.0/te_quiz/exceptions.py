"""Custom exceptions for te_quiz package."""


class InvalidAnswerError(ValueError):
    """Raised when an answer is invalid or missing."""
    pass


class InvalidQuestionError(ValueError):
    """Raised when a question ID is invalid."""
    pass