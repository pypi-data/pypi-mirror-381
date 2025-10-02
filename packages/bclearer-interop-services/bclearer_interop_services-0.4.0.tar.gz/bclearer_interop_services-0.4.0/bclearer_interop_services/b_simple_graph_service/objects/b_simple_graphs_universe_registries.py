from nf_common_base.b_source.common.infrastructure.nf.objects.registries.nf_universe_registries import (
    NfUniverseRegistries,
)
from nf_common_base.b_source.services.file_system_service.objects.folders import (
    Folders,
)


class BSimpleGraphsUniverseRegistries(
    NfUniverseRegistries
):
    def __init__(
        self,
        owning_b_simple_graphs_universe,
    ):
        super().__init__()
        self.b_simple_graphs_keyed_on_generator = (
            dict()
        )

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

    def export_all_b_simple_graphs_to_graph_ml(
        self, output_folder: Folders
    ) -> None:
        for (
            b_simple_graph
        ) in (
            self.b_simple_graphs_keyed_on_generator.values()
        ):
            b_simple_graph.export_to_graph_ml(
                output_folder=output_folder
            )
