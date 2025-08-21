from playwright.sync_api import Page


class TwitterPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.page_url = "https://x.com/saucelabs"
        self.page_title = page.locator("//title")