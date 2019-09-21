from datetime import datetime

from peewee import *


db = SqliteDatabase('SocialBots.db')


def create_tables():
    """Creates the database tables"""
    with db:
        db.create_tables([InstaPhoto], safe=True)


class BaseModel(Model):
    class Meta:
        database = db


class InstaPhoto(BaseModel):
    url = CharField(unique=True)
    author = CharField()
    visited_at = DateTimeField(default=datetime.now)

