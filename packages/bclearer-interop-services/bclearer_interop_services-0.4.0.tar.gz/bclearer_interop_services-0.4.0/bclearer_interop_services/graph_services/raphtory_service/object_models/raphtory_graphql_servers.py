"""Raphtory GraphQL server utilities."""

from __future__ import annotations

from raphtory import graphql


class RaphtoryGraphQLServers:
    """Manage Raphtory GraphQL servers."""

    def __init__(self) -> None:
        self._server: graphql.RunningGraphServer | None = None

    def start_server(self, graph_dir: str, port: int = 1736) -> None:
        """Start a GraphQL server.

        Raises:
            RuntimeError: If server already running or
                startup fails.

        """
        if self._server is not None:
            raise RuntimeError("Server already running")
        try:
            server = graphql.GraphServer(graph_dir)
            self._server = server.start(port=port)
        except Exception as exc:  # pragma: no cover
            raise RuntimeError(
                "Failed to start GraphQL server",
            ) from exc

    def get_client(self) -> graphql.RaphtoryClient:
        """Return a GraphQL client."""
        if self._server is None:
            raise RuntimeError("Server not running")
        return self._server.get_client()

    def execute_query(
        self,
        query: str,
        variables: dict[str, object] | None = None,
    ) -> object:
        """Execute a GraphQL query."""
        client = self.get_client()
        return client.query(query, variables)
