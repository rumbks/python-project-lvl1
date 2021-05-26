from random import choice, randint
from operator import add, sub, mul
from brain_games.games import Round


def show_rules() -> None:
    print('What is the result of the expression?')


def get_round() -> Round:
    UPPER_BOUND = 100

    OPERATIONS = {"+": add, "-": sub, "*": mul}
    left_number, right_number = randint(1, UPPER_BOUND), randint(1, UPPER_BOUND)
    operation_symbol = choice(tuple(OPERATIONS.keys()))

    question = " ".join(map(str, (left_number, operation_symbol, right_number)))
    result = OPERATIONS[operation_symbol](left_number, right_number)

    return Round(question=question, answer=str(result))
