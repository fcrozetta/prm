from pydantic import BaseModel, Field

# * Composition models
class _ID(BaseModel):
    id: int = Field(..., alias="_id")


# * Node models


class GenericNode(_ID):
    labels: set
    properties: dict | None


class BasePerson(BaseModel):
    first_name: str | None
    middle_name: str | None
    last_name: str | None
    nicknames: list[str] | None
    emails: list[str] | None
    phones: list[str] | None
    is_alive: bool | None
    birthdate: str | None
    deathdate: str | None


class Person(BasePerson, _ID):
    pass
