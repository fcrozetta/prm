from typing import Any
from fastapi import Depends
from fastapi.routing import APIRouter
from neo4j import Session

from app.graph_repository.database import get_db
import app.graph_repository.crud as crud
import app.schemas.neo4j_schemas as neo4j_schemas


router = APIRouter(prefix="/person", tags=["person"])


@router.get("/")
def get_all_people(db: Session = Depends(get_db)):
    return crud.get_all_people(db)


@router.post("/", response_model=list[neo4j_schemas.Person])
def create_person(person: neo4j_schemas.BasePerson, db: Session = Depends(get_db)):
    return crud.create_person(db, person)


@router.get("/{person_id}", response_model=neo4j_schemas.Person)
def get_person(person_id: int, db: Session = Depends(get_db)):
    return crud.get_person(db, person_id)


@router.get("/{person_id}/{relationship}", response_model=Any)
def related_to(person_id: int, relationship: str, db: Session = Depends(get_db)):
    return crud.get_relationship_nodes(db, person_id, relationship)


@router.post("/{person_id}/{relationship}/{id_to_know}")
def link(
    person_id: int,
    id_to_know: int,
    relationship: str,
    parameters: dict = None,
    db: Session = Depends(get_db),
):
    return crud.link(db, person_id, id_to_know, relationship, parameters)
