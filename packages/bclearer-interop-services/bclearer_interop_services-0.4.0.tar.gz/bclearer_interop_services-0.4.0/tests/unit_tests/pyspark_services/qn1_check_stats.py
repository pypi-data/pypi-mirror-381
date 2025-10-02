import pyspark.sql.functions as f


def check_all_cached_contents(
    df_flat, meta_dict
):
    """
    Dynamically checks stats for all columns in `df_flat` that have a 'cachedContents'
    entry in the metadata JSON. For each column, it compares various statistics between
    the metadata and the actual DataFrame values.
    """
    try:
        columns_info = meta_dict.get(
            "view", {}
        ).get("columns", [])
        if not columns_info:
            print(
                "No columns info found in metadata. Skipping stats check."
            )
            return

        for col_def in columns_info:
            name = col_def.get(
                "name", ""
            )
            # Use fieldName to match what is in the DataFrame.
            field_name = col_def.get(
                "fieldName", ""
            )
            # Some fieldName values might start with ":", remove if necessary:
            if field_name.startswith(
                ":"
            ):
                field_name = field_name[
                    1:
                ]

            cached = col_def.get(
                "cachedContents", None
            )
            if not cached:
                continue
            if (
                field_name
                not in df_flat.columns
            ):
                print(
                    f"Warning: DataFrame does not have column '{field_name}' as per metadata for field '{name}'."
                )
                continue

            print(
                f"\n--- Checking column '{field_name}' (metadata name: '{name}') ---"
            )

            # Extract expected stats from the metadata
            expected_cardinality = int(
                cached.get(
                    "cardinality", "0"
                )
            )
            expected_largest = (
                cached.get(
                    "largest", None
                )
            )
            expected_smallest = (
                cached.get(
                    "smallest", None
                )
            )
            expected_non_null = int(
                cached.get(
                    "non_null", "0"
                )
            )
            expected_null = int(
                cached.get("null", "0")
            )
            expected_count = int(
                cached.get("count", "0")
            )
            top_list = cached.get(
                "top", []
            )

            # Compute actual stats from the DataFrame
            df_count = df_flat.count()
            df_count_distinct = (
                df_flat.select(
                    field_name
                )
                .distinct()
                .count()
            )
            df_min_val = df_flat.select(
                f.min(field_name).alias(
                    "min"
                )
            ).collect()[0]["min"]
            df_max_val = df_flat.select(
                f.max(field_name).alias(
                    "max"
                )
            ).collect()[0]["max"]
            df_null_count = (
                df_flat.filter(
                    f.col(
                        field_name
                    ).isNull()
                ).count()
            )
            df_non_null_count = (
                df_count - df_null_count
            )

            print(
                f"Cardinality: expected={expected_cardinality}, actual={df_count_distinct} "
                + (
                    "-> MATCH"
                    if expected_cardinality
                    == df_count_distinct
                    else "-> MISMATCH"
                )
            )
            print(
                f"Largest: expected='{expected_largest}', actual='{df_max_val}' "
                + (
                    "-> MATCH"
                    if str(
                        expected_largest
                    )
                    == str(df_max_val)
                    else "-> MISMATCH"
                )
            )
            print(
                f"Smallest: expected='{expected_smallest}', actual='{df_min_val}' "
                + (
                    "-> MATCH"
                    if str(
                        expected_smallest
                    )
                    == str(df_min_val)
                    else "-> MISMATCH"
                )
            )
            print(
                f"Non-null: expected={expected_non_null}, actual={df_non_null_count} "
                + (
                    "-> MATCH"
                    if expected_non_null
                    == df_non_null_count
                    else "-> MISMATCH"
                )
            )
            print(
                f"Null: expected={expected_null}, actual={df_null_count} "
                + (
                    "-> MATCH"
                    if expected_null
                    == df_null_count
                    else "-> MISMATCH"
                )
            )
            print(
                f"Count: expected={expected_count}, actual={df_count} "
                + (
                    "-> MATCH"
                    if expected_count
                    == df_count
                    else "-> MISMATCH"
                )
            )

            # Check the 'top' statistics for this column.
            if top_list:
                expected_top = []
                for item in top_list:
                    # Convert count to integer if necessary.
                    expected_top.append(
                        (
                            item.get(
                                "item"
                            ),
                            int(
                                item.get(
                                    "count",
                                    "0",
                                )
                            ),
                        )
                    )
                num_top = len(
                    expected_top
                )
                # Calculate actual top N values for this column.
                actual_top_df = (
                    df_flat.groupBy(
                        field_name
                    )
                    .agg(
                        f.count(
                            "*"
                        ).alias(
                            "item_count"
                        )
                    )
                    .orderBy(
                        f.desc(
                            "item_count"
                        )
                    )
                    .limit(num_top)
                )
                actual_top = [
                    (
                        row[field_name],
                        row[
                            "item_count"
                        ],
                    )
                    for row in actual_top_df.collect()
                ]

                print(
                    f"Expected Top {num_top} items:"
                )
                for idx, (
                    exp_item,
                    exp_count,
                ) in enumerate(
                    expected_top,
                    start=1,
                ):
                    print(
                        f"  {idx}: item='{exp_item}', count={exp_count}"
                    )
                print(
                    f"Actual Top {num_top} items:"
                )
                for idx, (
                    act_item,
                    act_count,
                ) in enumerate(
                    actual_top, start=1
                ):
                    print(
                        f"  {idx}: item='{act_item}', count={act_count}"
                    )
                for i in range(num_top):
                    if i < len(
                        actual_top
                    ):
                        (
                            exp_item,
                            exp_count,
                        ) = expected_top[
                            i
                        ]
                        (
                            act_item,
                            act_count,
                        ) = actual_top[
                            i
                        ]
                        msg = f"Top {i + 1}: expected item='{exp_item}' count={exp_count}; actual item='{act_item}' count={act_count}"
                        if (
                            str(
                                exp_item
                            )
                            == str(
                                act_item
                            )
                            and exp_count
                            == act_count
                        ):
                            print(
                                msg
                                + " -> MATCH"
                            )
                        else:
                            print(
                                msg
                                + " -> MISMATCH"
                            )
                    else:
                        print(
                            f"Actual top list for '{field_name}' is shorter than expected; missing entry for index {i + 1}."
                        )
    except Exception as e:
        print(
            "Failed to validate metadata. Error:",
            e,
        )
