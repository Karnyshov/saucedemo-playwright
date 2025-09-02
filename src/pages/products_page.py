import random
from playwright.sync_api import Page, expect
from src.pages.base_page import BasePage
from src.pages.product_item import ProductItem
from utils.logger import logger
import re


class ProductsPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.page = page

        self.page_url = self.base_url + "inventory.html"
        self.products_page_title = page.locator("//span[@class=\"title\"]")
        self.product_items_list = page.locator("//div[@class=\"inventory_list\"]")
        self.product_item_element = page.locator("//div[@class=\"inventory_item\"]")

    def open_products_page(self) -> None:
        logger.info(f"Opening Products page")
        self.page.goto(self.page_url)

    def open_about_page(self) -> None:
        logger.info(f"Opening About page from burger menu")
        self.burger_menu_about.click()

    def logout(self) -> None:
        logger.info(f"Logging out as current user")
        self.burger_menu_logout.click()

    def get_all_items(self):
        logger.info(f"Getting all Product Items on page")
        items = []
        for i in range(self.product_item_element.count()):
            items.append(ProductItem(self.page, self.product_item_element.nth(i)))
        return items

    def get_random_item(self) -> ProductItem:
        logger.info(f"Getting random Product Item on page")
        items = self.get_all_items()
        return random.choice(items)

    def get_item(self, position):
        logger.info(f"Getting Product Item by given position")
        items = self.get_all_items()
        return items[position]

    # Leave as static or change? Move to product item POM?
    @staticmethod
    def verify_product_item(product_item: ProductItem) -> None:
        logger.info(f"Verifying given Product Item")
        expect(product_item.image).to_have_attribute("src", re.compile(r"^.+\.(jpg|jpeg)$"))
        expect(product_item.image_link).to_have_attribute("href", "#")
        expect(product_item.item_name_link).to_have_attribute("href", "#")
        expect(product_item.item_name).not_to_be_empty()
        expect(product_item.description).not_to_be_empty()
        expect(product_item.price).not_to_be_empty()
        expect(product_item.price).to_have_text(re.compile(r"^\$(\d{1,3}([ ,.]?\d{3})*|\d+)([.,]\d{1,2})?$"))
        expect(product_item.add_button).to_be_visible()

    def verify_product_items(self, product_items) -> None:
        logger.info(f"Verifying all Product Items on page")
        for item in product_items:
            self.verify_product_item(item)

    # Leave as static or change? Move to product item POM?
    @staticmethod
    def add_to_cart(product_item: ProductItem):
        logger.info(f"Adding given Product Item to cart")
        expect(product_item.remove_button).not_to_be_visible()
        product_item.add_button.click()

    # Leave as static or change? Move to product item POM?
    @staticmethod
    def remove_from_cart(product_item: ProductItem):
        logger.info(f"Removing given Product Item from cart")
        expect(product_item.add_button).not_to_be_visible()
        product_item.remove_button.click()
