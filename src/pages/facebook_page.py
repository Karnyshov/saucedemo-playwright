from playwright.sync_api import Page
from src.pages.base_page import BasePage


class FacebookPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.page = page
        self.page_url = "https://www.facebook.com/saucelabs"
        self.page_title = page.locator("//title")