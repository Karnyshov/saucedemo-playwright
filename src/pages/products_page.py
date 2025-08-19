from playwright.sync_api import Page, Locator, expect

class ProductPage:

    def __init__(self, page: Page) -> None:
        self.page = page
