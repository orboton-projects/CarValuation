import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser_setup():
    """Fixture to initialize and clean up Playwright browser."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()
