from types import ModuleType

from brain_games.cli import welcome_user, get_user_name, welcome
from brain_games.game import play, WrongAnswer
from brain_games.game import ROUNDS, show_ending, show_congratulations


def show_game_cli(game: ModuleType):
    welcome()
    name = get_user_name()
    welcome_user(name)
    game.show_rules()
    for _ in range(ROUNDS):
        try:
            play(game)
        except WrongAnswer:
            show_ending(name)
            return
    show_congratulations(name)
