#!/usr/bin/env python
from brain_games.cli import welcome_user, get_user_name, welcome


def main():
    welcome()
    name = get_user_name()
    welcome_user(name)


if __name__ == '__main__':
    main()
