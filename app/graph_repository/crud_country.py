from typing import Any
from neo4j import Session
from ..schemas import neo4j_schemas


def get_country(db: Session, country_id: int) -> neo4j_schemas.Country:
    command = db.run(f"match (a:Country) where id(a) = {country_id} return a")
    result = command.value()[0]
    return neo4j_schemas.Country(**result._properties, _id=result.id)


def get_all_countries(db: Session) -> list[neo4j_schemas.Country]:
    command = db.run("match (a:Country) return a")
    result = command.values()[0]
    return [neo4j_schemas.Country(**r._properties, _id=r.id) for r in result]


def create_country(
    db: Session, country: neo4j_schemas.BaseCountry
) -> neo4j_schemas.Country:
    command = db.run("CREATE (a:Country $params) return a", params=country.dict())
    result = command.value()[0]
    return neo4j_schemas.Country(**result._properties, _id=result.id)
