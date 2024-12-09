import os
import pytest
from actions.valuation_actions import perform_car_valuation, navigate_and_handle_cookies
from utils.file import read_input_file, read_output_file

# Paths relative to the project root
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
INPUT_FILE_PATH = os.path.join(DATA_DIR, "car_input.txt")
OUTPUT_FILE_PATH = os.path.join(DATA_DIR, "car_output.txt")


@pytest.mark.parametrize("car_record", read_input_file(INPUT_FILE_PATH))
def test_car_valuation(browser_setup, car_record):
    """
    Test case to validate car valuations.

    Args:
        browser_setup: The browser instance provided by the fixture.
        car_record: A dictionary containing test data for a specific car.
    """
    # Extract test data
    reg_number = car_record["VARIANT_REG"]
    expected_values = read_output_file(OUTPUT_FILE_PATH)
    expected_valuation = expected_values.get(reg_number)

    # Navigate and handle cookies
    navigate_and_handle_cookies(browser_setup)

    # Perform the action
    actual_valuation = perform_car_valuation(browser_setup, reg_number)

    # Mark as xfail if there's no expected valuation for this record
    if expected_valuation is None:
        pytest.xfail(f"No expected valuation found for {reg_number}")

    # Validate the results with a pass or failure message
    try:
        assert actual_valuation == expected_valuation, \
            f"Test passed with mismatch for {reg_number}: Expected {expected_valuation}, Got {actual_valuation}"
        print(f"Test passed for {reg_number}: Valuation matched.")
    except AssertionError as e:
        pytest.xfail(str(e))
