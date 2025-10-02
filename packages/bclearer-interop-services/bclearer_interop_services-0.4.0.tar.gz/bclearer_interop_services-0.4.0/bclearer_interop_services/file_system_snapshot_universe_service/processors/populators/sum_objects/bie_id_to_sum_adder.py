from nf_common_base.b_source.services.identification_services.b_identity_ecosystem.bie_id_creation_module.bie_id_creation_facade import (
    BieIdCreationFacade,
)
from nf_common_base.b_source.services.identification_services.b_identity_ecosystem.objects.bie_ids import (
    BieIds,
)
from nf_common_base.b_source.services.snapshot_universe_service.objects.sum_objects import (
    SumObjects,
)


def add_bie_id_to_sum(
    bie_id: BieIds,
    sum_object: SumObjects,
) -> SumObjects:
    sum_bie_id = BieIdCreationFacade.create_order_insensitive_bie_id_for_multiple_objects(
        input_objects=[
            sum_object.bie_id,
            bie_id,
        ]
    )

    sum_object = SumObjects(
        bie_id=sum_bie_id,
        direction_type=sum_object.direction_type,
        bie_summed_type=sum_object.bie_summed_type,
    )
    return sum_object
