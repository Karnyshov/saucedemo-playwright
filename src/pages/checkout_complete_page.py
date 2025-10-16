from playwright.sync_api import Page,expect,Locator
from src.pages.base_page import BasePage
from utils.logger import logger
from urllib.parse import urljoin


class CheckoutCompletePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.page = page