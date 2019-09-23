import os
from typing import List


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

def is_valid_topic(topic: str) -> None:
    """Checks if a topic is valid"""
    if len(topic) < 1:
        raise ValueError('A topic has to be at least 1 character long')
    elif not topic.isalpha():
        raise ValueError('A topic can only contain alphabetic characters')

def prompt_for_topics() -> List[str]:
    """Prompts the user for topics to search for
    Returns a list of topics entered by the user
    """
    topics = []

    print('\nEnter topics to search for:')
    print('(Enter \'q\' when you\'re done)\n')

    while True:
        topic = input('Topic: ')

        if topic.lower() == 'q':
            break

        try:
            is_valid_topic(topic)
        except ValueError as err:
            print(f'Error: {err}')
            continue

        if topic not in topics:
            topics.append(topic)

    return topics

