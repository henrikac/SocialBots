from getpass import getpass

from instabot import InstaBot


if __name__ == '__main__':
    topics = []
    username = input('Username: ')
    password = getpass()

    while True:
        topic = input('Topic: ')

        if topic.lower() == 'q':
            break

        topics.append(topic)

    bot = InstaBot(username, password)
    bot.login()
    bot.like_photos(topics)

