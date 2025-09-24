from playwright.sync_api import Page, expect
from src.pages.base_page import BasePage
from utils.logger import logger
from urllib.parse import urljoin
import re


class ItemPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.page = page
        #self.page_url = urljoin(self.base_url, "inventory-item.html")
        self.image = page.locator("//img[@class=\"inventory_details_img\"]")
        self.item_name = page.locator("//div[@class=\"inventory_details_name large_size\"]")
        self.description = page.locator("//div[@class=\"inventory_details_desc large_size\"]")
        self.price = page.locator("//div[@class=\"inventory_details_price\"]")
        self.add_button = page.locator("//button[@name=\"add-to-cart\"]")
        self.remove_button = page.locator("//button[@name=\"remove\"]")
        self.back_to_products_button = page.locator("//button[@id=\"back-to-products\"]")

    def add_to_cart(self):
        logger.info("Adding Product Item to cart")
        expect(self.remove_button).not_to_be_visible()
        self.add_button.click()

    def remove_from_cart(self):
        logger.info("Removing Product Item from cart")
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

    def back_to_products_page(self):
        logger.info("Moving back to Product items page")
        self.back_to_products_button.click()

    def verify_basic_state(self):
        logger.info("Checking basic state of Product Item details page")
        expect(self.image).to_have_attribute("src",re.compile(r"^.+\.(jpg|jpeg)$"))
        expect(self.item_name).not_to_be_empty()
        expect(self.description).not_to_be_empty()
        expect(self.price).not_to_be_empty()
        expect(self.price).to_have_text(re.compile(r"^\$(\d{1,3}([ ,.]?\d{3})*|\d+)([.,]\d{1,2})?$"))
        expect(self.add_button).to_be_visible()

    def verify_url(self):
        logger.info(f"Checking page URL is valid: {self.page.url}")
        expect(self.page).to_have_url(re.compile("^https?://(www\.)?saucedemo\.com/inventory-item\.html\?id=\d+$"))