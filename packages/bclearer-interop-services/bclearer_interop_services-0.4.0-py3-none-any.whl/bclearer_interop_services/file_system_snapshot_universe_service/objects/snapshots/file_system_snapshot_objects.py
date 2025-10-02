from nf_common_base.b_source.services.identification_services.b_identity_ecosystem.common_knowledge.bie_domain_types import (
    BieDomainTypes,
)
from nf_common_base.b_source.services.identification_services.b_identity_ecosystem.objects.bie_ids import (
    BieIds,
)
from nf_common_base.b_source.services.snapshot_universe_service.objects.snapshots import (
    Snapshots,
)


class FileSystemSnapshotObjects(
    Snapshots
):
    def __init__(
        self,
        bie_id: BieIds,
        base_hr_name: str,
        bie_domain_type: BieDomainTypes,
        relative_path: "RelativePaths",
        file_reference_number: "FileReferenceNumbers",
        object_content: "ObjectContents",
    ):
        super().__init__(
            bie_id=bie_id,
            base_hr_name=base_hr_name,
            bie_domain_type=bie_domain_type,
        )

        self.add_extended_object(
            extended_object=relative_path
        )

        self.add_extended_object(
            extended_object=file_reference_number
        )

        self.add_extended_object(
            extended_object=object_content
        )

        from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.extended.root_relative_paths import (
            RootRelativePaths,
        )

        if isinstance(
            relative_path,
            RootRelativePaths,
        ):
            return

        parent_snapshot = (
            relative_path.relative_path_parent.snapshot
        )

        # TODO - have a whole-part service?
        self.wholes.add(parent_snapshot)

        parent_snapshot.parts.add(self)
