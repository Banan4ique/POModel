from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_header()

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "Incorrect url"

    def should_be_basket_header(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_HEADER), "Basket header is not presented"

    def should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTENT), "Basket isn't empty"

    def should_be_empty_text(self):
        text = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT).text
        assert "Your basket is empty." in text, f"There is no text about basket emptiness instead: {text}"

