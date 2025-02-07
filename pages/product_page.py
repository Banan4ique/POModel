from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()

    def should_be_same_name(self):
        message = self.browser.find_element(*ProductPageLocators.ADDED_MESSAGE).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_name == message, \
            f"Название товара {product_name} не совпадает с названием в корзине {message}"

    def should_be_same_price(self):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert basket_price == product_price, \
            f"Цена товара {product_price} не совпадает с ценой в корзине {basket_price}"