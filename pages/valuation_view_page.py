from pages.bage_page import BasePage


class ValuationViewPage(BasePage):
    """Base Page to contain common methods for all pages."""
    def __init__(self, page):
        super().__init__(page)
        self.page = page


    def get_valuation(self) -> str:
        """Retrieve the valuation result."""
        return self.get_text(
            ".col-12.col-lg-3.d-none.d-sm-block.order-1.page-header > div > div.d-none.d-lg-block > div > div")
