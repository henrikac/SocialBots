"""SocialBots

A collection on different social media bots

Created: 2019
Author: Henrik A. Christensen
"""

from models import close_db, open_db
from socialmediabot import SocialMediaBot


if __name__ == '__main__':
    open_db()
    smb = SocialMediaBot()
    smb.run()
    close_db()

