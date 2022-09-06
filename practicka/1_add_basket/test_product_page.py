import time

from page.product_page import MainPage


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = MainPage(browser, link)
    page.open()
    page.add_in_basket()
    page.solve_quiz_and_get_code()
    page.should_msg_add()