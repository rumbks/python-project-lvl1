#!/usr/bin/env python
from brain_games.game import calc as calc_game
from brain_games.scripts import show_game_cli


def main():
    show_game_cli(calc_game)


if __name__ == '__main__':
    main()
