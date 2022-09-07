from .base_page import BasePage
from .locators import MainPageLocators
from .locators import MsgPageLocators
from .locators import BasketPageLocators
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def add_in_basket(self):
        link = self.browser.find_element(*MainPageLocators.BASKET_LINK)
        link.click()

    def should_msg_add(self):
        self.check_name()
        self.check_price()

    def check_name(self):
        assert self.return_atribbute_el(*MainPageLocators.NAME_ITEM)==self.return_atribbute_el(*MsgPageLocators.MSG_NAME_ITEM), "Msg name is missing on the page"

    def check_price(self):
        assert self.return_atribbute_el(*MainPageLocators.PRICE_ITEM)==self.return_atribbute_el(*MsgPageLocators.MSG_PRICE_ITEM), "Msg price is missing on the page"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*MsgPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_is_disappeared_msg(self):
        assert self.is_disappeared(*MsgPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should not be"

    def open_basket(self):
        btn_basket=self.browser.find_element(*MainPageLocators.BASKET_BTN)
        btn_basket.click()

class BasketPage(BasePage):
    def open_basket(self):
        btn_basket=self.browser.find_element(*MainPageLocators.BASKET_BTN)
        btn_basket.click()
    def should_basket_is_empty(self):
        self.check_msg_empty()
        self.items_not_in_basket()

    def check_msg_empty(self):
        assert self.return_atribbute_el(*BasketPageLocators.MSG_STATUS)=="Your basket is empty. Continue shopping", "Msg empty is missing on the page"

    def items_not_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_IN_BASKET), "Basket isn't empty"

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.url == "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/", "url isn't right"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is missing on the page"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is missing on the page"

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK)
