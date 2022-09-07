import pytest
import time
from page.product_page import MainPage, BasketPage
from page.login_page import LoginPage


class TestLoginFromMainPage():
    # не забываем передать первым аргументом self
    def test_guest_can_go_to_login_page_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
            link = "http://selenium1py.pythonanywhere.com/"
            page = MainPage(browser, link)
            page.open()
            page= LoginPage(browser, link)
            login_page = page.go_to_login_page()
            login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = MainPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()


@pytest.mark.need_review
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser,
                                                                       link="http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"):
    page = MainPage(browser, link)
    page.open()
    page.add_in_basket()
    page.should_not_be_success_message()

class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password =str(time.time())
        page=LoginPage(browser, "https://selenium1py.pythonanywhere.com/")
        page.open()
        page.go_to_login_page()
        page.register_new_user(email,password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"):
        page = MainPage(browser, link)
        page.open()
        page.add_in_basket()
        page.should_msg_add()

    def test_user_cant_see_success_message(self, browser,
                                            link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"):
        page = MainPage(browser, link)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(self, browser,
                                                            link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"):
    page = MainPage(browser, link)
    page.open()
    page.add_in_basket()
    page.should_is_disappeared_msg()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"):
    page = BasketPage(browser, link)
    page.open()
    page.open_basket()
    page.should_basket_is_empty()