from pages.bage_page import BasePage


class HomePage(BasePage):
    """Base Page to contain common methods for all pages."""
    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def handle_cookies(self, accept: bool = True):
        """Handle cookies banner if present on the page."""
        accept_button_selector = "#onetrust-accept-btn-handler"
        manage_button_selector = "#onetrust-pc-btn-handler"
        self.page.wait_for_selector(accept_button_selector)
        if self.page.is_visible(accept_button_selector):
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