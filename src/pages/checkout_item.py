from playwright.sync_api import Page, expect
from src.pages.base_page import BasePage
from utils.logger import logger

class CheckoutItem(BasePage):
    def __init__(self, page: Page, base_locator):
        super().__init__(page)
        self.page = page
        self.base_locator = page.locator(base_locator)
        self.item_quantity = base_locator.locator("//div[@class='cart_quantity']")
        self.item_name = base_locator.locator("//div[@class='inventory_item_name']")
        self.item_description = base_locator.locator("//div[@class='inventory_item_desc']")
        self.item_price = base_locator.locator("//div[@class='inventory_item_price']")

        self.quantity = self.item_quantity.text_content()
        self.name = self.item_name.text_content()
        self.description = self.item_description.text_content()
        self.price = self.item_price.text_content()

    def verify_content(self, cart_item):
        logger.info("Verifying Checkout Item identical to Cart Item: name, description, price")
        expect(self.item_name).to_have_text(cart_item.item_name_text)
        expect(self.item_description).to_have_text(cart_item.description_text)
        expect(self.item_price).to_have_text(cart_item.price_text)

    def verify_checkout_item(self) -> None:
        logger.info("Checking item is present in cart")
        expect(self.item_quantity).not_to_be_empty()
        expect(self.item_name).not_to_be_empty()
        expect(self.item_description).not_to_be_empty()
        expect(self.item_price).not_to_be_empty()