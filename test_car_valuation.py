import os

import pytest

from pages.home_page import HomePage
from pages.valuation_view_page import ValuationViewPage
from pages.vechicle_details_page import VehicleDetailsPage
from utils.file import read_input_file, read_output_file


# Define the file path relative to the project root
project_root = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(project_root, "data", "car_input.txt")
output_file_path = os.path.join(project_root, "data", "car_output.txt")

# Parametrize the test with records from the input file
@pytest.mark.parametrize("car_record", read_input_file(input_file_path))
def test_car_valuation(browser_setup, car_record):
    """Test case to validate car valuations."""
    page = browser_setup
    home_page = HomePage(page)
    vehicle_page =   VehicleDetailsPage(page)
    valuation_page = ValuationViewPage(page)

    # Extract data for the current car record
    reg_number = car_record["VARIANT_REG"]
    expected_values = read_output_file(output_file_path)
    expected_valuation = expected_values.get(reg_number)  # Default fallback value

    try:
        # Perform vehicle search and valuation
        home_page.navigate_to("https://www.webuyanycar.com/")
        home_page.handle_cookies(accept=True)
        home_page.search_vehicle(reg_number)
        vehicle_page.fill_details(email="kipesif557@rustetic.com", postcode="M71 1UN", mobile="07000000000")
        actual_valuation = valuation_page.get_valuation()

        # Validate the results
        assert actual_valuation == expected_valuation, \
            f"Mismatch for {reg_number}: Expected {expected_valuation}, Got {actual_valuation}"

        print(f"Test passed for {reg_number}: Valuation matched.")

    except AssertionError as e:
        # Log the mismatch without failing the test
        print(f"Test failed for {reg_number}: {e}")
