from typing import Dict, Optional

from pydantic import (
    BaseModel,
    ValidationInfo,
    field_validator,
    model_validator,
)

from ...resources.mappings import (
    TYPES_MAP_NEO4J_TO_PYTHON,
    TYPES_MAP_PYTHON_TO_NEO4J,
    TYPES_MAP_PYTHON_TO_SOLUTIONS_WORKBENCH,
    TYPES_MAP_SOLUTIONS_WORKBENCH_TO_PYTHON,
    PythonTypeEnum,
)
from ...utils.naming_conventions import (
    fix_property,
)
from ..solutions_workbench import (
    SolutionsWorkbenchProperty,
)


class Property(BaseModel):
    """
    Property representation.

    Attributes
    ----------
    name : str
        The property name in Neo4j.
    type : str
        The Python type of the property.
    column_mapping : str
        Which column the property is found under.
    alias : Optional[str]
        An optional second column that also indicates this property.
    is_unique : bool
        Whether the property is a unique identifier.
    part_of_key : bool
        Whether the property is part of a node or relationship key.
    """

    name: str
    type: str
    column_mapping: str
    alias: Optional[str] = None
    is_unique: bool = False
    part_of_key: bool = False

    @field_validator("name")
    def validate_name(
        cls,
        name: str,
        info: ValidationInfo,
    ) -> str:
        apply_neo4j_naming_conventions: (
            bool
        ) = (
            info.context.get(
                "apply_neo4j_naming_conventions",
                True,
            )
            if info.context is not None
            else True
        )

        if apply_neo4j_naming_conventions:
            return fix_property(name)

        return name

    @field_validator(
        "type", mode="before"
    )
    def validate_type(
        cls, v: str
    ) -> str:
        if (
            v.lower() == "object"
            or v.lower() == "string"
        ):
            return "str"
        elif "float" in v.lower():
            return "float"
        elif v.lower().startswith(
            "int"
        ):
            return "int"
        elif "bool" in v.lower():
            return "bool"

        valid_python_types = [
            a.value
            for a in PythonTypeEnum
        ]
        if v in valid_python_types:
            return v
        elif (
            v.split(".")[-1]
            in valid_python_types
        ):
            return v.split(".")[-1]
        elif v in list(
            TYPES_MAP_SOLUTIONS_WORKBENCH_TO_PYTHON.keys()
        ):
            return TYPES_MAP_SOLUTIONS_WORKBENCH_TO_PYTHON[
                v
            ]
        elif v in list(
            TYPES_MAP_NEO4J_TO_PYTHON.keys()
        ):
            return TYPES_MAP_NEO4J_TO_PYTHON[
                v
            ]
        else:
            raise ValueError(
                f"Invalid Property type given: {v}. Must be one of: {valid_python_types}"
            )

    @model_validator(mode="after")
    def validate_is_unique_and_part_of_key(
        self,
    ) -> "Property":
        if (
            self.is_unique
            and self.part_of_key
        ):
            self.part_of_key = False
        return self

    def get_schema(
        self,
        verbose: bool = True,
        neo4j_typing: bool = False,
    ) -> str:
        """
        Get the Property schema.

        Parameters
        ----------
        verbose : bool, optional
            Whether to provide more detail, by default True
        neo4j_typing : bool, optional
            Whether to use Neo4j types instead of Python types, by default False

        Returns
        -------
        str
            The schema
        """

        ending = ""
        if self.is_unique:
            ending = " | UNIQUE"
        elif self.part_of_key:
            ending = " | KEY"

        if verbose:
            return (
                f"{self.name} ({self.column_mapping}): {self.type if not neo4j_typing else self.neo4j_type}"
                + ending
            )
        else:
            return f"{self.name}: {self.type if not neo4j_typing else self.neo4j_type}"

    @property
    def neo4j_type(self) -> str:
        """
        The Neo4j property type.
        """
        return (
            TYPES_MAP_PYTHON_TO_NEO4J[
                self.type
            ]
        )

    @classmethod
    def from_arrows(
        cls,
        arrows_property: Dict[str, str],
        caption: str = "",
    ) -> "Property":
        """
        Parse the arrows property representation into a standard Property model.
        Arrow property values are formatted as <column_mapping> | <python_type> | <unique, nodekey> | <ignore>.
        """

        column_mapping: str = ""
        if (
            "|"
            in list(
                arrows_property.values()
            )[0]
        ):
            prop_props = [
                x.strip()
                for x in list(
                    arrows_property.values()
                )[0].split("|")
            ]
            if "," in prop_props[0]:
                (
                    column_mapping,
                    alias,
                ) = [
                    x.strip()
                    for x in prop_props[
                        0
                    ].split(",")
                ]
            else:
                column_mapping = (
                    prop_props[0]
                )
                alias = None

            python_type = prop_props[1]
            is_unique = (
                "unique" in prop_props
            )
            node_key = (
                "nodekey" in prop_props
            )
        else:
            column_mapping = list(
                arrows_property.values()
            )[0]
            python_type = "unknown"
            alias = None
            is_unique = False
            node_key = False

        return cls(
            name=list(
                arrows_property.keys()
            )[0],
            column_mapping=column_mapping,
            alias=alias,
            type=python_type,
            is_unique=is_unique,
            part_of_key=node_key,
        )

    @classmethod
    def from_solutions_workbench(
        cls,
        solutions_workbench_property: SolutionsWorkbenchProperty,
    ) -> "Property":
        """
        Parse the Solutions Workbench property into the standard property representation.
        """

        if (
            ","
            in solutions_workbench_property.referenceData
        ):
            column_mapping, alias = [
                x.strip()
                for x in solutions_workbench_property.referenceData.split(
                    ","
                )
            ]
        else:
            column_mapping, alias = (
                solutions_workbench_property.referenceData,
                None,
            )

        return cls(
            name=solutions_workbench_property.name,
            column_mapping=column_mapping,
            alias=alias,
            type=TYPES_MAP_SOLUTIONS_WORKBENCH_TO_PYTHON[
                solutions_workbench_property.datatype
            ],
            is_unique=solutions_workbench_property.hasUniqueConstraint,
            part_of_key=solutions_workbench_property.isPartOfKey,
        )

    def to_solutions_workbench(
        self,
    ) -> "SolutionsWorkbenchProperty":
        """
        Parse into a Solutions Workbench property representation.
        """
        if self.alias:
            reference_data = f"{self.column_mapping}, {self.alias}"
        else:
            reference_data = (
                self.column_mapping
            )

        return SolutionsWorkbenchProperty(
            key=self.name,
            name=self.name,
            datatype=TYPES_MAP_PYTHON_TO_SOLUTIONS_WORKBENCH[
                self.type
            ],
            referenceData=reference_data,
            isPartOfKey=self.part_of_key,
            isIndexed=self.is_unique,
            mustExist=self.part_of_key,
            hasUniqueConstraint=self.is_unique,
            isArray=(
                True
                if self.type.startswith(
                    "List"
                )
                else False
            ),
        )
