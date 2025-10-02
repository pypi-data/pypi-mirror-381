from nf_common_base.b_source.services.identification_services.b_identity_ecosystem.objects.bie_ids import (
    BieIds,
)
from nf_common_base.b_source.services.identification_services.b_identity_ecosystem.objects.bie_universes import (
    BieUniverses,
)


class BieFileSystemSnapshotUniverses(
    BieUniverses
):
    def __init__(
        self, bie_id: BieIds = None
    ):
        super().__init__(bie_id)
