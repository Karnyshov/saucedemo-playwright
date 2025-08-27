import pytest
from playwright.sync_api import Page
from src.client.sausedemo_ui import SauceDemoUI

@pytest.fixture
def page_manager(page: Page):
    pages_manager = SauceDemoUI(page)
    yield pages_manager
