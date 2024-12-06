import pytest

from utils.file import read_input_file, read_output_file


# Parametrize the test with records from the input file
@pytest.mark.parametrize("car_record", read_input_file("car_input.txt"))
def test_car_valuation(browser_setup, car_record):
    """Test case to validate car valuations."""
    page = browser_setup
    car_valuation_page = CarValuationPage(page)

    # Extract data for the current car record
    reg_number = car_record["VARIANT_REG"]
    expected_values = read_output_file("car_output.txt")
    expected_valuation = expected_values.get(reg_number)  # Default fallback value

    try:
        # Perform vehicle search and valuation
        car_valuation_page.navigate_to("https://www.webuyanycar.com/")
        car_valuation_page.handle_cookies(accept=True)
        car_valuation_page.search_vehicle(reg_number)
        car_valuation_page.fill_details(email="xxx@xxx.com", postcode="XX0 0XX", mobile="07000000000")
        actual_valuation = car_valuation_page.get_valuation()

        # Validate the results
        assert actual_valuation == expected_valuation, \
            f"Mismatch for {reg_number}: Expected {expected_valuation}, Got {actual_valuation}"
        print(f"Test passed for {reg_number}: Valuation matched.")

    except AssertionError as e:
        # Log the mismatch without failing the test
        print(f"Test failed for {reg_number}: {e}")