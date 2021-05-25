from random import choice, randint
from operator import add, sub, mul
from brain_games.game import Round


def show_rules() -> None:
    print('What is the result of the expression?')


def get_round() -> Round:
    upper_bound = 100

    operations = {"+": add, "-": sub, "*": mul}
    left_number, right_number = randint(1, upper_bound), randint(1, upper_bound)
    operation_symbol = choice(tuple(operations.keys()))

    question = " ".join(map(str, (left_number, operation_symbol, right_number)))
    result = operations[operation_symbol](left_number, right_number)

    return Round(question=question, answer=str(result))
