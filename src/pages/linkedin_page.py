from playwright.sync_api import Page
from src.pages.base_page import BasePage


class LinkedInPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.page = page
        self.page_url = "https://www.linkedin.com/company/sauce-labs/"
        self.page_title = page.locator("//title")