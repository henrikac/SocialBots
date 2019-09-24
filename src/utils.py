import os


def clear_terminal() -> None:
    """Clears the terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')


def prompt_for_int(prompt_msg: str) -> int:
    """Prompts the user for an integer"""
    while True:
        try:
            user_input = int(input(prompt_msg))
        except ValueError:
            print('Please enter an integer')
        else:
            return user_input

