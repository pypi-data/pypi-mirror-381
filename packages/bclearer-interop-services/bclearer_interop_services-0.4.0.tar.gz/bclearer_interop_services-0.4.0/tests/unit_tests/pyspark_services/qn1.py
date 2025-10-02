# Please provide your code answer for Question 1 here
# Write the Data Frame into a CSV and load it into the `data/` folder
import pyspark.sql.functions as f
from pyspark.sql import SparkSession

# create a spark session
spark = SparkSession.builder.appName(
    "databricks_de"
).getOrCreate()
schema = [
    "sid",
    "id",
    "position",
    "created_at",
    "created_meta",
    "updated_at",
    "updated_meta",
    "meta",
    "year",
    "first_name",
    "county",
    "sex",
    "count",
]
baby_names_path = (
    "data/databricks_baby_names.json"
)
# Do not edit the code above this line.
########################################

from pyspark.sql.types import (
    StringType,
    StructField,
    StructType,
)

### Please provide your code answer for Question 1 by implementing the read_json_and_flatten_data() and parse_dataframe_with_schema() functions below.
from qn1_data_model import (
    build_dynamic_model,
    final_schema,
    get_metadata,
    get_schema,
    validate_record,
)


# Do not modify the function declarations below. Implement them based on the provided specifications.
def read_json_and_flatten_data(
    spark, baby_names_path
):
    """
    Reads the JSON data from the provided path and pulls all columns in the nested data column to top level.

    Parameters:
    - spark: The SparkSession object.
    - baby_names_path: Path to the JSON file containing baby names data.

    Returns:
    - A DataFrame.
    """
    # Implement read_json_and_flatten_data() here
    baby_names_dataframe = (
        spark.read.option(
            "multiline", "true"
        ).json(baby_names_path)
    )

    # Extract metadata and derive the metadata schema (as a list of column names).
    metadata = get_metadata(
        baby_names_dataframe
    )

    metadata_schema = get_schema(
        metadata
    )

    print(
        f"schema of input file:\n{metadata_schema}"
    )

    struct_fields = [
        StructField(
            field, StringType(), True
        )
        for field in metadata_schema
    ]

    explicit_schema = StructType(
        struct_fields
    )

    # If the 'data' column is missing, return an empty DataFrame with the specified column names.
    if (
        "data"
        not in baby_names_dataframe.columns
    ):
        return spark.createDataFrame(
            [], schema=explicit_schema
        )

    df_exploded = (
        baby_names_dataframe.withColumn(
            "record", f.explode("data")
        )
    )

    # Flatten the nested 'data' field.
    for idx, field in enumerate(
        metadata_schema
    ):
        df_exploded = (
            df_exploded.withColumn(
                field,
                f.col("record").getItem(
                    idx
                ),
            )
        )

    # Create DataFrame using the ordered RDD and the list of column names.
    df_flat = df_exploded.select(
        *metadata_schema
    )

    return df_flat


def parse_dataframe_with_schema(
    df_processed, schema
):
    """
    Parses the DataFrame returned by read_json_and_flatten_data for output to CSV based on the provided schema.

    Parameters:
    - df_processed: DataFrame returned from read_json_and_flatten_data.
    - schema: Schema to follow for the output CSV.

    Returns:
    - A DataFrame processed based on the provided schema.
    """
    # Implement parse_dataframe_with_schema() here

    # Verify that every column required for the output exists in the input DataFrame.
    input_columns = df_processed.columns
    missing_cols = [
        col
        for col in schema
        if col not in input_columns
    ]

    if missing_cols:
        raise ValueError(
            f"The following columns were not found in the input DataFrame: {missing_cols}"
        )

    # Create a new DataFrame from the ordered RDD using the required schema.
    parsed_df = df_processed.select(
        *schema
    )

    return parsed_df


from qn1_check_stats import (
    check_all_cached_contents,
)


def check_stats():
    """
    Reads the JSON data from the provided path, extracts metadata, creates a flat
    DataFrame from the nested data, and then checks the metadata statistics.
    """
    # Read the JSON file (using the multiline option)
    baby_names_dataframe = (
        spark.read.option(
            "multiline", "true"
        ).json(baby_names_path)
    )

    # Extract metadata using get_metadata (from your qn1_data_model module)
    meta_data = get_metadata(
        baby_names_dataframe
    )
    print("Extracted Metadata:")
    print(meta_data)

    # Read and flatten the baby names data.
    df_flat = (
        read_json_and_flatten_data(
            spark, baby_names_path
        )
    )

    # Parse the DataFrame using the provided schema.
    df_processed = (
        parse_dataframe_with_schema(
            df_flat, schema
        )
    )

    # Force materialization of the DataFrame to ensure all lazy actions are executed.
    df_processed.cache()
    _ = (
        df_processed.count()
    )  # Materialize the DataFrame.

    # Now check all cached metadata statistics.
    if meta_data is not None:
        check_all_cached_contents(
            df_processed, meta_data
        )


# run this to check if stats in the metadata match with the stats of in the dataframe
# check_stats()

########################################

# Do not edit the code below this line
df_processed = (
    read_json_and_flatten_data(
        spark, baby_names_path
    )
)
df = parse_dataframe_with_schema(
    df_processed, schema
)
df.toPandas().to_csv(
    "data/baby_names.csv", index=False
)
spark.stop()

# Please provide your brief written description of your code here. (Commented out)

# read_json_and_flatten_data : parses the json, and extracts the a flattenen data section into an rdd and returns this rdd

# parse_dataframe_with_schema : reads in the dataframe, validates that the schema is consitent with the globally defined schema, uses the schema provided to export the data into a dataframe.

# check_stats: this is an optional check to see if the stats in the data match the stats of the data loaded in the dataframe
