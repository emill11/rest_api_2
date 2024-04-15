import pytest
from selene import browser

LOGIN = "example1200@example.com"
PASSWORD = "123456"
API_URL = "https://demowebshop.tricentis.com/"


@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser.config.base_url = "https://demowebshop.tricentis.com/"

    yield

    browser.quit()
