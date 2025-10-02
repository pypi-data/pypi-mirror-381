import os
import shutil

import pandas as pd
import pytest
from bclearer_interop_services.excel_services.excel_facades import (
    ExcelFacades,
)
from bclearer_interop_services.file_system_service.objects.files import (
    Files,
)


class TestExcelFacadesUtilityMethods:
    @pytest.fixture(autouse=True)
    def setup_method(
        self,
        excel_file_name_and_path_xlsx,
        data_output_folder_absolute_path,
    ):
        # Set up fixture data
        self.excel_file_path = excel_file_name_and_path_xlsx

        # Create output paths
        self.output_folder = os.path.join(
            data_output_folder_absolute_path,
            "excel/utility_methods_test",
        )

        # Create test file paths
        self.multi_sheet_excel_path = os.path.join(
            self.output_folder,
            "test_multi_sheet_utils.xlsx",
        )

        # Ensure the output directory exists and is clean
        if os.path.exists(
            self.output_folder
        ):
            shutil.rmtree(
                self.output_folder
            )
        os.makedirs(
            self.output_folder,
            exist_ok=True,
        )

        # Create test multi-sheet Excel file
        self._create_test_excel_file()

        yield

        # Optional cleanup
        # if os.path.exists(self.output_folder):
        #    shutil.rmtree(self.output_folder)

    def _create_test_excel_file(self):
        """Create a multi-sheet Excel file for testing."""
        # Create sample dataframes for different sheets
        df1 = pd.DataFrame(
            {
                "Column1": [
                    "A1",
                    "A2",
                    "A3",
                ],
                "Column2": [
                    "B1",
                    "B2",
                    "B3",
                ],
                "Column3": [
                    "C1",
                    "C2",
                    "C3",
                ],
            }
        )

        df2 = pd.DataFrame(
            {
                "Name": [
                    "John",
                    "Jane",
                    "Bob",
                ],
                "Age": [30, 25, 45],
                "City": [
                    "New York",
                    "London",
                    "Paris",
                ],
            }
        )

        # Create Excel writer
        writer = pd.ExcelWriter(
            self.multi_sheet_excel_path,
            engine="xlsxwriter",
        )

        # Write each dataframe to a different sheet
        df1.to_excel(
            writer,
            sheet_name="DataSheet",
            index=False,
        )
        df2.to_excel(
            writer,
            sheet_name="PeopleSheet",
            index=False,
        )

        # Save the Excel file
        writer.close()

    def test_extract_dataframe_from_excel_sheet(
        self,
    ):
        """Test the extract_dataframe_from_excel_sheet method."""
        try:
            # Use the static method to extract a dataframe
            df = ExcelFacades.extract_dataframe_from_excel_sheet(
                self.multi_sheet_excel_path,
                "DataSheet",
            )

            # Verify dataframe structure
            assert (
                not df.empty
            ), "DataFrame should not be empty"
            assert list(df.columns) == [
                "Column1",
                "Column2",
                "Column3",
            ], "Column names don't match"
            assert (
                len(df) == 3
            ), "DataFrame should have 3 rows"

            # Verify content
            assert (
                df.iloc[0]["Column1"]
                == "A1"
            ), "First cell value mismatch"
            assert (
                df.iloc[1]["Column2"]
                == "B2"
            ), "Middle cell value mismatch"
            assert (
                df.iloc[2]["Column3"]
                == "C3"
            ), "Last cell value mismatch"

        except Exception as e:
            pytest.fail(
                f"An error occurred during the test: {e}"
            )

    def test_extract_dataframe_from_excel_sheet_error_handling(
        self,
    ):
        """Test error handling in extract_dataframe_from_excel_sheet."""
        # Test with non-existent sheet name
        with pytest.raises(
            Exception
        ) as exc_info:
            ExcelFacades.extract_dataframe_from_excel_sheet(
                self.multi_sheet_excel_path,
                "NonExistentSheet",
            )
        assert (
            "error reading sheet"
            in str(exc_info.value)
        ), "Error message should indicate sheet reading failure"

        # Test with non-existent file
        non_existent_path = os.path.join(
            self.output_folder,
            "non_existent_file.xlsx",
        )
        with pytest.raises(
            Exception
        ) as exc_info:
            ExcelFacades.extract_dataframe_from_excel_sheet(
                non_existent_path,
                "Sheet1",
            )
        assert (
            "error reading sheet"
            in str(exc_info.value)
        ), "Error message should indicate file reading failure"

    def test_convert_xlxs_to_dataframe_dictionary(
        self,
    ):
        """Test the convert_xlxs_to_dataframe_dictionary method."""
        try:
            # Create a Files object for the test file
            excel_file = Files(
                absolute_path_string=self.multi_sheet_excel_path
            )

            # Use the static method to convert Excel to dataframe dictionary
            df_dict = ExcelFacades.convert_xlxs_to_dataframe_dictionary(
                excel_file
            )

            # Verify dictionary structure
            assert isinstance(
                df_dict, dict
            ), "Result should be a dictionary"
            assert (
                len(df_dict) == 2
            ), "Dictionary should have 2 sheets"
            assert (
                "DataSheet" in df_dict
            ), "DataSheet should be in the dictionary"
            assert (
                "PeopleSheet" in df_dict
            ), "PeopleSheet should be in the dictionary"

            # Verify DataSheet content
            data_df = df_dict[
                "DataSheet"
            ]
            assert (
                not data_df.empty
            ), "DataSheet DataFrame should not be empty"
            assert list(
                data_df.columns
            ) == [
                "Column1",
                "Column2",
                "Column3",
            ], "DataSheet column names don't match"
            assert (
                len(data_df) == 3
            ), "DataSheet should have 3 rows"

            # Verify PeopleSheet content
            people_df = df_dict[
                "PeopleSheet"
            ]
            assert (
                not people_df.empty
            ), "PeopleSheet DataFrame should not be empty"
            assert list(
                people_df.columns
            ) == [
                "Name",
                "Age",
                "City",
            ], "PeopleSheet column names don't match"
            assert (
                len(people_df) == 3
            ), "PeopleSheet should have 3 rows"
            assert (
                people_df.iloc[0][
                    "Name"
                ]
                == "John"
            ), "First name should be John"
            assert (
                people_df.iloc[1]["Age"]
                == 25
            ), "Second age should be 25"

        except Exception as e:
            pytest.fail(
                f"An error occurred during the test: {e}"
            )

    def test_convert_sheet_with_header_to_dataframe(
        self,
    ):
        """Test the convert_sheet_with_header_to_dataframe method."""
        try:
            # Use the static method to convert a sheet with header to dataframe
            df = ExcelFacades.convert_sheet_with_header_to_dataframe(
                self.multi_sheet_excel_path,
                "PeopleSheet",
            )

            # Verify dataframe structure
            assert (
                not df.empty
            ), "DataFrame should not be empty"
            assert list(df.columns) == [
                "Name",
                "Age",
                "City",
            ], "Column names don't match"
            assert (
                len(df) == 3
            ), "DataFrame should have 3 rows"

            # Verify content
            assert (
                df.iloc[0]["Name"]
                == "John"
            ), "First name should be John"
            assert (
                df.iloc[1]["Age"] == 25
            ), "Second age should be 25"
            assert (
                df.iloc[2]["City"]
                == "Paris"
            ), "Third city should be Paris"

        except Exception as e:
            pytest.fail(
                f"An error occurred during the test: {e}"
            )

    def test_convert_sheet_with_header_to_dataframe_error_handling(
        self,
    ):
        """Test error handling in convert_sheet_with_header_to_dataframe."""
        from bclearer_core.constants.standard_constants import (
            DEFAULT_NULL_VALUE,
        )

        # Test with non-existent sheet name
        result = ExcelFacades.convert_sheet_with_header_to_dataframe(
            self.multi_sheet_excel_path,
            "NonExistentSheet",
        )
        assert (
            result == DEFAULT_NULL_VALUE
        ), "Should return DEFAULT_NULL_VALUE for non-existent sheet"

        # Test with non-existent file
        non_existent_path = os.path.join(
            self.output_folder,
            "non_existent_file.xlsx",
        )
        result = ExcelFacades.convert_sheet_with_header_to_dataframe(
            non_existent_path,
            "Sheet1",
        )
        assert (
            result == DEFAULT_NULL_VALUE
        ), "Should return DEFAULT_NULL_VALUE for non-existent file"
