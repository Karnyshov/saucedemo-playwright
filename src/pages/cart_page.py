from playwright.sync_api import Page, expect
from src.pages.base_page import BasePage
from src.pages.cart_item import CartItem
from utils.logger import logger
from urllib.parse import urljoin


class CartPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.page = page
        self.page_url = urljoin(self.base_url, "cart.html")
        self.page_title = page.locator("//span[@class=\"title\"]")
        self.quantity_label = page.locator("//div[@class=\"cart_quantity_label\"]")
        self.description_label = page.locator("//div[@class=\"cart_desc_label\"]")
        self.checkout_button = page.locator("//button[@id=\"checkout\"]")
        self.continue_shopping_button = page.locator("//button[@id=\"continue-shopping\"]")

        self.item_container = page.locator("//div[@class=\"cart_item\"]")
        self.item_quantity = page.locator("//div[@class=\"cart_quantity\"]")
        self.item_name = page.locator("//div[@class=\"inventory_item_name\"]")
        self.item_description = page.locator("//div[@class=\"inventory_item_desc\"]")
        self.item_price = page.locator("//div[@class=\"inventory_item_price\"]")
        self.remove_button = page.locator("//button[@class=\"btn btn_secondary btn_small cart_button\"]")

    def open_checkout_page(self) -> None:
        logger.info("Opening Checkout page")
        self.checkout_button.click()

    def open_products_page(self) -> None:
        logger.info("Returning to Products Page")
        self.continue_shopping_button.click()

    def verify_empty_cart(self) -> None:
        logger.info("Checking item was removed and cart is empty (if 1 item was added)")
        expect(self.item_quantity).not_to_be_visible()
        expect(self.item_name).not_to_be_visible()
        expect(self.item_description).not_to_be_visible()
        expect(self.item_price).not_to_be_visible()
        expect(self.remove_button).not_to_be_visible()
        expect(self.shopping_cart).to_be_visible()
        expect(self.shopping_cart_count).not_to_be_visible()

    def get_all_items(self):
        logger.info(f"Getting all Cart Items on page")
        items = []
        for i in range(self.item_container.count()):
            items.append(CartItem(self.page, self.item_container.nth(i)))
        return items

    def get_item(self, position):
        logger.info(f"Getting Product Item by given position")
        items = self.get_all_items()
        return items[position]