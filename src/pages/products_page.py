from playwright.sync_api import Page, expect
from src.pages.base_page import BasePage
from utils.logger import logger

class ProductPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.page = page
        self.page_url = self.base_url + "inventory.html"

        self.products_page_title = page.locator("//span[@class=\"title\"]")

    def open_products_page(self) -> None:
        logger.info(f"Opening Products page")
        self.page.goto(self.page_url)