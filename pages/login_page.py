from .locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url

    def should_be_login_form(self):
        self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"
        assert True

    def should_be_register_form(self):
        self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"
        assert True

    def register_new_user(self, email, password):
        register_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        register_email.send_keys(email)
        register_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        register_password.send_keys(password)
        register_confirm_password = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
        register_confirm_password.send_keys(password)
        end_register = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        end_register.click()


