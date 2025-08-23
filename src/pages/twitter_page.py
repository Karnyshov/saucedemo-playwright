from playwright.sync_api import Page

from src.pages.base_page import BasePage


class TwitterPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.page = page
        self.page_url = "https://x.com/saucelabs"
        self.page_title = page.locator("//title")