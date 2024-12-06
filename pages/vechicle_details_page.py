from pages.bage_page import BasePage


class VehicleDetailsPage(BasePage):
    """Vehicle DetailsPage to contain related methods and objects."""
    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def fill_details(self, email: str, postcode: str, mobile: str):
        """Fill out the 'Your details' form with email, postcode, and mobile number."""
        self.fill_textbox("#EmailAddress", email)
        self.fill_textbox("#Postcode", postcode)
        self.fill_textbox("#TelephoneNumber", mobile)
        self.click_button("#advance-btn")

        #All locators needs to be isolated from hardcoded to follow best practice.