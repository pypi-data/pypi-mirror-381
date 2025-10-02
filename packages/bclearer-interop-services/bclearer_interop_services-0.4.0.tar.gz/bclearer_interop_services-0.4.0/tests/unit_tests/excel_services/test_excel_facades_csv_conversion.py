import os
import shutil

import pandas as pd
import pytest
from bclearer_interop_services.excel_services.excel_facades import (
    ExcelFacades,
)


class TestExcelFacadesCsvConversion:
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
            "excel/csv_conversion_test",
        )

        # Create a multi-sheet test Excel file
        self.multi_sheet_excel_path = (
            os.path.join(
                self.output_folder,
                "test_multi_sheet.xlsx",
            )
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
        # If CSV files should be removed after test, uncomment:
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

        df3 = pd.DataFrame(
            {
                "Product": [
                    "Widget",
                    "Gadget",
                    "Tool",
                ],
                "Price": [
                    10.99,
                    24.99,
                    15.50,
                ],
                "InStock": [
                    True,
                    False,
                    True,
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
            sheet_name="Sheet1",
            index=False,
        )
        df2.to_excel(
            writer,
            sheet_name="Sheet2",
            index=False,
        )
        df3.to_excel(
            writer,
            sheet_name="Sheet3",
            index=False,
        )

        # Save the Excel file
        writer.close()

    def test_multi_sheet_csv_conversion(
        self,
    ):
        """Test that all sheets in an Excel file are properly converted to CSV files."""
        try:
            # Initialize facade
            excel_facade = ExcelFacades(
                self.multi_sheet_excel_path
            )

            # Convert to CSVs
            excel_facade.convert_to_csv(
                self.multi_sheet_excel_path
            )

            # Get base name of the Excel file without extension
            base_name = os.path.splitext(
                os.path.basename(
                    self.multi_sheet_excel_path
                )
            )[
                0
            ]

            # Check that CSV files were created for each sheet
            for sheet_name in [
                "Sheet1",
                "Sheet2",
                "Sheet3",
            ]:
                expected_csv_path = os.path.join(
                    self.output_folder,
                    f"{base_name}_{sheet_name}.csv",
                )

                # Assert CSV file exists
                assert os.path.exists(
                    expected_csv_path
                ), f"CSV file for {sheet_name} was not created"

                # Read CSV and check content
                csv_df = pd.read_csv(
                    expected_csv_path
                )
                assert (
                    not csv_df.empty
                ), f"CSV for {sheet_name} is empty"

                # Verify column names based on sheet
                if (
                    sheet_name
                    == "Sheet1"
                ):
                    expected_columns = [
                        "Column1",
                        "Column2",
                        "Column3",
                    ]
                elif (
                    sheet_name
                    == "Sheet2"
                ):
                    expected_columns = [
                        "Name",
                        "Age",
                        "City",
                    ]
                else:  # Sheet3
                    expected_columns = [
                        "Product",
                        "Price",
                        "InStock",
                    ]

                assert (
                    list(csv_df.columns)
                    == expected_columns
                ), f"Column names in {sheet_name} don't match"

                # Check the right number of rows for each sheet
                expected_rows = 3  # Default expectation
                assert (
                    len(csv_df)
                    == expected_rows
                ), f"CSV for {sheet_name} doesn't have expected number of rows ({expected_rows})"

        except Exception as e:
            pytest.fail(
                f"An error occurred during the test: {e}"
            )

    def test_csv_conversion_with_existing_files(
        self,
    ):
        """Test that existing CSV files aren't overwritten."""
        try:
            # Initialize facade
            excel_facade = ExcelFacades(
                self.multi_sheet_excel_path
            )

            # Get the expected CSV path for Sheet1
            base_name = os.path.splitext(
                os.path.basename(
                    self.multi_sheet_excel_path
                )
            )[
                0
            ]
            csv_path = os.path.join(
                self.output_folder,
                f"{base_name}_Sheet1.csv",
            )

            # Create a dummy CSV file in advance
            with open(
                csv_path, "w"
            ) as f:
                f.write(
                    "dummy,content\n1,2\n"
                )

            # Record the modification time of the file
            original_mtime = (
                os.path.getmtime(
                    csv_path
                )
            )

            # Run the conversion
            excel_facade.convert_to_csv(
                self.multi_sheet_excel_path
            )

            # Check that the file still exists
            assert os.path.exists(
                csv_path
            ), "CSV file should still exist"

            # Check that the modification time hasn't changed
            # This verifies the file wasn't overwritten
            current_mtime = (
                os.path.getmtime(
                    csv_path
                )
            )
            assert (
                current_mtime
                == original_mtime
            ), "CSV file should not have been overwritten"

        except Exception as e:
            pytest.fail(
                f"An error occurred during the test: {e}"
            )

    def test_csv_conversion_content_accuracy(
        self,
    ):
        """Test that CSV content accurately reflects the Excel content."""
        try:
            # Initialize facade
            excel_facade = ExcelFacades(
                self.multi_sheet_excel_path
            )

            # Convert to CSVs
            excel_facade.convert_to_csv(
                self.multi_sheet_excel_path
            )

            # Get base name of the Excel file without extension
            base_name = os.path.splitext(
                os.path.basename(
                    self.multi_sheet_excel_path
                )
            )[
                0
            ]

            # Check specific content in each CSV
            # Sheet2 test
            sheet2_csv_path = os.path.join(
                self.output_folder,
                f"{base_name}_Sheet2.csv",
            )
            sheet2_df = pd.read_csv(
                sheet2_csv_path
            )

            # Check specific cell values
            assert (
                sheet2_df.iloc[0][
                    "Name"
                ]
                == "John"
            ), "First row name should be 'John'"
            assert (
                sheet2_df.iloc[1]["Age"]
                == 25
            ), "Second row age should be 25"
            assert (
                sheet2_df.iloc[2][
                    "City"
                ]
                == "Paris"
            ), "Third row city should be 'Paris'"

            # Sheet3 test (with different data types)
            sheet3_csv_path = os.path.join(
                self.output_folder,
                f"{base_name}_Sheet3.csv",
            )
            sheet3_df = pd.read_csv(
                sheet3_csv_path
            )

            # Check specific cell values with different data types
            assert (
                sheet3_df.iloc[0][
                    "Product"
                ]
                == "Widget"
            ), "First row product should be 'Widget'"
            assert (
                sheet3_df.iloc[1][
                    "Price"
                ]
                == 24.99
            ), "Second row price should be 24.99"
            # Boolean values are usually converted to True/False strings in CSV
            assert str(
                sheet3_df.iloc[2][
                    "InStock"
                ]
            ).lower() in (
                "true",
                "1",
            ), "Third row InStock should be True"

        except Exception as e:
            pytest.fail(
                f"An error occurred during the test: {e}"
            )
