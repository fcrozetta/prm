from typing import Any
from neo4j import Session
from ..schemas import neo4j_schemas


def link(db: Session, node_from_id, node_to_id, label: str, parameters: dict = None):
    db.run(
        "match (a), (b) where id(a) = $node_from_id and id(b) = $node_to_id create (a)-[:"
        + label
        + " $params]->(b)",
        {
            "node_from_id": node_from_id,
            "node_to_id": node_to_id,
            "params": parameters,
        },
    )
    return True


def get_all_people(db: Session) -> list[neo4j_schemas.Person]:
    command = db.run("match (a:Person) return a")
    result = command.value()
    return [
        neo4j_schemas.Person(**person._properties, _id=person.id) for person in result
    ]


def create_person(
    db: Session, person: neo4j_schemas.BasePerson
) -> neo4j_schemas.Person:
    command = db.run("create (a:Person $params) return a", params=person.dict())
    result = command.value()[0]
    return neo4j_schemas.Person(**result._properties, _id=result.id)


def get_person(db: Session, person_id: int) -> neo4j_schemas.Person:
    command = db.run(f"match (a:Person) where id(a) = {person_id} return a")
    result = command.value()[0]
    return neo4j_schemas.Person(**result._properties, _id=result.id)


def get_relationship_nodes(db: Session, person_id: int, label: str) -> list[Any]:
    command = db.run(
        f"match (a:Person)-[r:{label}]->(b) where id(a) = {person_id} return b"
    )
    result = command.value()
    return [
        neo4j_schemas.GenericNode(
            labels=relationship._labels,
            properties=relationship._properties,
            _id=relationship.id,
        )
        for relationship in result
    ]
