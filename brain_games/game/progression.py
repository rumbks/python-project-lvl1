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
    initial_term_upper_bound = 30
    initial_term = randint(0, initial_term_upper_bound)

    length_lower_bound, length_upper_bound = 5, 15
    progression_length = randint(length_lower_bound, length_upper_bound)

    difference_lower_bound, difference_upper_bound = 1, 10
    progression_difference = randint(
        difference_lower_bound, difference_upper_bound
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
