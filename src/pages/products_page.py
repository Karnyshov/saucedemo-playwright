from playwright.sync_api import Page
from src.pages.base_page import BasePage
from utils.logger import logger


class ProductsPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.page = page
        self.page_url = self.base_url + "inventory.html"

        self.products_page_title = page.locator("//span[@class=\"title\"]")

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
        pass

    def get_random_item(self):
        pass

    def add_to_cart(self):
        pass

    def remove_from_cart(self):
        pass