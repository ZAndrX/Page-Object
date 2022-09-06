from selenium.webdriver.common.by import By


class MainPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_ITEM=(By.CSS_SELECTOR, ".product_main>h1")
    PRICE_ITEM=(By.CSS_SELECTOR, "div.product_main >.price_color")


class MsgPageLocators():
    MSG_NAME_ITEM=(By.CSS_SELECTOR,".alertinner>strong")
    MSG_PRICE_ITEM = (By.CSS_SELECTOR, ".alertinner > p > strong")
    SUCCESS_MESSAGE =(By.CSS_SELECTOR, ".alert")


