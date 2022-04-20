from neo4j import GraphDatabase
import app.config as cfg

driver = GraphDatabase.driver(cfg.NEO4J_URI, auth=(cfg.NEO4J_USER, cfg.NEO4J_PASSWORD))


def get_db():
    try:
        yield driver.session(database=cfg.NEO4J_DB)
    finally:
        driver.close()
