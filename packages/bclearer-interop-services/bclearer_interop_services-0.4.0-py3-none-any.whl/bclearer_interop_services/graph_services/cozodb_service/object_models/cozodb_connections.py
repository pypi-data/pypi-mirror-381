try:
    import pycozo as cozo
except ModuleNotFoundError:  # pragma: no cover - handled in tests
    cozo = None


class CozoDbConnections:
    def __init__(
        self,
        uri: str = "mem://",
    ):
        self.uri = uri
        self._client = None

    def get_client(self):
        if self._client is None:
            if cozo is None:
                raise ModuleNotFoundError(
                    "pycozo package is required for CozoDbConnections",
                )
            engine, _, path = self.uri.partition("://")
            if hasattr(cozo, "Client"):
                self._client = cozo.Client(engine, path)
            elif hasattr(cozo, "Database"):
                self._client = cozo.Database(engine, path)
            else:
                raise AttributeError(
                    "Neither Client nor Database class found in pycozo package",
                )
        return self._client

    def close(self):
        if self._client and hasattr(self._client, "close"):
            self._client.close()

    def __enter__(self):
        return self

    def __exit__(
        self,
        exc_type,
        exc_val,
        exc_tb,
    ):
        self.close()
