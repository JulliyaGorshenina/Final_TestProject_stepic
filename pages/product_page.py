from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
from .locators import ProductPageLocators
import math


class ProductPage(BasePage):
    def go_add_to_basket(self):
        adding = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        adding.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        print(answer)
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_add_to_button(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        basket_name = self.browser.find_element(*ProductPageLocators.BASKET_NAME).text
        assert book_name == basket_name

    def should_be_correct_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert book_price in basket_price

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_is_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is disappear"
