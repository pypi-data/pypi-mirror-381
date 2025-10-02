import os

from networkx import (
    Graph,
    write_graphml,
)
from nf_common_base.b_source.services.file_system_service.objects.folders import (
    Folders,
)


class BSimpleGraphs:
    def __init__(
        self, graph: Graph, name: str
    ):
        self.graph = graph

        self.name = name

    def __enter__(self):
        return self

    def __exit__(
        self,
        exception_type,
        exception_value,
        traceback,
    ):
        pass

    def export_to_graph_ml(
        self, output_folder: Folders
    ) -> None:
        output_file_path = os.path.join(
            output_folder.absolute_path_string,
            self.name + ".graphml",
        )

        write_graphml(
            G=self.graph,
            path=output_file_path,
            encoding="utf-8",
            prettyprint=True,
        )
