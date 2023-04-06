from gremlin_python.process.anonymous_traversal import traversal, GraphTraversalSource
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection


class GremlinDb:
    g: GraphTraversalSource

    def __init__(self, connection_string="ws://localhost:8182/gremlin") -> None:
        self.g = traversal().withRemote(DriverRemoteConnection(connection_string, "g"))
        self.__is_conected__()

    def __is_conected__(self) -> bool | Exception:
        """Tries to get a vertex to check connection
        TODO: Find a better way to check the connection"""
        try:
            self.g.V(0).to_list()
        except Exception as e:
            raise e
        return True
