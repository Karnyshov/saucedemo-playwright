from playwright.sync_api import Page


class AboutPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.page_url = "https://saucelabs.com/"
        self.page_title = page.locator("//title")