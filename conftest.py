import pytest
import os
from playwright.sync_api import sync_playwright
from utils.config import HEADLESS

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)

        if page:
            try:
                os.makedirs("screenshots", exist_ok=True)
                page.screenshot(path=f"screenshots/{item.name}.png")
            except Exception as e:
                print(f"Failed to capture screenshot: {e}")