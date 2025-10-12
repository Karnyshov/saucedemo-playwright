from playwright.sync_api import Page, expect
from src.pages.base_page import BasePage
from utils.logger import logger
from urllib.parse import urljoin

class CheckoutOverviewPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.page = page

        self.page_title = page.locator("//span[@class=\"title\"]")
        self.quantity_label = page.locator("")

        self.description_label = page.locator("")
        self.payment_info_label = page.locator("")
        self.payment_info = page.locator("")
        self.shipping_info_label = page.locator("")
        self.shipping_info = page.locator("")
        self.price_total_label = page.locator("")
        self.price_item_total_value = page.locator("")
        self.price_tax_value = page.locator("")
        self.price_total_value = page.locator("")

        self.cancel_button = page.locator("")
        self.finish_button = page.locator("")

    def cancel_checkout(self):
        pass

    def finish_checkout(self):
        pass