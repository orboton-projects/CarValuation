from pages.bage_page import BasePage


class ValuationViewPage(BasePage):
    """Base Page to contain common methods for all pages."""
    def __init__(self, page):
        super().__init__(page)
        self.page = page


    def get_valuation(self) -> str:
        """Retrieve the valuation result."""
        return self.get_text(
            '[class="container"] [class="row"] [class="amount"]')
        #this locator needs to be moved and updated short.

#TODO All locators needs to be isolated from hardcoded to follow best practice.