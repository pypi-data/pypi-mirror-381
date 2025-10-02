### Please provide your code answer for the question here
import re

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName(
    "databricks_de"
).getOrCreate()
visitors_path = "data/births-with-visitor-data.jsonl"


def _run_query(query):
    return spark.sql(query).collect()


def _strip_margin(text):
    return re.sub(
        "\n[ \t]*\|", "\n", text
    )


# Write your code below this line

import xml.etree.ElementTree as ET

from pyspark.sql.functions import (
    avg,
    col,
)
from pyspark.sql.functions import (
    count as sql_count,
)
from pyspark.sql.functions import (
    desc,
    element_at,
    explode,
    expr,
    lit,
    regexp_replace,
    size,
    trim,
    udf,
    xpath,
)
from pyspark.sql.types import (
    ArrayType,
    MapType,
    StringType,
    StructField,
    StructType,
)


# Define the function that parses the XML string.
def parse_visitors(xml_string):
    """Parses an XML string and returns a list of dictionaries for each visitor node.

    Each dictionary contains the attributes of a <visitor> element.
    """
    if not xml_string:
        return []
    try:
        root = ET.fromstring(xml_string)
        visitors = []
        for visitor in root.findall(
            "visitor"
        ):
            # visitor.attrib returns a dictionary of attribute names and values.
            visitors.append(
                visitor.attrib
            )
        return visitors
    except Exception as e:
        # In case of parsing errors return empty list.
        return []


# Register the UDF with the proper schema.
parse_visitors_udf = udf(
    parse_visitors,
    ArrayType(
        MapType(
            StringType(), StringType()
        )
    ),
)

df = spark.read.option(
    "multiline", "false"
).json(visitors_path)

# Optional: Check the cleaned XML. The output should now start immediately with <visitors>

df_with_parsed = df.withColumn(
    "visitors_list",
    parse_visitors_udf(col("visitors")),
)

df_exploded = df_with_parsed.withColumn(
    "visitor",
    explode(col("visitors_list")),
)

# You can now select the visitor attributes (which are stored in a map/dictionary)
df_with_visitors = df_exploded.select(
    col("sid"),
    col("first_name"),
    col("county"),
    col("year"),
    col("sex"),
    col("visitors_list"),
    col("visitor")["id"].alias(
        "visitor_id"
    ),
    col("visitor")["age"].alias(
        "visitor_age"
    ),
    col("visitor")["sex"].alias(
        "visitor_sex"
    ),
)

df_with_visitors.show()
df_with_visitors.printSchema()

df_with_visitors.createOrReplaceTempView(
    "births"
)

### Part A
queryA = """
        SELECT count(*)
            as total_records
        FROM births
        """
query_result = _run_query(queryA)
try:
    partA = f"""records={query_result[0][0]}"""
except IndexError:
    partA = ""

### Part B
queryB = """
        SELECT
            county,
            AVG(size(visitors_list)) AS avg_visitors
        FROM births
        GROUP BY county
        ORDER BY avg_visitors DESC
        LIMIT 1
        """
query_result = _run_query(queryB)
try:
    partB = f"""county={query_result[0][0]}, avgVisitors={query_result[0][1]}"""
except IndexError:
    partB = ""

### Part C
queryC = """
        SELECT AVG(CAST(visitor_age AS INT)) AS avg_visitor_age
        FROM births
        WHERE county = 'KINGS'
        """
query_result = _run_query(queryC)
try:
    partC = f"""avgVisitorAge={query_result[0][0]}"""
except IndexError:
    partC = ""

### Part D
queryD = """
        SELECT visitor_age, COUNT(*) AS record_count
            FROM births
            WHERE county = 'KINGS'
            GROUP BY visitor_age
            ORDER BY record_count DESC
        LIMIT 1
        """
query_result = _run_query(queryD)
try:
    partD = f"""mostCommonBirthAge={query_result[0][0]}, count={query_result[0][1]}"""
except IndexError:
    partD = ""

# Do not edit below this line
with open("data/output.txt", "w") as f:
    f.write(
        f"{partA}\n{partB}\n{partC}\n{partD}\n"
    )

spark.stop()
