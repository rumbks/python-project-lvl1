from types import ModuleType
from typing import NamedTuple
import prompt

ROUNDS = 3

Round = NamedTuple("Round", [("question", str), ("answer", str)])


class WrongAnswer(Exception):
    pass


def show_congratulations(name: str) -> None:
    print(f"Congratulations, {name}!")


def show_ending(name: str) -> None:
    print(f"Let's try again, {name}!")


def show_round_question(round: Round) -> None:
    print(f"Question: {round.question}")


def get_answer() -> str:
    return prompt.string("Your answer: ")


def show_correct_answer(user_answer: str, round: Round) -> None:
    print(f"'{user_answer}' is wrong answer ;(. "
          f"Correct answer was '{round.answer}'.")


def show_round_passed():
    print("Correct!")


def play(game: ModuleType):
    round = game.get_round()
    show_round_question(round)
    user_answer = get_answer()
    if user_answer != round.answer:
        show_correct_answer(user_answer, round)
        raise WrongAnswer
    show_round_passed()
