import sys
import types

import pytest


# Create a stub raphtory module with a minimal Graph class
class DummyGraph:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

raphtory_stub = types.ModuleType("raphtory")
raphtory_stub.Graph = DummyGraph
sys.modules["raphtory"] = raphtory_stub

from bclearer_interop_services.graph_services.raphtory_service.object_models import (
    raphtory_graphs,
)
from bclearer_interop_services.graph_services.raphtory_service.object_models.raphtory_graphs import (
    RaphtoryGraphs,
)


def test_create_and_get_graph():
    manager = RaphtoryGraphs()
    graph = manager.create_graph("test")
    assert isinstance(graph, DummyGraph)
    assert manager.get_graph("test") is graph


def test_create_graph_existing_name_raises():
    manager = RaphtoryGraphs()
    manager.create_graph("dup")
    with pytest.raises(ValueError, match="already exists"):
        manager.create_graph("dup")


def test_create_graph_memory_error(monkeypatch):
    manager = RaphtoryGraphs()

    class FailingGraph:
        def __init__(self, **kwargs):
            raise MemoryError

    monkeypatch.setattr(raphtory_graphs, "Graph", FailingGraph)
    with pytest.raises(MemoryError):
        manager.create_graph("fail")
    monkeypatch.setattr(raphtory_graphs, "Graph", DummyGraph)


def test_get_graph_not_found():
    manager = RaphtoryGraphs()
    with pytest.raises(KeyError) as exc:
        manager.get_graph("missing")
    assert "Graph 'missing' not found" in str(exc.value)


def test_delete_graph_removes_and_collects(monkeypatch):
    manager = RaphtoryGraphs()
    manager.create_graph("temp")

    collected = False

    def fake_collect():
        nonlocal collected
        collected = True
        return 0

    monkeypatch.setattr(raphtory_graphs.gc, "collect", fake_collect)
    manager.delete_graph("temp")

    assert collected
    with pytest.raises(KeyError):
        manager.get_graph("temp")
