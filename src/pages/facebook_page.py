from playwright.sync_api import Page


class FacebookPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.page_url = "https://www.facebook.com/saucelabs"
        self.page_title = page.locator("//title")