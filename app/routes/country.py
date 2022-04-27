from typing import Any
from fastapi import Depends
from fastapi.routing import APIRouter
from neo4j import Session

from ..graph_repository import crud_country
from ..graph_repository.database import get_db
from ..schemas import neo4j_schemas

router = APIRouter(prefix="/country", tags=["location"])


@router.get("/", response_model=list[neo4j_schemas.Country])
def get_all_countries(db: Session = Depends(get_db)):
    return crud_country.get_all_countries(db)


@router.get("/{country_id}", response_model=neo4j_schemas.Country)
def get_country(country_id: int, db: Session = Depends(get_db)):
    return crud_country.get_country(db, country_id)


@router.post("/", response_model=neo4j_schemas.Country)
def create_country(country: neo4j_schemas.BaseCountry, db: Session = Depends(get_db)):
    return crud_country.create_country(db, country)
