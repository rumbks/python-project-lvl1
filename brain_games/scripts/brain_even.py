#!/usr/bin/env python
from brain_games.cli import welcome_user, get_user_name, welcome
from brain_games.game import even as game

ROUNDS = 3


def main():
    welcome()
    name = get_user_name()
    welcome_user(name)
    game.show_rules()
    for _ in range(ROUNDS):
        try:
            game.play()
        except game.WrongAnswer:
            game.show_ending(name)
            return
    game.show_congratulations(name)


if __name__ == '__main__':
    main()
