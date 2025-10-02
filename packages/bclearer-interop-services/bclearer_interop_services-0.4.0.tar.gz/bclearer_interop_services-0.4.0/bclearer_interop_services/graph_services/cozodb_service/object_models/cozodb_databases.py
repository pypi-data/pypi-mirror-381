from .cozodb_connections import CozoDbConnections
from .cozodb_sessions import CozoDbSessions


class CozoDbDatabases:
    def __init__(
        self,
        uri: str | None = None,
        external_connection: CozoDbConnections | None = None,
    ):
        if external_connection is None:
            self.connection = CozoDbConnections(
                uri=uri or "mem://",
            )
        else:
            self.connection = external_connection

    def get_new_session(self):
        return CozoDbSessions(
            connection=self.connection,
        )

    def run_query(
        self,
        query: str,
        parameters: dict | None = None,
    ):
        session = self.get_new_session()
        return session.run(
            query,
            parameters,
        )

    def close(self):
        self.connection.close()

    def __exit__(
        self,
        exc_type,
        exc_val,
        exc_tb,
    ):
        self.close()
