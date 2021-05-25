import prompt


def welcome() -> None:
    print("Welcome to the Brain Games!")


def welcome_user() -> None:
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
