import requests
from selene import browser, have
import allure

from tests.conftest import API_URL, LOGIN, PASSWORD
from tests.utils import log_post_request


def test_add_to_cart_laptop():
    with allure.step("Get user cookie"):
        response = log_post_request(url=API_URL + "login", data={"Email": LOGIN, "Password": PASSWORD},
                                    allow_redirects=False)
        cookie = response.cookies.get("NOPCOMMERCE.AUTH")

    with allure.step("Add product to user's cart"):
        add_to_cart_url = "https://demowebshop.tricentis.com/addproducttocart/catalog/31/1/1"
        requests.post(add_to_cart_url, cookies={"NOPCOMMERCE.AUTH": cookie})

    with allure.step("Open cart page"):
        browser.open("https://demowebshop.tricentis.com")
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
        browser.open("https://demowebshop.tricentis.com/cart")

    with allure.step("Check item in cart"):
        browser.all(".cart-item-row")[-1].element(".qty-input").should(have.value('1'))

    with allure.step("Remove item from cart"):
        browser.all(".remove-from-cart")[-1].element('input[type="checkbox"]').click()
        browser.element(".button-2.update-cart-button").click()
