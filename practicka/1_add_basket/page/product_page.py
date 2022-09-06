from .base_page import BasePage
from .locators import MainPageLocators
from .locators import MsgPageLocators
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