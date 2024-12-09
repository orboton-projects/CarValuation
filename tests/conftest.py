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

@pytest.fixture(scope="function", autouse=True)
def capture_artifacts(request, browser_setup):
    """Captures screenshots, recordings, and logs on failure."""
    page = browser_setup

    yield

    if request.node.rep_call.failed:
        # Take Screenshot on Failure
        screenshot_file = f"screenshots/{request.node.name}.png"
        page.screenshot(path=screenshot_file)
        print(f"::error::Screenshot saved at {screenshot_file}")

        # Start/Stop Video Recording
        video_file = f"recordings/{request.node.name}.webm"
        page.context.new_page().video.start(path=video_file)
        print(f"::error::Recording saved at {video_file}")

