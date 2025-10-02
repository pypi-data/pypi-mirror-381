import json
import re
from typing import Optional
from uuid import UUID

from pydantic import (
    BaseModel,
    field_validator,
    model_validator,
)
from pyspark.sql.types import (
    IntegerType,
    StringType,
    StructField,
    StructType,
    TimestampType,
)


def ensure_dict(obj):
    """
    Convert `obj` to a Python dict if possible:
      - If obj is None => {}
      - If obj is already dict => obj
      - If obj is a Row => obj.asDict(recursive=True)
      - If obj is a string => parse it as JSON
      - Otherwise => attempt .asDict() or return {}
    """
    if obj is None:
        return {}
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, str):
        try:
            return json.loads(obj)
        except json.JSONDecodeError:
            return {}
    try:
        return obj.asDict(
            recursive=True
        )
    except:
        return {}


def get_metadata(input_dataframe):

    meta_data_dictionary = None
    print(
        f"reading dataframe with following columns: \n {input_dataframe.columns} "
    )
    if (
        "meta"
        in input_dataframe.columns
    ):

        meta_row = (
            input_dataframe.select(
                "meta"
            ).first()
        )

        if meta_row is not None:
            meta_data_dictionary = (
                ensure_dict(
                    meta_row["meta"]
                )
            )

        else:
            print(
                "Warning: Metadata section is present but empty; proceeding without metadata."
            )
    else:
        print(
            "Warning: Metadata section is not present in the input file."
        )

    return meta_data_dictionary


def get_schema(metadata):
    """
    Extracts column names from the metadata and converts them to snake_case.

    Parameters:
    - metadata (dict): The metadata dictionary containing the "view" information.

    Returns:
    - schema (list): A list of column names converted to snake_case.
    """
    # Navigate to the 'columns' list in the metadata
    columns = metadata.get(
        "view", {}
    ).get("columns", [])

    # Initialize the schema list.
    schema = []

    # Iterate over each column definition in the metadata
    for col in columns:
        # Get the original column name
        original_name = col.get(
            "name", ""
        )

        # Convert the name to snake_case:
        #   - lower the case,
        #   - replace any sequence of non-alphanumeric characters with a single underscore,
        #   - strip leading/trailing underscores if any
        snake_case_name = (
            re.sub(
                r"\W+",
                "_",
                original_name,
            )
            .lower()
            .strip("_")
        )

        # Append the converted name to the schema list.
        schema.append(snake_case_name)

    return schema


# Define the final Spark schema with the correct data types.
final_schema = StructType(
    [
        StructField(
            "sid", StringType(), False
        ),
        StructField(
            "id", StringType(), False
        ),
        StructField(
            "position",
            IntegerType(),
            False,
        ),
        StructField(
            "created_at",
            IntegerType(),
            False,
        ),
        StructField(
            "created_meta",
            StringType(),
            True,
        ),
        StructField(
            "updated_at",
            IntegerType(),
            False,
        ),
        StructField(
            "updated_meta",
            StringType(),
            True,
        ),
        StructField(
            "meta", StringType(), False
        ),
        StructField(
            "year", StringType(), False
        ),
        StructField(
            "first_name",
            StringType(),
            False,
        ),
        StructField(
            "county",
            StringType(),
            False,
        ),
        StructField(
            "sex", StringType(), False
        ),
        StructField(
            "count", StringType(), False
        ),
    ]
)


def build_dynamic_model():
    """
    Build a dynamic Pydantic model using Pydantic V2 style validators.
    """

    class BabyNameRecordDynamic(
        BaseModel
    ):
        sid: str
        id: UUID
        position: int
        created_at: int
        created_meta: Optional[str] = (
            None
        )
        updated_at: int
        updated_meta: Optional[str] = (
            None
        )
        meta: Optional[str] = "{ }"
        year: str
        first_name: str
        county: str
        sex: str
        count: str

        # ------------------------------------------------------------
        # Field validators in Pydantic V2 style using @field_validator
        # ------------------------------------------------------------

        @field_validator(
            "sid", mode="before"
        )
        def validate_sid(cls, v):
            pattern = (
                r"^row-[\w\.\-\~]+$"
            )
            if not v:
                raise ValueError(
                    "sid is required"
                )
            if not re.match(pattern, v):
                # TODO add fixes for sid
                raise ValueError(
                    "sid does not match required pattern"
                )
            return v

        @field_validator(
            "year", mode="before"
        )
        def validate_year(cls, v):
            pattern = r"[0-9]{4}"
            if not v:
                raise ValueError(
                    "year is required"
                )
            if not re.match(pattern, v):
                raise ValueError(
                    "year does not match required pattern"
                )
            return v

        @field_validator(
            "count", mode="before"
        )
        def validate_count(cls, v):
            return v

        @field_validator(
            "first_name", mode="before"
        )
        def validate_first_name(cls, v):
            if v is None:
                raise ValueError(
                    "first_name is required"
                )
            return v.upper()

        @field_validator("sex")
        def validate_sex(cls, v):
            if v not in {"M", "F"}:
                raise ValueError(
                    "Sex must be either 'M' or 'F'"
                )
            return v

        @field_validator(
            "created_at",
            "updated_at",
            mode="before",
        )
        def validate_timestamp(cls, v):
            ts = int(v)
            if ts < 0:
                raise ValueError(
                    "Timestamp must be a nonnegative integer"
                )
            return ts

        @field_validator(
            "meta", mode="before"
        )
        def validate_meta(cls, v):
            if v is None or (
                isinstance(v, str)
                and v.strip() == ""
            ):
                return "{ }"
            if isinstance(v, str):
                try:
                    obj = json.loads(v)
                    if not isinstance(
                        obj, dict
                    ):
                        raise ValueError(
                            "meta field must be a JSON object"
                        )
                except Exception:
                    raise ValueError(
                        "meta field must be a valid JSON string representing an object"
                    )
                if not obj:
                    return "{ }"
                return v
            else:
                if not isinstance(
                    v, dict
                ):
                    raise ValueError(
                        "meta field must be a JSON object"
                    )
                if not v:
                    return "{ }"
                return json.dumps(v)

        @field_validator(
            "county", mode="before"
        )
        def validate_county(cls, v):
            if v is None:
                return v
            return v

    return BabyNameRecordDynamic


def validate_record(
    rec: list, schema: list, model_cls
) -> dict:
    """
    Validates a single record (list of fields) against a Pydantic model.

    If validation fails, returns a dict of all None values (matching 'schema').
    If validation succeeds, returns the validated dict (with any transformations).
    """
    try:
        # Pad or slice 'rec' to match the length of 'schema'
        rec = rec[: len(schema)] + [
            None
        ] * (len(schema) - len(rec))

        # Convert into { colName: fieldValue } for Pydantic
        data_dict = dict(
            zip(schema, rec)
        )

        # Validate with your Pydantic model
        validated = model_cls(
            **data_dict
        )

        # Convert to Python dict
        result = validated.model_dump()

        # Example transformation: uppercase the "id" if not None
        if result.get("id"):
            result["id"] = str(
                result["id"]
            ).upper()

        # Return final validated result
        return result

    except Exception as e:
        # Debug: print or log the validation failure
        print(
            f"[VALIDATION ERROR] row={rec}\nReason: {e}\n"
        )

        # Return an all-None row so the schema lines up
        return {
            col: None for col in schema
        }
