import pytest


def test_cozodb_connection():
    pytest.importorskip("pycozo")
    from bclearer_interop_services.graph_services.cozodb_service.object_models.cozodb_databases import (  # noqa: PLC0415
        CozoDbDatabases,
    )

    db = CozoDbDatabases(uri="mem://")
    client = db.connection.get_client()

    assert client is not None
    db.close()
