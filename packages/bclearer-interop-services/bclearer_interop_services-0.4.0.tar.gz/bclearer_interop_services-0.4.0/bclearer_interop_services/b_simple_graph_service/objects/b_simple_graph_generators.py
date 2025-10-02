from abc import abstractmethod

from networkx import DiGraph
from nf_common_base.b_source.services.b_simple_graph_service.objects.b_simple_graphs import (
    BSimpleGraphs,
)
from nf_common_base.b_source.services.reporting_service.reporters.log_with_datetime import (
    log_message,
)


class BSimpleGraphGenerators:
    def __init__(
        self,
        owning_b_simple_graphs_universe,
    ):
        self.owning_b_simple_graphs_universe = owning_b_simple_graphs_universe

    def __enter__(self):
        return self

    def __exit__(
        self,
        exception_type,
        exception_value,
        traceback,
    ):
        pass

    @abstractmethod
    def generate_and_register_b_simple_graph(
        self, graph_name: str
    ) -> None:
        pass

    def register_b_simple_graph(
        self,
        graph: DiGraph,
        graph_name: str,
    ) -> None:
        log_message(
            message="Registering graph: "
            + graph_name
        )

        b_simple_graph = BSimpleGraphs(
            graph=graph, name=graph_name
        )

        self.owning_b_simple_graphs_universe.b_simple_graphs_universe_registry.b_simple_graphs_keyed_on_generator[
            self
        ] = b_simple_graph
