import pytest
from playwright.sync_api import Page
from src.pages.login_page import LoginPage
from src.pages.products_page import ProductsPage

@pytest.fixture
def open_login_page(page: Page):
    login_page = LoginPage(page)
    login_page.open_login_page()
    yield login_page

@pytest.fixture
def open_products_page(page: Page):
    login_page = LoginPage(page)
    login_page.login_standard_user()
    products_page = ProductsPage(page)
    products_page.open_products_page()
    yield products_page