from math import sqrt
from random import randint

from brain_games.game import Round


def divides(a: int, b: int) -> bool:
    return a % b == 0


def is_prime(n) -> bool:
    for i in range(2, int(sqrt(n)) + 1):
        if divides(n, i):
            return False
    return True


def show_rules() -> None:
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def get_round() -> Round:
    UPPER_BOUND = 100

    number = randint(2, UPPER_BOUND)
    answer = "yes" if is_prime(number) else "no"

    return Round(question=str(number), answer=answer)
