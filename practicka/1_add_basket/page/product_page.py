from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def add_in_basket(self):
        link = self.browser.find_element(*MainPageLocators.BASKET_LINK)
        link.click()
