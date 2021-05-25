import prompt


def welcome() -> None:
    print("Welcome to the Brain Games!")


def get_user_name() -> str:
    return prompt.string('May I have your name? ')


def welcome_user(name: str) -> None:
    print(f"Hello, {name}!")
