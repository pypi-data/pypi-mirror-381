import os

import pandas as pd
import pytest
from bclearer_interop_services.delimited_text.csv_summarizer import (
    generate_detailed_csv_summary,
    summarize_csv,
    summarize_csv_directory,
)
from pandas import DataFrame


class TestCsvSummarizer:
    @pytest.fixture(autouse=True)
    def setup_method(
        self,
        csv_file_name_and_path,
        data_output_folder_absolute_path,
    ):
        # Set up fixture data
        self.csv_file_path = (
            csv_file_name_and_path
        )

        # Create output paths
        self.output_folder = os.path.join(
            data_output_folder_absolute_path,
            "csv/summarization_test",
        )

        # Ensure output directory exists
        os.makedirs(
            self.output_folder,
            exist_ok=True,
        )

        # Create test CSV files
        self._create_test_csv_files()

        yield

    def _create_test_csv_files(self):
        """Create test CSV files for the test cases."""
        # Create a simple CSV with standard data
        df1 = pd.DataFrame(
            {
                "ID": [
                    1,
                    2,
                    3,
                ],
                "Name": [
                    "Alpha",
                    "Beta",
                    "Gamma",
                ],
                "Value": [
                    100,
                    200,
                    300,
                ],
            }
        )

        # Create a CSV with different data types
        df2 = pd.DataFrame(
            {
                "String": [
                    "Text1",
                    "Text2",
                    None,
                ],
                "Integer": [
                    10,
                    None,
                    30,
                ],
                "Float": [
                    1.1,
                    2.2,
                    3.3,
                ],
            }
        )

        # Save the test CSV files
        self.standard_csv_path = (
            os.path.join(
                self.output_folder,
                "standard_data.csv",
            )
        )
        self.mixed_csv_path = (
            os.path.join(
                self.output_folder,
                "mixed_types.csv",
            )
        )

        df1.to_csv(
            self.standard_csv_path,
            index=False,
        )
        df2.to_csv(
            self.mixed_csv_path,
            index=False,
        )

    def test_summarize_csv(
        self,
    ):
        """Test basic CSV summarization."""
        try:
            # Get summary for the standard CSV file
            summary_df = summarize_csv(
                self.standard_csv_path
            )

            # Verify summary structure
            assert isinstance(
                summary_df, DataFrame
            ), "Return value should be a DataFrame"
            assert (
                not summary_df.empty
            ), "Summary DataFrame should not be empty"

            # Check expected columns
            assert (
                "number_of_rows"
                in summary_df.columns
            ), "Summary should contain row count"
            assert (
                "number_of_columns"
                in summary_df.columns
            ), "Summary should contain column count"
            assert (
                "file_name"
                in summary_df.columns
            ), "Summary should contain file name"

            # Check specific values
            assert (
                summary_df[
                    "number_of_rows"
                ].values[0]
                == 3
            ), "CSV should have 3 rows"
            assert (
                summary_df[
                    "number_of_columns"
                ].values[0]
                == 3
            ), "CSV should have 3 columns"
            assert (
                summary_df[
                    "file_name"
                ].values[0]
                == "standard_data.csv"
            ), "File name incorrect"

        except Exception as e:
            pytest.fail(
                f"An error occurred during the test: {e}"
            )

    def test_summarize_csv_error_handling(
        self,
    ):
        """Test error handling for non-existent files."""
        # Create a non-existent file path
        non_existent_path = (
            os.path.join(
                self.output_folder,
                "non_existent_file.csv",
            )
        )

        # Get summary
        summary_df = summarize_csv(
            non_existent_path
        )

        # Should return a DataFrame with error information
        assert isinstance(
            summary_df, DataFrame
        ), "Return value should be a DataFrame even with errors"
        assert (
            "error"
            in summary_df.columns
        ), "Error column should be present for failed summaries"
        assert (
            summary_df[
                "file_name"
            ].values[0]
            == "non_existent_file.csv"
        ), "File name incorrect"
        assert (
            summary_df[
                "number_of_rows"
            ].values[0]
            == 0
        ), "Error case should report 0 rows"

    def test_summarize_csv_directory(
        self,
    ):
        """Test summarization of all CSV files in a directory."""
        try:
            # Run the directory summarization
            summary_df = (
                summarize_csv_directory(
                    self.output_folder
                )
            )

            # Verify summary structure
            assert isinstance(
                summary_df, DataFrame
            ), "Return value should be a DataFrame"
            assert (
                not summary_df.empty
            ), "Summary DataFrame should not be empty"
            assert (
                len(summary_df) == 2
            ), "Summary should have 2 rows (one for each CSV file)"

            # Check columns
            assert (
                "number_of_rows"
                in summary_df.columns
            ), "Summary should contain row count"
            assert (
                "number_of_columns"
                in summary_df.columns
            ), "Summary should contain column count"
            assert (
                "file_name"
                in summary_df.columns
            ), "Summary should contain file name"
            assert (
                "parent_directory"
                in summary_df.columns
            ), "Summary should contain parent directory"

            # Verify files were found
            files_found = summary_df[
                "file_name"
            ].tolist()
            assert (
                "standard_data.csv"
                in files_found
            ), "Standard CSV file should be in summary"
            assert (
                "mixed_types.csv"
                in files_found
            ), "Mixed types CSV file should be in summary"

            # Check parent directory
            assert (
                summary_df[
                    "parent_directory"
                ].iloc[0]
                == self.output_folder
            ), "Parent directory should match"

        except Exception as e:
            pytest.fail(
                f"An error occurred during the test: {e}"
            )

    def test_generate_detailed_csv_summary(
        self,
    ):
        """Test detailed CSV summary generation."""
        try:
            # Get detailed summary
            summary = generate_detailed_csv_summary(
                self.standard_csv_path
            )

            # Check basic structure
            assert isinstance(
                summary, dict
            ), "Summary should be a dictionary"
            assert (
                "file_info" in summary
            ), "Summary should contain file info"
            assert (
                "data_summary"
                in summary
            ), "Summary should contain data summary"
            assert (
                "column_statistics"
                in summary
            ), "Summary should contain column statistics"

            # Check file info
            assert (
                summary["file_info"][
                    "file_name"
                ]
                == "standard_data.csv"
            ), "File name incorrect"
            assert (
                summary["file_info"][
                    "file_size_bytes"
                ]
                > 0
            ), "File size should be positive"

            # Check data summary
            assert (
                summary["data_summary"][
                    "row_count"
                ]
                == 3
            ), "Should report 3 rows"
            assert (
                summary["data_summary"][
                    "column_count"
                ]
                == 3
            ), "Should report 3 columns"
            assert (
                "ID"
                in summary[
                    "data_summary"
                ]["column_names"]
            ), "ID column should be present"
            assert (
                "Name"
                in summary[
                    "data_summary"
                ]["column_names"]
            ), "Name column should be present"
            assert (
                "Value"
                in summary[
                    "data_summary"
                ]["column_names"]
            ), "Value column should be present"

            # Check column statistics
            assert (
                "ID"
                in summary[
                    "column_statistics"
                ]
            ), "Column statistics for ID should exist"
            assert (
                "data_type"
                in summary[
                    "column_statistics"
                ]["ID"]
            ), "Data type should be reported"
            assert (
                summary[
                    "column_statistics"
                ]["ID"]["unique_count"]
                == 3
            ), "ID should have 3 unique values"

        except Exception as e:
            pytest.fail(
                f"An error occurred during the test: {e}"
            )

    def test_generate_detailed_csv_summary_with_mixed_types(
        self,
    ):
        """Test detailed CSV summary with mixed data types and nulls."""
        try:
            # Get detailed summary of mixed types file
            summary = generate_detailed_csv_summary(
                self.mixed_csv_path
            )

            # Check null counts
            assert (
                summary[
                    "column_statistics"
                ]["String"][
                    "non_null_count"
                ]
                == 2
            ), "String column should have 2 non-null values"
            assert (
                summary[
                    "column_statistics"
                ]["Integer"][
                    "non_null_count"
                ]
                == 2
            ), "Integer column should have 2 non-null values"

            # Check null percentage calculation
            assert (
                summary[
                    "column_statistics"
                ]["String"][
                    "null_percentage"
                ]
                > 0
            ), "String column should report null percentage"
            assert (
                summary[
                    "column_statistics"
                ]["Integer"][
                    "null_percentage"
                ]
                > 0
            ), "Integer column should report null percentage"

        except Exception as e:
            pytest.fail(
                f"An error occurred during the test: {e}"
            )
