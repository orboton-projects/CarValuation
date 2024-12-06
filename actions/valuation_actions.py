from pages.home_page import HomePage
from pages.valuation_view_page import ValuationViewPage
from pages.vechicle_details_page import VehicleDetailsPage

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
    home_page.navigate_to("https://www.webuyanycar.com/")
    home_page.handle_cookies(accept=True)
    home_page.search_vehicle(reg_number)
    vehicle_page.fill_details(
        email="xyz@xyz.com",
        postcode="AB1 1XY",
        mobile="07000000000"
    )
    actual_valuation = valuation_page.get_valuation()

    return actual_valuation
