from random import randint

from brain_games.game import Round


def find_gcd(a: int, b: int):
    if a < b:
        a, b = b, a
    if a == 0 or b == 0:
        return a or b

    return find_gcd(b, a % b)


def show_rules() -> None:
    print('Find the greatest common divisor of given numbers.')


def get_round() -> Round:
    upper_bound = 100

    left_number, right_number = randint(1, upper_bound), randint(1, upper_bound)

    question = " ".join(map(str, (left_number, right_number)))
    gcd = find_gcd(left_number, right_number)

    return Round(question=question, answer=str(gcd))
