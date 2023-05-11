import datetime as dt
from pydantic import BaseModel


class Person(BaseModel):
    name: str
    aliases: list[str] | None
    birthdate: dt.date | None


class Knows(BaseModel):
    since: dt.date | None
