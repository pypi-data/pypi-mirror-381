"""Raphtory service facade."""

from __future__ import annotations

from typing import Self

from raphtory import Graph

from .configurations.raphtory_configurations import (
    RaphtoryConfigurations,
)
from .object_models.raphtory_algorithms import (
    RaphtoryAlgorithms,
)
from .object_models.raphtory_graphs import (
    RaphtoryGraphs,
)
from .object_models.raphtory_temporal_views import (
    RaphtoryTemporalViews,
)
from .object_models.raphtory_vectorizations import (
    RaphtoryVectorizations,
)
from .orchestrators.raphtory_data_exporters import (
    RaphtoryDataExporters,
)
from .orchestrators.raphtory_data_loaders import (
    RaphtoryDataLoaders,
)


class RaphtoryServiceFacade:
    """Main entry point for Raphtory."""

    def __init__(
        self,
        configuration_file: str,
        *,
        profile: str = "default",
    ) -> None:
        self.configuration = RaphtoryConfigurations(
            configuration_file,
            profile=profile,
        )
        self.graphs = RaphtoryGraphs()

    def create_graph(
        self,
        name: str,
        **graph_kwargs: object,
    ) -> Graph:
        """Create and register a graph."""
        return self.graphs.create_graph(
            name,
            **graph_kwargs,
        )

    def get_graph(self, name: str) -> Graph:
        """Return a managed graph."""
        return self.graphs.get_graph(name)

    def get_temporal_views(
        self,
        name: str,
    ) -> RaphtoryTemporalViews:
        """Return temporal view helper."""
        return RaphtoryTemporalViews(
            self.get_graph(name),
        )

    def get_data_loader(
        self,
        name: str,
    ) -> RaphtoryDataLoaders:
        """Return data loader for graph."""
        return RaphtoryDataLoaders(
            self.get_graph(name),
        )

    def get_data_exporter(
        self,
        name: str,
    ) -> RaphtoryDataExporters:
        """Return data exporter for graph."""
        return RaphtoryDataExporters(
            self.get_graph(name),
        )

    def get_algorithms(
        self,
        name: str,
    ) -> RaphtoryAlgorithms:
        """Return algorithm helper."""
        return RaphtoryAlgorithms(
            self.get_graph(name),
        )

    def get_vectorizations(
        self,
        name: str,
    ) -> RaphtoryVectorizations:
        """Return vectorisation helper."""
        return RaphtoryVectorizations(
            self.get_graph(name),
        )

    def close(self) -> None:
        """Delete all managed graphs."""
        for name in list(self.graphs._graphs):
            self.graphs.delete_graph(name)

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type,
        exc_val,
        exc_tb,
    ) -> None:
        self.close()
