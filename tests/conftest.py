import pytest
from playwright.sync_api import Page
from src.pages.login_page import LoginPage

@pytest.fixture
def open_login_page(page: Page):
    login_page = LoginPage(page)
    login_page.open_login_page()
    yield login_page