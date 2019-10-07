from .pages.basket_page import BasketPage


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_not_be_item()
    page.should_be_empty_message()


