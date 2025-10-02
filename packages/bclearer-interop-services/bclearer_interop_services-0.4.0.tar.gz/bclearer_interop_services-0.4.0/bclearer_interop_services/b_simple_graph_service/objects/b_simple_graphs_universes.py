from nf_common_base.b_source.common.infrastructure.nf.objects.verses.nf_universes import (
    NfUniverses,
)
from nf_common_base.b_source.services.b_simple_graph_service.objects.b_simple_graph_generators import (
    BSimpleGraphGenerators,
)
from nf_common_base.b_source.services.b_simple_graph_service.objects.b_simple_graphs_universe_registries import (
    BSimpleGraphsUniverseRegistries,
)
from nf_common_base.b_source.services.file_system_service.objects.folders import (
    Folders,
)
from nf_common_base.b_source.services.reporting_service.wrappers.run_and_log_function_wrapper import (
    run_and_log_function,
)


class BSimpleGraphsUniverses(
    NfUniverses
):
    def __init__(self):
        super().__init__()

        self.b_simple_graphs_universe_registry = BSimpleGraphsUniverseRegistries(
            owning_b_simple_graphs_universe=self
        )

        # TODO: Is this actually needed here?
        self.b_simple_graphs_generator = BSimpleGraphGenerators(
            owning_b_simple_graphs_universe=self
        )

    def __enter__(self):
        return self

    def __exit__(
        self,
        exception_type,
        exception_value,
        traceback,
    ):
        pass

    # TODO: add parameter output_folder and any other output-related parameters
    @run_and_log_function()
    def export_all_b_simple_graphs_to_graph_ml(
        self, output_folder: Folders
    ) -> None:
        self.b_simple_graphs_universe_registry.export_all_b_simple_graphs_to_graph_ml(
            output_folder=output_folder
        )

    # def run_b_simple_graph_generator(
    #         self,
    #         b_simple_graph_generator: BSimpleGraphGenerators) \
    #         -> None:
    #     b_simple_graph_generator.generate_and_register_b_simple_graph()
