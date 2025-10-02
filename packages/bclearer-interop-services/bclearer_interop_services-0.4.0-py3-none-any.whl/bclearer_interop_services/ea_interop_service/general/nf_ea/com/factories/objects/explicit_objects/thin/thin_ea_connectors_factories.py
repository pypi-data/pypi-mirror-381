from bclearer_core.nf.types.nf_column_types import (
    NfColumnTypes,
)
from bclearer_interop_services.dataframe_service.dataframe_helpers.dataframe_filter_and_renamer import (
    dataframe_filter_and_rename,
)
from bclearer_interop_services.ea_interop_service.general.nf_ea.com.common_knowledge.column_types.nf_ea_com_column_types import (
    NfEaComColumnTypes,
)
from bclearer_interop_services.ea_interop_service.nf_ea_common.common_knowledge.column_types.ea_t.ea_t_connector_column_types import (
    EaTConnectorColumnTypes,
)
from bclearer_interop_services.ea_interop_service.nf_ea_common.common_knowledge.ea_collection_types import (
    EaCollectionTypes,
)
from pandas import DataFrame


class ThinEaConnectorsFactories:
    def __init__(
        self, nf_ea_com_universe
    ):
        self.nf_ea_com_universe = (
            nf_ea_com_universe
        )

    def create(self) -> DataFrame:
        ea_connectors = (
            self.__create_ea_connectors()
        )

        return ea_connectors

    def __create_ea_connectors(
        self,
    ) -> DataFrame:
        extended_t_connector_dataframe = self.nf_ea_com_universe.ea_tools_session_manager.nf_ea_sql_stage_manager.nf_ea_sql_universe_manager.get_extended_ea_t_table_dataframe(
            ea_repository=self.nf_ea_com_universe.ea_repository,
            ea_collection_type=EaCollectionTypes.EXTENDED_T_CONNECTOR,
        )

        nf_uuids_column_name = (
            NfColumnTypes.NF_UUIDS.column_name
        )

        ea_connector_place1_supplier_element_column_name = (
            NfEaComColumnTypes.ELEMENTS_SUPPLIER_PLACE1_END_CONNECTORS.column_name
        )

        ea_connector_place2_client_element_column_name = (
            NfEaComColumnTypes.ELEMENTS_CLIENT_PLACE2_END_CONNECTORS.column_name
        )

        ea_connector_direction_type_name_column_name = (
            NfEaComColumnTypes.CONNECTORS_DIRECTION_TYPE_NAME.column_name
        )

        ea_connector_element_type_name_column_name = (
            NfEaComColumnTypes.CONNECTORS_ELEMENT_TYPE_NAME.column_name
        )

        ea_connector_supplier_cardinality_column_name = (
            NfEaComColumnTypes.CONNECTORS_SOURCE_CARDINALITY.column_name
        )

        ea_connector_client_cardinality_column_name = (
            NfEaComColumnTypes.CONNECTORS_DEST_CARDINALITY.column_name
        )

        ea_connectors = dataframe_filter_and_rename(
            dataframe=extended_t_connector_dataframe,
            filter_and_rename_dictionary={
                nf_uuids_column_name: nf_uuids_column_name,
                "start_t_object_nf_uuids": ea_connector_place1_supplier_element_column_name,
                "end_t_object_nf_uuids": ea_connector_place2_client_element_column_name,
                EaTConnectorColumnTypes.T_CONNECTOR_DIRECTIONS.nf_column_name: ea_connector_direction_type_name_column_name,
                EaTConnectorColumnTypes.T_CONNECTOR_TYPES.nf_column_name: ea_connector_element_type_name_column_name,
                EaTConnectorColumnTypes.T_CONNECTOR_SOURCE_CARDINALITIES.nf_column_name: ea_connector_supplier_cardinality_column_name,
                EaTConnectorColumnTypes.T_CONNECTOR_DEST_CARDINALITIES.nf_column_name: ea_connector_client_cardinality_column_name,
            },
        )

        return ea_connectors
