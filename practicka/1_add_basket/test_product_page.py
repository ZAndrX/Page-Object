import pytest

from page.product_page import MainPage, BasketPage

@pytest.mark.login_guest
class TestLoginFromMainPage():
    # не забываем передать первым аргументом self
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser,link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page()

def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        login_page = page.go_to_login_page()
        login_page.should_be_login_page()

@pytest.mark.skip
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = MainPage(browser, link)
    page.open()
    page.add_in_basket()
    page.solve_quiz_and_get_code()
    page.should_msg_add()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser,
                                                                       link="http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"):
    page = MainPage(browser, link)
    page.open()
    page.add_in_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser,
                                        link="http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"):
    page = MainPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser,
                                                            link="http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"):
    page = MainPage(browser, link)
    page.open()
    page.add_in_basket()
    page.should_is_disappeared_msg()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0","http://selenium1py.pythonanywhere.com/"])
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, link):
    page = BasketPage(browser, link)
    page.open()
    page.open_basket()
    page.should_basket_is_empty()