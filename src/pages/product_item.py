from playwright.sync_api import Page, expect
from src.pages.base_page import BasePage
from utils.logger import logger
import re

class ProductItem(BasePage):
    def __init__(self, page: Page, base_locator):
        super().__init__(page)
        self.page = page
        self.base_locator = page.locator(base_locator)
        self.image = base_locator.locator("//div[@class=\"inventory_item_img\"]/a/img")
        self.image_link = base_locator.locator("//div[@class=\"inventory_item_img\"]/a")
        self.item_name = base_locator.locator("//div[@class=\"inventory_item_label\"]/a/div")
        self.item_name_link = base_locator.locator("//div[@class=\"inventory_item_label\"]/a")
        self.description = base_locator.locator("//div[@class=\"inventory_item_desc\"]")
        self.price = base_locator.locator("//div[@class=\"inventory_item_price\"]")
        self.add_button = base_locator.locator("//button[@class=\"btn btn_primary btn_small btn_inventory \"]")
        self.remove_button = base_locator.locator("//button[@class=\"btn btn_secondary btn_small btn_inventory \"]")

        self.item_id = self.get_item_id()
        self.price_text = self.price.text_content()
        self.item_name_text = self.item_name.text_content()
        self.description_text =  self.description.text_content()
        self.image_src = self.image.get_attribute("src")

    def verify_product_item(self) -> None:
        logger.info("Verifying given Product Item")
        expect(self.image).to_have_attribute("src", re.compile(r"^.+\.(jpg|jpeg)$"))
        expect(self.image_link).to_have_attribute("href", "#")
        expect(self.item_name_link).to_have_attribute("href", "#")
        expect(self.item_name).not_to_be_empty()
        expect(self.description).not_to_be_empty()
        expect(self.price).not_to_be_empty()
        expect(self.price).to_have_text(re.compile(r"^\$(\d{1,3}([ ,.]?\d{3})*|\d+)([.,]\d{1,2})?$"))
        expect(self.add_button).to_be_visible()

    def add_to_cart(self):
        logger.info("Adding given Product Item to cart")
        expect(self.remove_button).not_to_be_visible()
        self.add_button.click()

    def remove_from_cart(self):
        logger.info("Removing given Product Item from cart")
        expect(self.add_button).not_to_be_visible()
        self.remove_button.click()

    def verify_item_added_to_cart(self):
        logger.info("Verifying item is added to cart: remove button replaces add button")
        expect(self.remove_button).to_be_visible()
        expect(self.add_button).not_to_be_visible()

    def verify_item_removed_from_cart(self):
        logger.info("Verifying item is added to cart: add button replaces remove button")
        expect(self.add_button).to_be_visible()
        expect(self.remove_button).not_to_be_visible()

    def get_item_id(self):
        attribute = self.item_name_link.get_attribute("id")
        return attribute.split("_")[1]