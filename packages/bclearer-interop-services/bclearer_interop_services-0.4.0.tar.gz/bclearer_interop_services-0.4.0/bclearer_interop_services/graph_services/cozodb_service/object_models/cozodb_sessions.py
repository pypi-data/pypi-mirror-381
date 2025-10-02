from .cozodb_connections import CozoDbConnections


class CozoDbSessions:
    def __init__(
        self,
        connection: CozoDbConnections,
    ):
        self.connection = connection

    def run(
        self,
        query: str,
        parameters: dict | None = None,
    ):
        client = self.connection.get_client()
        return client.run(
            query,
            parameters or {},
        )
