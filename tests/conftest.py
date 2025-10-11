import pytest
from playwright.sync_api import Page
from src.client.sausedemo_ui import SauceDemoUI

@pytest.fixture
def page_manager(page: Page):
    pages_manager = SauceDemoUI(page)
    yield pages_manager

@pytest.fixture(scope = "function")
def login_user(page_manager):
    page_manager.login_page.open_login_page()
    page_manager.login_page.login_standard_user()
    yield page_manager

@pytest.fixture(scope = "function")
def open_first_item(page_manager):
    page_manager.login_page.open_login_page()
    page_manager.login_page.login_standard_user()
    item = page_manager.products_page.get_item(0)
    page_manager.products_page.open_item_page(item.item_name_link)
    yield item

@pytest.fixture(scope = "function")
def open_cart_with_item(page_manager):
    page_manager.login_page.open_login_page()
    page_manager.login_page.login_standard_user()
    item = page_manager.products_page.get_item(0)
    item.add_to_cart()
    page_manager.products_page.open_cart_page()
    yield item

@pytest.fixture(scope = "function")
def open_cart_with_multiple_items(page_manager):
    page_manager.login_page.open_login_page()
    page_manager.login_page.login_standard_user()
    item1 = page_manager.products_page.get_item(0)
    item1.add_to_cart()
    item2 = page_manager.products_page.get_item(1)
    item2.add_to_cart()
    items = [item1, item2]
    page_manager.products_page.open_cart_page()
    yield items

@pytest.fixture(scope = "function")
def open_empty_cart(page_manager):
    page_manager.login_page.open_login_page()
    page_manager.login_page.login_standard_user()
    page_manager.products_page.open_cart_page()
    yield page_manager

@pytest.fixture(scope = "function")
def open_checkout_info_page(page_manager):
    page_manager.login_page.open_login_page()
    page_manager.login_page.login_standard_user()
    item = page_manager.products_page.get_item(0)
    item.add_to_cart()
    page_manager.products_page.open_cart_page()
    page_manager.cart_page.open_checkout_page()
    yield item