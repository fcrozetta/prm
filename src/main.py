import os
from repositories.graph.gremlin import GremlinDb

x = GremlinDb("ws://localhost:8182/gremlin")
print(os.getenv("IS_ENV_LOADED"))
