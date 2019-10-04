from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    LOGIN_EMAIL = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")
    LOGIN_BUTTON = (By.NAME, "login_submit")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators():
    BOOK_NAME = (By.CSS_SELECTOR, "div h1")
    BOOK_PRICE = (By.CSS_SELECTOR, "[class='col-sm-6 product_main'] [class='price_color']")
    ADD_BUTTON = (By.ID, "add_to_basket_form")
    BASKET_NAME = (By.XPATH, "//div[@id='messages']/div[1]/div/strong")
    BASKET_PRICE = (By.XPATH, "//div[@id][1]//p[1]")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]/div")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "[class='btn-group']")
    BASKET_EMPTY_MESSAGE = (By.ID, "content_inner")


