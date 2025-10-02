import os
import tempfile
from pathlib import Path

import pandas as pd
import pytest
from bclearer_interop_services.delimited_text.delimited_text_facades import (
    DelimitedTextFacades,
)


class TestDelimitedTextFacades:
    @pytest.fixture(autouse=True)
    def setup_method(
        self,
        data_output_folder_absolute_path,
    ):
        # Set up test data
        self.test_data = {
            "ID": [1, 2, 3],
            "Name": [
                "Alpha",
                "Beta",
                "Gamma",
            ],
            "Value": [100, 200, 300],
        }
        self.test_df = pd.DataFrame(
            self.test_data
        )

        # Create output folder
        self.output_folder = os.path.join(
            data_output_folder_absolute_path,
            "delimited_text_facade_tests",
        )
        os.makedirs(
            self.output_folder,
            exist_ok=True,
        )

        # Create test CSV file
        self.test_csv_path = (
            os.path.join(
                self.output_folder,
                "test_data.csv",
            )
        )
        self.test_df.to_csv(
            self.test_csv_path,
            index=False,
        )

        yield

        # Clean up
        if os.path.exists(
            self.test_csv_path
        ):
            os.remove(
                self.test_csv_path
            )

    def test_init_with_file_path(self):
        """Test initialization with a file path."""
        facade = DelimitedTextFacades(
            self.test_csv_path
        )

        # Check initialization
        assert (
            facade.file_path
            == self.test_csv_path
        )
        assert (
            facade._dataframe
            is not None
        )

        # Check data loaded correctly
        df = facade.get_dataframe()
        assert len(df) == 3
        assert list(df.columns) == [
            "ID",
            "Name",
            "Value",
        ]
        assert df["Name"][0] == "Alpha"

    def test_load_csv(self):
        """Test loading a CSV file."""
        facade = DelimitedTextFacades()
        df = facade.load_csv(
            self.test_csv_path
        )

        # Check dataframe loaded correctly
        assert len(df) == 3
        assert list(df.columns) == [
            "ID",
            "Name",
            "Value",
        ]
        assert df["Value"][2] == 300

        # Check it was stored in the instance
        assert (
            facade._dataframe
            is not None
        )
        assert (
            facade.file_path
            == self.test_csv_path
        )

    def test_save_csv(self):
        """Test saving a DataFrame to CSV."""
        facade = DelimitedTextFacades()
        facade.set_dataframe(
            self.test_df
        )

        # Save to new location
        output_path = os.path.join(
            self.output_folder,
            "output_test.csv",
        )
        facade.save_csv(output_path)

        # Verify the file was created and contains expected data
        assert os.path.exists(
            output_path
        )

        # Load and check
        loaded_df = pd.read_csv(
            output_path
        )
        assert len(loaded_df) == 3
        assert list(
            loaded_df.columns
        ) == ["ID", "Name", "Value"]

        # Clean up
        os.remove(output_path)

    def test_read_csv_files_from_directory(
        self,
    ):
        """Test reading all CSV files from a directory."""
        # Remove any existing test files to start fresh
        for file in os.listdir(
            self.output_folder
        ):
            file_path = os.path.join(
                self.output_folder, file
            )
            if os.path.isfile(
                file_path
            ) and file.endswith(".csv"):
                os.remove(file_path)

        # Create our test CSV files
        self.test_df.to_csv(
            self.test_csv_path,
            index=False,
        )

        second_df = pd.DataFrame(
            {
                "Letter": [
                    "A",
                    "B",
                    "C",
                ],
                "Number": [1, 2, 3],
            }
        )
        second_csv_path = os.path.join(
            self.output_folder,
            "second_test.csv",
        )
        second_df.to_csv(
            second_csv_path, index=False
        )

        # Read directory
        df_dict = DelimitedTextFacades.read_csv_files_from_directory(
            self.output_folder
        )

        # Verify results
        assert (
            len(df_dict) == 2
        ), f"Expected 2 files but found: {list(df_dict.keys())}"
        assert "test_data" in df_dict
        assert "second_test" in df_dict
        assert (
            len(df_dict["test_data"])
            == 3
        )
        assert (
            len(df_dict["second_test"])
            == 3
        )

        # Clean up
        os.remove(second_csv_path)

    def test_write_dataframes_to_csv_files(
        self,
    ):
        """Test writing multiple DataFrames to CSV files."""
        # Create dictionary of dataframes
        df_dict = {
            "first": self.test_df,
            "second": pd.DataFrame(
                {
                    "Letter": [
                        "A",
                        "B",
                        "C",
                    ],
                    "Number": [1, 2, 3],
                }
            ),
        }

        # Create output directory
        temp_dir = os.path.join(
            self.output_folder,
            "multi_csv_output",
        )
        os.makedirs(
            temp_dir, exist_ok=True
        )

        # Write files
        DelimitedTextFacades.write_dataframes_to_csv_files(
            df_dict, temp_dir
        )

        # Check files were created
        assert os.path.exists(
            os.path.join(
                temp_dir, "first.csv"
            )
        )
        assert os.path.exists(
            os.path.join(
                temp_dir, "second.csv"
            )
        )

        # Verify content
        first_df = pd.read_csv(
            os.path.join(
                temp_dir, "first.csv"
            )
        )
        second_df = pd.read_csv(
            os.path.join(
                temp_dir, "second.csv"
            )
        )

        assert len(first_df) == 3
        assert len(second_df) == 3
        assert list(
            first_df.columns
        ) == ["ID", "Name", "Value"]
        assert list(
            second_df.columns
        ) == ["Letter", "Number"]

    def test_export_list_to_csv(self):
        """Test exporting a list of strings to CSV."""
        test_list = [
            "First line",
            "Second line",
            "Third line",
        ]
        output_path = os.path.join(
            self.output_folder,
            "list_output.csv",
        )

        # Export list
        DelimitedTextFacades.export_list_to_csv(
            output_path, test_list
        )

        # Check file exists
        assert os.path.exists(
            output_path
        )

        # Verify content
        with open(
            output_path, "r"
        ) as f:
            lines = f.readlines()
            assert len(lines) == 3
            assert (
                "First line" in lines[0]
            )
            assert (
                "Second line"
                in lines[1]
            )
            assert (
                "Third line" in lines[2]
            )

        # Clean up
        os.remove(output_path)

    def test_export_dictionary_to_csv(
        self,
    ):
        """Test exporting a dictionary to CSV."""
        test_dict = {
            "Column1": ["A", "B", "C"],
            "Column2": [1, 2, 3],
        }
        output_path = os.path.join(
            self.output_folder,
            "dict_output.csv",
        )

        # Export dictionary
        DelimitedTextFacades.export_dictionary_to_csv(
            output_path, test_dict
        )

        # Check file exists
        assert os.path.exists(
            output_path
        )

        # Verify content
        df = pd.read_csv(output_path)
        assert len(df) == 3
        assert list(df.columns) == [
            "Column1",
            "Column2",
        ]
        assert df["Column1"][0] == "A"
        assert df["Column2"][2] == 3

        # Clean up
        os.remove(output_path)

    def test_summarize_csv(self):
        """Test CSV summarization."""
        summary_df = DelimitedTextFacades.summarize_csv(
            self.test_csv_path
        )

        # Check summary structure
        assert not summary_df.empty
        assert (
            "number_of_rows"
            in summary_df.columns
        )
        assert (
            "number_of_columns"
            in summary_df.columns
        )
        assert (
            "file_name"
            in summary_df.columns
        )

        # Check values
        assert (
            summary_df[
                "number_of_rows"
            ].values[0]
            == 3
        )
        assert (
            summary_df[
                "number_of_columns"
            ].values[0]
            == 3
        )
        assert (
            summary_df[
                "file_name"
            ].values[0]
            == "test_data.csv"
        )

    def test_summarize_directory(self):
        """Test directory summarization."""
        # Remove any existing test files to start fresh
        for file in os.listdir(
            self.output_folder
        ):
            file_path = os.path.join(
                self.output_folder, file
            )
            if os.path.isfile(
                file_path
            ) and file.endswith(".csv"):
                os.remove(file_path)

        # Create our test files
        self.test_df.to_csv(
            self.test_csv_path,
            index=False,
        )

        second_df = pd.DataFrame(
            {
                "Letter": [
                    "A",
                    "B",
                    "C",
                    "D",
                ],
                "Number": [1, 2, 3, 4],
            }
        )
        second_csv_path = os.path.join(
            self.output_folder,
            "second_test.csv",
        )
        second_df.to_csv(
            second_csv_path, index=False
        )

        # Summarize directory
        summary_df = DelimitedTextFacades.summarize_directory(
            self.output_folder
        )

        # Check summary structure
        assert not summary_df.empty
        assert (
            len(summary_df) == 2
        ), f"Expected 2 files but found: {summary_df['file_name'].tolist()}"  # Two CSV files
        assert (
            "number_of_rows"
            in summary_df.columns
        )
        assert (
            "file_name"
            in summary_df.columns
        )

        # Check file names are included
        file_names = summary_df[
            "file_name"
        ].tolist()
        assert (
            "test_data.csv"
            in file_names
        )
        assert (
            "second_test.csv"
            in file_names
        )

        # Clean up
        os.remove(second_csv_path)

    def test_detailed_summary(self):
        """Test detailed CSV summary."""
        summary = DelimitedTextFacades.detailed_summary(
            self.test_csv_path
        )

        # Check summary structure
        assert "file_info" in summary
        assert "data_summary" in summary
        assert (
            "column_statistics"
            in summary
        )

        # Check file info
        assert (
            summary["file_info"][
                "file_name"
            ]
            == "test_data.csv"
        )

        # Check data summary
        assert (
            summary["data_summary"][
                "row_count"
            ]
            == 3
        )
        assert (
            summary["data_summary"][
                "column_count"
            ]
            == 3
        )

        # Check column statistics
        assert (
            "ID"
            in summary[
                "column_statistics"
            ]
        )
        assert (
            "Name"
            in summary[
                "column_statistics"
            ]
        )
        assert (
            "Value"
            in summary[
                "column_statistics"
            ]
        )

        # Check column details
        assert (
            summary[
                "column_statistics"
            ]["Name"]["unique_count"]
            == 3
        )
        assert (
            "data_type"
            in summary[
                "column_statistics"
            ]["ID"]
        )

    def test_detect_encoding(self):
        """Test encoding detection."""
        encoding = DelimitedTextFacades.detect_encoding(
            self.test_csv_path
        )
        assert encoding is not None
        assert isinstance(encoding, str)
        assert len(encoding) > 0

    def test_convert_to_files_object(
        self,
    ):
        """Test conversion to Files object."""
        files_obj = DelimitedTextFacades.convert_to_files_object(
            self.test_csv_path
        )
        assert files_obj is not None
        assert files_obj.absolute_path_string.endswith(
            "test_data.csv"
        )

    def test_convert_to_folders_object(
        self,
    ):
        """Test conversion to Folders object."""
        folders_obj = DelimitedTextFacades.convert_to_folders_object(
            self.output_folder
        )
        assert folders_obj is not None
        assert folders_obj.absolute_path_string.endswith(
            "delimited_text_facade_tests"
        )
