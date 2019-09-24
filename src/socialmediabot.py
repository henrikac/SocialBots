from getpass import getpass
from typing import Tuple

from instabot import InstaBot
from utils import clear_terminal, prompt_for_int


class SocialMediaBot:
    menu = [
        (1, 'Instagram Bot'),
        (0, 'Exit')
    ]

    def __display_title(self, title: str) -> None:
        """Prints a title"""
        print('=' * len(title))
        print(title)
        print('=' * len(title), end='\n\n')

    def __display_menu(self) -> None:
        """Prints the different menu options"""
        for item in self.menu:
            print(f'{item[0]}) {item[1]}')

    def prompt_credentials(self) -> Tuple[str, str]:
        """Prompts the user for credentials
        Returns a tuple containing username, password
        """
        username = input('Username: ')
        password = getpass()

        return (username, password)

    def quit(self) -> None:
        """Exits the program"""
        raise SystemExit

    def instabot(self) -> None:
        """Run the Instagram Bot"""
        clear_terminal()
        self.__display_title('Instagram Bot')
        username, password = self.prompt_credentials()
        bot = InstaBot(username, password)
        topics = bot.prompt_for_topics()
        bot.login()
        bot.like_photos(topics)
        bot.quit()

    def run(self) -> None:
        """Run the Social Media Bots program"""
        clear_terminal()
        self.__display_title('Social Media Bots')
        self.__display_menu()

        while True:
            menu_max = len(self.menu) - 1

            user_choice = prompt_for_int('\n> ')
            if user_choice < 0 or user_choice > menu_max:
                print(f'Please only enter a number between 0 and {menu_max}')
                continue

            if user_choice == 0:
                self.quit()
            elif user_choice == 1:
                self.instabot()
                clear_terminal()
                self.__display_title('Social Media Bots')
                self.__display_menu()

