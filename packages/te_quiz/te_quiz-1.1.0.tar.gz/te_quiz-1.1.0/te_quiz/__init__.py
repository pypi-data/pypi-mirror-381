"""
te_quiz: A Python package for evaluating quiz results and communication styles.

This package evaluates quiz results to determine:
1. Communication style percentages (red, yellow, blue, green)
2. Self-Deceptive (SD) positivity level (low, moderate, high)
"""

from .evaluator import evaluate_quiz
from .exceptions import InvalidAnswerError, InvalidQuestionError

__version__ = "1.0.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"
__description__ = "A simple package for evaluating quiz results and communication styles"

# Export main API
__all__ = ['evaluate_quiz', 'InvalidAnswerError', 'InvalidQuestionError']