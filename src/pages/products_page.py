from playwright.sync_api import Page, expect

from src.pages.about_page import AboutPage
from src.pages.base_page import BasePage
#from src.pages.login_page import LoginPage
from utils.logger import logger

class ProductsPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.page = page
        self.page_url = self.base_url + "inventory.html"

        self.products_page_title = page.locator("//span[@class=\"title\"]")

    def open_products_page(self) -> None:
        logger.info(f"Opening Products page")
        self.page.goto(self.page_url)

    def open_about_page(self) -> AboutPage:
        self.burger_menu_about.click()
        return AboutPage(self.page)

    # def logout(self) -> LoginPage:
    #     self.burger_menu_logout.click()
    #     return LoginPage(self.page)