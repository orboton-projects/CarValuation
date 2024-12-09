import os

from pages.home_page import HomePage
from pages.valuation_view_page import ValuationViewPage
from pages.vechicle_details_page import VehicleDetailsPage
from utils.file import read_input_file

# Paths relative to the project root
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
TEST_DATA_FILE_PATH = os.path.join(DATA_DIR, "user_data.txt")
TEST_DATA = read_input_file(TEST_DATA_FILE_PATH)[0]

def navigate_and_handle_cookies(page):
    """
       Perform the steps to navigate and handle cookies.

       Args:
           page: Playwright browser page instance.

       Returns: None
       """
    home_page = HomePage(page)
    home_page.navigate_to("https://www.webuyanycar.com/")
    home_page.handle_cookies(accept=True)

def perform_car_valuation(page, reg_number):
    """
    Perform the steps to validate car valuation for a specific registration number.

    Args:
        page: Playwright browser page instance.
        reg_number: Car registration number to search.

    Returns:
        actual_valuation: The valuation retrieved from the application.
    """
    home_page = HomePage(page)
    vehicle_page = VehicleDetailsPage(page)
    valuation_page = ValuationViewPage(page)

    # Perform steps
    home_page.search_vehicle(reg_number)
    vehicle_page.fill_details(
        email=TEST_DATA["EMAIL"],
        postcode=TEST_DATA["POSTCODE"],
        mobile=TEST_DATA["MOBILE"]
    )
    actual_valuation = valuation_page.get_valuation()

    return actual_valuation
