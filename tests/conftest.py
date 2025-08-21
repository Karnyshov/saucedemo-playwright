import pytest
from playwright.sync_api import Page
from utils.pages_manager import PagesManager

@pytest.fixture
def page_manager(page: Page):
    pages_manager = PagesManager(page)
    yield pages_manager
