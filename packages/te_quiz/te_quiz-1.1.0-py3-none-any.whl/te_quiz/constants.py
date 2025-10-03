"""Constants for te_quiz package including question mappings and keys."""

# Communication style questions (10 total)
# Questions 1, 2, 3, 4, 7: a=extrovert, b=introvert
EXTROVERT_INTROVERT_QUESTIONS = {1, 2, 3, 4, 7}

# Questions 5, 6, 8, 9, 10: a=thinker, b=feeler
THINKER_FEELER_QUESTIONS = {5, 6, 8, 9, 10}

# All valid question IDs (communication style questions only)
ALL_QUESTIONS = EXTROVERT_INTROVERT_QUESTIONS | THINKER_FEELER_QUESTIONS

# Valid answers for communication style questions
VALID_COMMUNICATION_ANSWERS = {'a', 'b'}
