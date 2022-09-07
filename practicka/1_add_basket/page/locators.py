from selenium.webdriver.common.by import By


class MainPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_ITEM = (By.CSS_SELECTOR, ".product_main>h1")
    PRICE_ITEM = (By.CSS_SELECTOR, "div.product_main >.price_color")
    BASKET_BTN = (By.CSS_SELECTOR, ".btn-group>a.btn-default")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class MsgPageLocators:
    MSG_NAME_ITEM = (By.CSS_SELECTOR, ".alertinner>strong")
    MSG_PRICE_ITEM = (By.CSS_SELECTOR, ".alertinner > p > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert")

class BasketPageLocators:
    MSG_STATUS=(By.CSS_SELECTOR, "#content_inner>p")
    ITEM_IN_BASKET=(By.CSS_SELECTOR, ".basket-items")

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, 'input#id_registration-email')
    REGISTER_FORM_PASSWORD_1= (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_FORM_PASSWORD_2 = (By.CSS_SELECTOR, '#id_registration-password2')
    BTN_CONFIRM_REGISTER=(By.CSS_SELECTOR,"[name=registration_submit]")