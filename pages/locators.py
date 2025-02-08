from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//a[@class='btn btn-default']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_HEADER = (By.XPATH, "//div[contains(h1, 'Basket')]")
    BASKET_CONTENT = (By.ID, "basket_formset")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner p")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators():
    ADD_BUTTON = (By.XPATH, "//button[@value='Add to basket']")
    PRODUCT_NAME = (By.XPATH, "//div[contains(@class, 'product_main')]/h1")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'alert-success')]")
    ADDED_MESSAGE = (By.XPATH, "//div[@class='alertinner ']/strong")
    BASKET_PRICE = (By.XPATH, "//div[@class='alertinner ']/p/strong")