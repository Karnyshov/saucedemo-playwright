from playwright.sync_api import Page

from src.pages.about_page import AboutPage
from src.pages.login_page import LoginPage
from src.pages.products_page import ProductsPage


class PagesManager:
    def __init__(self, page: Page):
        self.login_page = LoginPage(page)
        self.products_page = ProductsPage(page)
        self.about_page = AboutPage(page)