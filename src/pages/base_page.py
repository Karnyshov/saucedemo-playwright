from playwright.sync_api import Page
import abc

class BasePage(abc.ABC):
    def __init__(self, page: Page) -> None:
        self.page = page
        self.base_url = "https://www.saucedemo.com/"

        self.logo = self.page.locator("//div[@class='login_logo']")
        self.title = self.page.locator("//title")