import datetime
import os

import pytest
from bclearer_interop_services.excel_services.excel_facades import (
    ExcelFacades,
)


class TestExcelFacadesEditHistory:
    @pytest.fixture(autouse=True)
    def setup_method(
        self,
        excel_file_name_and_path_xlsx,
        data_output_folder_absolute_path,
    ):
        # Set up fixture data
        self.excel_file_path = excel_file_name_and_path_xlsx
        self.sheet_name = "Categories"

        # Create output path for edit tests
        self.output_path = os.path.join(
            data_output_folder_absolute_path,
            "excel/test_edit_history.xlsx",
        )

        # Ensure the output directory exists
        os.makedirs(
            os.path.dirname(
                self.output_path
            ),
            exist_ok=True,
        )

        # Define test coordinates and values
        self.test_row = 3
        self.test_col = 3
        self.initial_value = (
            "Initial value"
        )
        self.updated_value = (
            "Updated value"
        )
        self.final_value = "Final value"

    def test_edit_history_tracking(
        self,
    ):
        """Test that the edit_history dictionary is correctly tracking cell changes."""
        try:
            # Initialize a facade for testing
            excel_facade = ExcelFacades(
                self.excel_file_path
            )

            # Make a copy for testing
            excel_facade.save(
                self.output_path
            )

            # Create new facade with the copy file
            test_facade = ExcelFacades(
                self.output_path
            )

            # Verify edit_history dictionary exists and is empty at start
            assert hasattr(
                test_facade,
                "edit_history",
            ), "ExcelFacades instance should have an edit_history attribute"
            assert isinstance(
                test_facade.edit_history,
                dict,
            ), "edit_history should be a dictionary"
            assert (
                len(
                    test_facade.edit_history
                )
                == 0
            ), "edit_history should be empty initially"

            # Get current value to set up test
            current_value = test_facade.read_cell(
                sheet_name=self.sheet_name,
                row_index=self.test_row,
                column_index=self.test_col,
            )

            # Update the cell for the first time
            test_facade.update_cell(
                sheet_name=self.sheet_name,
                row_index=self.test_row,
                column_index=self.test_col,
                value=self.initial_value,
            )

            # Check history after first update
            cell_key = (
                self.sheet_name,
                self.test_row,
                self.test_col,
            )
            assert (
                cell_key
                in test_facade.edit_history
            ), "Cell key should be in edit_history after update"

            # Record should have original value (but we don't know what it was)
            assert (
                len(
                    test_facade.edit_history[
                        cell_key
                    ]
                )
                == 1
            ), "Should have 1 history entry"
            assert (
                "value"
                in test_facade.edit_history[
                    cell_key
                ][
                    0
                ]
            ), "History entry should contain 'value'"
            assert (
                "timestamp"
                in test_facade.edit_history[
                    cell_key
                ][
                    0
                ]
            ), "History entry should contain 'timestamp'"

            # Update the cell for the second time
            test_facade.update_cell(
                sheet_name=self.sheet_name,
                row_index=self.test_row,
                column_index=self.test_col,
                value=self.updated_value,
            )

            # Check history after second update
            assert (
                len(
                    test_facade.edit_history[
                        cell_key
                    ]
                )
                == 2
            ), "Should have 2 history entries"
            assert (
                test_facade.edit_history[
                    cell_key
                ][
                    1
                ][
                    "value"
                ]
                == self.initial_value
            ), "Second history entry should have initial value"

            # Update the cell for the third time
            test_facade.update_cell(
                sheet_name=self.sheet_name,
                row_index=self.test_row,
                column_index=self.test_col,
                value=self.final_value,
            )

            # Check history after third update
            assert (
                len(
                    test_facade.edit_history[
                        cell_key
                    ]
                )
                == 3
            ), "Should have 3 history entries"
            assert (
                test_facade.edit_history[
                    cell_key
                ][
                    2
                ][
                    "value"
                ]
                == self.updated_value
            ), "Third history entry should have updated value"

            # Check final cell value
            final_cell_value = test_facade.read_cell(
                sheet_name=self.sheet_name,
                row_index=self.test_row,
                column_index=self.test_col,
            )
            assert (
                final_cell_value
                == self.final_value
            ), f"Cell value should be {self.final_value}, got {final_cell_value}"

        except Exception as e:
            pytest.fail(
                f"An error occurred during the test: {e}"
            )

    def test_edit_history_timestamp_format(
        self,
    ):
        """Test that the timestamps in edit history are properly formatted ISO strings."""
        try:
            # Initialize a facade for testing
            excel_facade = ExcelFacades(
                self.excel_file_path
            )

            # Make a copy for testing
            excel_facade.save(
                self.output_path
            )

            # Create new facade with the copy file
            test_facade = ExcelFacades(
                self.output_path
            )

            # Update the cell
            test_facade.update_cell(
                sheet_name=self.sheet_name,
                row_index=self.test_row,
                column_index=self.test_col,
                value=self.initial_value,
            )

            # Get the timestamp
            cell_key = (
                self.sheet_name,
                self.test_row,
                self.test_col,
            )
            timestamp_str = test_facade.edit_history[
                cell_key
            ][
                0
            ][
                "timestamp"
            ]

            # Verify it's a valid ISO format string
            try:
                timestamp = datetime.datetime.fromisoformat(
                    timestamp_str
                )
                assert isinstance(
                    timestamp,
                    datetime.datetime,
                ), "Timestamp should parse to a datetime object"
            except ValueError:
                pytest.fail(
                    f"Timestamp '{timestamp_str}' is not a valid ISO format string"
                )

        except Exception as e:
            pytest.fail(
                f"An error occurred during the test: {e}"
            )

    def test_no_duplicate_entries_for_same_value(
        self,
    ):
        """Test that updating a cell with the same value doesn't add to history."""
        try:
            # Initialize a facade for testing
            excel_facade = ExcelFacades(
                self.excel_file_path
            )

            # Make a copy for testing
            excel_facade.save(
                self.output_path
            )

            # Create new facade with the copy file
            test_facade = ExcelFacades(
                self.output_path
            )

            # Update the cell
            test_facade.update_cell(
                sheet_name=self.sheet_name,
                row_index=self.test_row,
                column_index=self.test_col,
                value=self.initial_value,
            )

            # Get history length after first update
            cell_key = (
                self.sheet_name,
                self.test_row,
                self.test_col,
            )
            first_update_length = len(
                test_facade.edit_history[
                    cell_key
                ]
            )

            # Update with the same value
            test_facade.update_cell(
                sheet_name=self.sheet_name,
                row_index=self.test_row,
                column_index=self.test_col,
                value=self.initial_value,
            )

            # Check history length - should be unchanged
            assert (
                len(
                    test_facade.edit_history[
                        cell_key
                    ]
                )
                == first_update_length
            ), "Edit history length should not change when updating with the same value"

        except Exception as e:
            pytest.fail(
                f"An error occurred during the test: {e}"
            )
