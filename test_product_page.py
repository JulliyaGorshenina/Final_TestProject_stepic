import time
import pytest
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page_link = "http://selenium1py.pythonanywhere.com"
        page = LoginPage(browser, login_page_link)
        page.open()
        page.go_to_login_page()
        page.register_new_user(str(time.time())+"@fakemail.org", "Q7877797989756")
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.go_add_to_basket()
