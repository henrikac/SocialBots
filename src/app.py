"""SocialBots

A collection on different social media bots

Created: 2019
Author: Henrik A. Christensen
"""

from getpass import getpass
import os
from typing import List

from instabot import InstaBot
import models


def clear_terminal() -> None:
    """Clears the terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')


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
    print('(Enter \'q\' when you\'re done)')

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


if __name__ == '__main__':
    models.open_db()
    clear_terminal()
    username = input('Username: ')
    password = getpass()
    topics = prompt_for_topics()

    bot = InstaBot(username, password)
    bot.login()
    bot.like_photos(topics)
    bot.quit()
    models.close_db()

