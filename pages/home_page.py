from pages.bage_page import BasePage


class HomePage(BasePage):
    """Base Page to contain common methods for all pages."""
    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def handle_cookies(self, accept: bool = True):
        """Handle cookies banner if present on the page."""
        cookie_banner_selector = "#onetrust-banner-sdk .ot-sdk-container .ot-sdk-row"  # Replace with actual selector
        accept_button_selector = "#onetrust-accept-btn-handler"  # Replace with actual selector
        manage_button_selector = "#onetrust-pc-btn-handler"  # Replace with actual selector
        self.page.wait_for_selector(cookie_banner_selector)
        if self.page.is_visible(cookie_banner_selector):
            if accept:
                self.click_button(accept_button_selector)
            else:
                self.click_button(manage_button_selector)
            print("Cookies banner handled.")

    def search_vehicle(self, reg_number: str, mileage: str = "50000"):
        """Search for vehicle details using registration number and mileage."""
        self.fill_textbox("#vehicleReg", reg_number)  # Adjust selector as per site
        self.fill_textbox("#Mileage", mileage)  # Random mileage
        self.click_button("#btn-go")  # Submit button
        self.page.wait_for_selector("#questions-title")  # Wait for result

        # All locators needs to be isolated from hardcoded to follow best practice.