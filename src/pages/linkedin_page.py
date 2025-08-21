from playwright.sync_api import Page


class LinkedInPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.page_url = "https://www.linkedin.com/company/sauce-labs/"
        self.page_title = page.locator("//title")