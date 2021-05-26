from random import randint
from brain_games.games import Round


def show_rules() -> None:
    print('Answer "yes" if the number is even, otherwise answer "no".')


def is_even(number: int) -> bool:
    return number % 2 == 0


def get_round() -> Round:
    upper_bound = 100

    number = randint(0, upper_bound)
    answer = "yes" if is_even(number) else "no"
    return Round(question=str(number), answer=answer)
