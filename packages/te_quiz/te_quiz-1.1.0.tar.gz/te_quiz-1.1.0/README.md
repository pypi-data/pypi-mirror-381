# te_quiz

A Python package for evaluating quiz results to determine communication styles and stress journey mapping.

## Features

- **Communication Style Analysis**: Calculates percentages for four communication styles (Red, Yellow, Blue, Green)
- **Stress Journey Mapping**: Maps stress levels 1-10 to dominant communication colors based on percentages
- **Flexible Input**: Handles questions in any order
- **Simple API**: Single function interface


## Installation

```bash
pip install te_quiz
```

## Quick Start

```python
from te_quiz import evaluate_quiz

# Define quiz answers (questions can be in any order)
answers = {
    1: 'a',   # All questions use 'a' or 'b' answers
    2: 'b',
    3: 'a',
    4: 'b',
    5: 'a',
    6: 'b',
    7: 'a',
    8: 'a',
    9: 'a',
    10: 'b'
}

# Evaluate the quiz
result = evaluate_quiz(answers)

print(result)
# Output:
# {
#     'communication_style': {
#         'red': 0.35,
#         'yellow': 0.25,
#         'blue': 0.25,
#         'green': 0.15
#     },
#     'stress_journey': {
#         1: 'red', 2: 'red', 3: 'red', 4: 'red',
#         5: 'yellow', 6: 'yellow', 7: 'blue',
#         8: 'blue', 9: 'green', 10: 'green'
#     }
# }
```

## API Reference

### `evaluate_quiz(answers: Dict[int, str]) -> Dict`

Evaluates complete quiz results.

**Parameters:**
- `answers`: Dictionary mapping question IDs (1-10) to answers

**Returns:**
- Dictionary with:
  - `communication_style`: Color percentages (red, yellow, blue, green)
  - `stress_journey`: Mapping of stress levels (1-10) to colors

**Raises:**
- `InvalidQuestionError`: Missing or invalid question IDs
- `InvalidAnswerError`: Invalid answer format

## License

Not to be distributed.