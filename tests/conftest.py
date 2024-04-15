import pytest
from selene import browser

LOGIN = "example1200@example.com"
PASSWORD = "123456"
API_URL = "https://demowebshop.tricentis.com/"


@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser.config.window_width = 1000
    browser.config.window_height = 2000
    browser.config.base_url = API_URL

    yield

    browser.quit()
