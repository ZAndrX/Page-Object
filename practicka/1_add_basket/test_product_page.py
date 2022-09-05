import time

from page.product_page import MainPage


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link)
    page.open()
    page.add_in_basket()