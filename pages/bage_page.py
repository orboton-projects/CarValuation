class BasePage:
    """Base Page to contain common methods for all pages."""
    def __init__(self, page):
        self.page = page

    def navigate_to(self, url: str):
        """Navigate to a specific URL."""
        self.page.goto(url)

    def fill_textbox(self, selector: str, value: str):
        """Fill a textbox with a given value."""
        self.page.fill(selector, value)

    def click_button(self, selector: str):
        """Click a button."""
        self.page.click(selector)

    def get_text(self, selector: str) -> str:
        """Retrieve text from a given selector."""
        return self.page.inner_text(selector)
