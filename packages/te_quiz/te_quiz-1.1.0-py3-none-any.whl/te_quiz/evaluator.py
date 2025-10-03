"""Core evaluation logic for te_quiz package."""

from typing import Dict, Union, List, Tuple
from .constants import (
    EXTROVERT_INTROVERT_QUESTIONS,
    THINKER_FEELER_QUESTIONS,
    ALL_QUESTIONS,
    VALID_COMMUNICATION_ANSWERS
)
from .exceptions import InvalidAnswerError, InvalidQuestionError


def validate_answers(answers: Dict[int, str]) -> None:
    """Validate that all required answers are present and valid."""
    # Check if all 10 questions are answered
    if set(answers.keys()) != ALL_QUESTIONS:
        missing = ALL_QUESTIONS - set(answers.keys())
        extra = set(answers.keys()) - ALL_QUESTIONS
        if missing:
            raise InvalidQuestionError(
                f"Missing answers for questions: {sorted(missing)}"
            )
        if extra:
            raise InvalidQuestionError(
                f"Invalid question IDs: {sorted(extra)}"
            )

    # Validate communication style answers
    for q_id in ALL_QUESTIONS:
        if answers[q_id] not in VALID_COMMUNICATION_ANSWERS:
            raise InvalidAnswerError(
                f"Question {q_id}: answer must be 'a' or 'b', "
                f"got '{answers[q_id]}'"
            )


def calculate_communication_style(answers: Dict[int, str]) -> Dict[str, float]:
    """Calculate communication style percentages."""
    extrovert_count = 0
    introvert_count = 0
    thinker_count = 0
    feeler_count = 0

    # Count extrovert/introvert answers
    for q_id in EXTROVERT_INTROVERT_QUESTIONS:
        if answers[q_id] == 'a':
            extrovert_count += 1
        else:  # 'b'
            introvert_count += 1

    # Count thinker/feeler answers
    for q_id in THINKER_FEELER_QUESTIONS:
        if answers[q_id] == 'a':
            thinker_count += 1
        else:  # 'b'
            feeler_count += 1

    # Calculate percentages using the provided formulas
    # Convert to percentages by dividing by 10 (total comm style questions)
    red = (extrovert_count + thinker_count) / 20.0    # /2 then /10 = /20
    yellow = (extrovert_count + feeler_count) / 20.0
    blue = (introvert_count + thinker_count) / 20.0
    green = (introvert_count + feeler_count) / 20.0

    return {
        'red': round(red, 2),
        'yellow': round(yellow, 2),
        'blue': round(blue, 2),
        'green': round(green, 2)
    }


def calculate_stress_journey(comm_style: Dict[str, float]) -> Dict[int, str]:
    """
    Calculate stress journey based on communication style percentages.

    Arranges colors by descending percentage and maps stress levels 1-10
    to corresponding colors based on their ratios.

    Uses dynamic cyclical tie-breaking rule starting from dominant color:
    Blue → Red → Yellow → Green → Blue

    Args:
        comm_style: Dictionary with color percentages (red, yellow, blue, green)

    Returns:
        Dictionary mapping stress levels (1-10) to colors
    """
    # Define base cycle
    base_cycle = ['blue', 'red', 'yellow', 'green']

    # Find dominant color (highest percentage)
    dominant_color = max(comm_style.keys(), key=lambda k: comm_style[k])

    # Create cyclical order starting from dominant color
    dominant_index = base_cycle.index(dominant_color)
    cyclical_order = base_cycle[dominant_index:] + base_cycle[:dominant_index]

    # Convert percentages to ratios out of 10
    color_ratios = [(color, comm_style[color] * 10) for color in comm_style]

    # Sort by ratio descending, then by cyclical order for ties
    def sort_key(item: Tuple[str, float]) -> Tuple[float, int]:
        color, ratio = item
        cyclical_index = cyclical_order.index(color)
        return (-ratio, cyclical_index)  # Negative for descending

    sorted_colors = sorted(color_ratios, key=sort_key)

    # Build stress journey mapping
    stress_journey = {}
    current_level = 1

    for i, (color, ratio) in enumerate(sorted_colors):
        # Calculate levels for this color
        if i == len(sorted_colors) - 1:  # Last color gets remaining levels
            level_count = 10 - current_level + 1
        else:
            level_count = round(ratio)

        # Assign stress levels to this color
        for _ in range(level_count):
            if current_level <= 10:
                stress_journey[current_level] = color
                current_level += 1

    return stress_journey


def evaluate_quiz(
    answers: Dict[int, str]
) -> Dict[str, Union[Dict[str, float], Dict[int, str]]]:
    """
    Evaluate quiz results and return communication style and stress journey.

    Args:
        answers: Dictionary mapping question IDs (1,3,5,7,9,10,11,12,13,14) to answers.
                All questions use 'a' or 'b' answers.

    Returns:
        Dictionary with:
        - 'communication_style': color percentages
        - 'stress_journey': mapping of stress levels (1-10) to colors

    Raises:
        InvalidQuestionError: If question IDs are invalid or missing
        InvalidAnswerError: If answers are in wrong format
    """
    # Validate input
    validate_answers(answers)

    # Calculate communication style
    comm_style = calculate_communication_style(answers)

    # Calculate stress journey
    stress_journey = calculate_stress_journey(comm_style)

    return {
        'communication_style': comm_style,
        'stress_journey': stress_journey
    }