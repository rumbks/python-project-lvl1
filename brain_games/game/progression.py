from random import randint
from typing import List

from brain_games.game import Round


def show_rules() -> None:
    print('What number is missing in the progression?')


def get_progression(
    initial_term: int, difference: int, length: int
) -> List[int]:
    progression = []
    item = initial_term
    for _ in range(length):
        progression.append(item)
        item += difference
    return progression


def get_representation_with_hidden_item(
    progression: List[int], hidden_item_index: int
) -> str:
    items_strings = [str(item) for item in progression]
    items_strings[hidden_item_index] = ".."
    return " ".join(items_strings)


def get_round() -> Round:
    INITIAL_TERM_UPPER_BOUND = 30
    initial_term = randint(0, INITIAL_TERM_UPPER_BOUND)

    LENGTH_LOWER_BOUND, LENGTH_UPPER_BOUND = 5, 15
    progression_length = randint(LENGTH_LOWER_BOUND, LENGTH_UPPER_BOUND)

    DIFFERENCE_LOWER_BOUND, DIFFERENCE_UPPER_BOUND = 1, 10
    progression_difference = randint(
        DIFFERENCE_LOWER_BOUND, DIFFERENCE_UPPER_BOUND
    )

    progression = get_progression(
        initial_term, progression_difference, progression_length
    )
    hidden_item_index = randint(0, progression_length - 1)

    question = get_representation_with_hidden_item(
        progression, hidden_item_index
    )
    hidden_item = progression[hidden_item_index]

    return Round(question=question, answer=str(hidden_item))
