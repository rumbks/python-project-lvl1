from random import randint
from typing import NamedTuple
import prompt


class WrongAnswer(Exception):
    pass


Riddle = NamedTuple("Riddle", [("question", int), ("answer", str)])


def show_congratulations(name: str) -> None:
    print(f"Congratulations, {name}!")


def show_ending(name: str) -> None:
    print(f"Let's try again, {name}!")


def show_rules() -> None:
    print('Answer "yes" if the number is even, otherwise answer "no".')


def is_even(number: int) -> bool:
    return number % 2 == 0


def get_riddle() -> Riddle:
    upper_bound = 100

    number = randint(0, upper_bound)
    answer = "yes" if is_even(number) else "no"
    return Riddle(question=number, answer=answer)


def show_riddle(riddle: Riddle) -> None:
    print(f"Question: {riddle.question}")


def get_answer() -> str:
    return prompt.string("Your answer: ")


def show_correct_answer(user_answer: str, riddle: Riddle) -> None:
    print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{riddle.answer}'.")


def show_riddle_solved():
    print("Correct!")


def play():
    riddle = get_riddle()
    show_riddle(riddle)
    user_answer = get_answer()
    if user_answer != riddle.answer:
        show_correct_answer(user_answer, riddle)
        raise WrongAnswer
    show_riddle_solved()
