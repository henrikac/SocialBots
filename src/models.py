"""Contains all database related stuff

Note: peewee doesn't support type hints, therefore
running i.e. 'mypy' on this file will cause lots errors

Created: 2019
Author: Henrik A. Christensen
"""

from datetime import datetime
from typing import Dict, Union

from peewee import *
from playhouse.shortcuts import model_to_dict


db = SqliteDatabase('SocialBots.db')


def open_db() -> None:
    """Opens the database connection"""
    db.connect()


def close_db() -> None:
    """Closes the database connection"""
    db.close()


def create_tables() -> None:
    """Creates the database tables"""
    with db:
        db.create_tables([InstaPhoto], safe=True)


def add_instaphoto(details: Dict) -> None:
    """Adds a single InstaPhoto to the database"""
    try:
        InstaPhoto.create(**details)
    except IntegrityError:
        pass


def get_instaphoto(url: str) -> Union[Dict, None]:
    """Gets an InstaPhoto from the database by its url
    Returns None if there is no InstaPhoto with the given url
    """
    instaphoto = InstaPhoto.get_or_none(InstaPhoto.url == url)

    if instaphoto:
        return model_to_dict(instaphoto)

    return instaphoto


class BaseModel(Model):
    class Meta:
        database = db


class InstaPhoto(BaseModel):
    url = CharField(unique=True)
    author = CharField()
    visited_at = DateTimeField(default=datetime.now)

