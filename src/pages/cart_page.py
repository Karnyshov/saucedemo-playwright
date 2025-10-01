from playwright.sync_api import Page, expect
from src.pages.base_page import BasePage
from utils.logger import logger
from urllib.parse import urljoin


class CartPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.page = page
        self.page_url = urljoin(self.base_url, "cart.html")
        self.page_title = page.locator("//span[@class=\"title\"]")
        self.quantity_label = page.locator("//div[@class=\"cart_quantity_label\"]")
        self.description_label = page.locator("//div[@class=\"cart_desc_label\"]")
        self.checkout_button = page.locator("//button[@id=\"checkout\"]")
        self.continue_shopping_button = page.locator("//button[@id=\"continue-shopping\"]")

        self.item_quantity = page.locator("//div[@class=\"cart_quantity\"]")
        self.item_name = page.locator("//div[@class=\"inventory_item_name\"]")
        self.item_description = page.locator("//div[@class=\"inventory_item_desc\"]")
        self.item_price = page.locator("//div[@class=\"inventory_item_price\"]")
        self.remove_button = page.locator("//button[@id=\"remove-sauce-labs-bike-light\"]")
