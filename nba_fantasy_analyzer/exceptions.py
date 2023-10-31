from dataclasses import dataclass

from nba_fantasy_analyzer.mixins.exceptions import ExceptionMixin


@dataclass
class UserNotFound(ExceptionMixin):
    _message: str = ("Could not find any user with the provide data.")


@dataclass
class UserAlreadyPresent(ExceptionMixin):
    _message: str = ("User already has posted cities.")


@dataclass
class DatabaseError(ExceptionMixin):
    _message: str = ("Something went wrong while connecting to the database.")
    details: str = ""


@dataclass
class ItemNotFound(ExceptionMixin):
    _message: str = ("Item not found.")
    details: str = ""
