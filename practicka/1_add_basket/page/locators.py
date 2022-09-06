from selenium.webdriver.common.by import By


class MainPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_ITEM = (By.CSS_SELECTOR, ".product_main>h1")
    PRICE_ITEM = (By.CSS_SELECTOR, "div.product_main >.price_color")
    BASKET_BTN = (By.CSS_SELECTOR, ".btn-group>a.btn-default")


class MsgPageLocators:
    MSG_NAME_ITEM = (By.CSS_SELECTOR, ".alertinner>strong")
    MSG_PRICE_ITEM = (By.CSS_SELECTOR, ".alertinner > p > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert")

class BasketPageLocators:
    MSG_STATUS=(By.CSS_SELECTOR, "#content_inner>p")
    ITEM_IN_BASKET=(By.CSS_SELECTOR, ".basket-items")