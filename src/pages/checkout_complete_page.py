from playwright.sync_api import Page,expect,Locator
from src.pages.base_page import BasePage
from utils.logger import logger
from urllib.parse import urljoin


class CheckoutCompletePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.page = page

        self.page_title = page.locator("//span[@class=\"title\"]")
        self.back_to_home_button = page.locator("")
        self.success_image = page.locator("")
        self.success_label = page.locator("")
        self.success_text = page.locator("")

    def open_products_page(self):
        pass
