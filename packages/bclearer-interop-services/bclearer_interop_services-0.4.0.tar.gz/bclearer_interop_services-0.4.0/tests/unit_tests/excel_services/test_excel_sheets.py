import os

import pandas as pd
import pytest
from bclearer_interop_services.excel_services.excel_facades import (
    ExcelFacades,
)
from pandas import DataFrame


class TestExcelSheets:
    @pytest.fixture(autouse=True)
    def setup_method(
        self,
        excel_file_name_and_path_xlsx,
        data_output_folder_absolute_path,
    ):
        self.excel_file_path = excel_file_name_and_path_xlsx
        self.sheet_name = "Categories"

        # Set up output path for save tests
        self.output_path = os.path.join(
            data_output_folder_absolute_path,
            "excel/test_save_dataframe.xlsx",
        )

        # Ensure the output directory exists
        os.makedirs(
            os.path.dirname(
                self.output_path
            ),
            exist_ok=True,
        )

        # Create test dataframe
        self.test_df = pd.DataFrame(
            {
                "Column1": [
                    "Value1",
                    "Value2",
                    "Value3",
                ],
                "Column2": [10, 20, 30],
                "Column3": [
                    1.1,
                    2.2,
                    3.3,
                ],
            }
        )

    def test_save_dataframe_method(
        self,
        data_output_folder_absolute_path,
    ):
        """Test the save_dataframe method added to ExcelSheets class."""
        try:
            # Get a reference to the ExcelSheets object
            excel_facade = ExcelFacades(
                self.excel_file_path
            )
            excel_sheet = excel_facade.workbook.sheet(
                self.sheet_name
            )

            # Test the save_dataframe method
            output_path = os.path.join(
                data_output_folder_absolute_path,
                "excel/test_save_dataframe.xlsx",
            )

            # Make sure output dir exists
            os.makedirs(
                os.path.dirname(
                    output_path
                ),
                exist_ok=True,
            )

            # Test saving the dataframe
            excel_sheet.save_dataframe(
                table=self.test_df,
                full_filename=output_path,
                sheet_name="TestSheet",
            )

            # Verify the saved file by loading it back
            result_facade = (
                ExcelFacades(
                    output_path
                )
            )
            result_df = result_facade.read_sheet_to_dataframe(
                sheet_name="TestSheet"
            )

            # Assertions
            assert isinstance(
                result_df, DataFrame
            ), "Result should be a DataFrame"
            assert (
                not result_df.empty
            ), "Result DataFrame should not be empty"
            assert result_df.shape == (
                3,
                3,
            ), f"DataFrame shape should be (3, 3), got {result_df.shape}"
            assert list(
                result_df.columns
            ) == [
                "Column1",
                "Column2",
                "Column3",
            ], "Column names don't match"
            assert (
                result_df.iloc[0][
                    "Column1"
                ]
                == "Value1"
            ), "First row value doesn't match"
            assert (
                result_df.iloc[1][
                    "Column2"
                ]
                == 20
            ), "Second row numeric value doesn't match"

        except Exception as e:
            pytest.fail(
                f"An error occurred during the test: {e}"
            )

    def test_save_dataframe_with_default_sheet_name(
        self,
        data_output_folder_absolute_path,
    ):
        """Test save_dataframe method using the default sheet name."""
        try:
            # Get a reference to the ExcelSheets object
            excel_facade = ExcelFacades(
                self.excel_file_path
            )
            excel_sheet = excel_facade.workbook.sheet(
                self.sheet_name
            )

            # Test the save_dataframe method with default sheet name
            output_path = os.path.join(
                data_output_folder_absolute_path,
                "excel/test_save_dataframe_default_sheet.xlsx",
            )

            # Make sure output dir exists
            os.makedirs(
                os.path.dirname(
                    output_path
                ),
                exist_ok=True,
            )

            # Use the default sheet name (should use the current sheet name)
            excel_sheet.save_dataframe(
                table=self.test_df,
                full_filename=output_path,
                # No sheet_name parameter
            )

            # Verify the saved file by loading it back
            # It should use the source sheet name (Categories)
            result_facade = (
                ExcelFacades(
                    output_path
                )
            )
            result_df = result_facade.read_sheet_to_dataframe(
                sheet_name=self.sheet_name
            )

            # Assertions
            assert isinstance(
                result_df, DataFrame
            ), "Result should be a DataFrame"
            assert (
                not result_df.empty
            ), "Result DataFrame should not be empty"
            assert result_df.shape == (
                3,
                3,
            ), f"DataFrame shape should be (3, 3), got {result_df.shape}"
            assert list(
                result_df.columns
            ) == [
                "Column1",
                "Column2",
                "Column3",
            ], "Column names don't match"

        except Exception as e:
            pytest.fail(
                f"An error occurred during the test: {e}"
            )
