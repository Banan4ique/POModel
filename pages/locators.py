from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    ADD_BUTTON = (By.XPATH, "//button[@value='Add to basket']")
    PRODUCT_NAME = (By.XPATH, "//div[contains(@class, 'product_main')]/h1")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'alert-success')]")
    ADDED_MESSAGE = (By.XPATH, "//div[@class='alertinner ']/strong")
    BASKET_PRICE = (By.XPATH, "//div[@class='alertinner ']/p/strong")