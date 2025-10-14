from playwright.sync_api import Page,expect,Locator
from src.pages.base_page import BasePage
from src.pages.checkout_item import CheckoutItem
from utils.logger import logger
from urllib.parse import urljoin
from decimal import Decimal
import re

class CheckoutOverviewPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.page = page

        self.page_title = page.locator("//span[@class=\"title\"]")
        self.quantity_label = page.locator("//div[@class='cart_quantity_label']")
        self.description_label = page.locator("//div[@class='cart_desc_label']")
        self.item_container = page.locator("//div[@class='cart_item']")

        self.payment_info_label = page.locator("//div[@data-test='payment-info-label']")
        self.payment_info = page.locator("//div[@data-test='payment-info-value']")
        self.shipping_info_label = page.locator("//div[@data-test='shipping-info-label']")
        self.shipping_info = page.locator("//div[@data-test='shipping-info-value']")
        self.price_total_label = page.locator("//div[@data-test='total-info-label']")
        self.price_item_total_value = page.locator("//div[@data-test='subtotal-label']")
        self.price_tax_value = page.locator("//div[@data-test='tax-label']")
        self.price_total_value = page.locator("//div[@data-test='total-label']")

        self.cancel_button = page.locator("//button[@id='cancel']")
        self.finish_button = page.locator("//button[@id='finish']")

    def cancel_checkout(self):
        logger.info("Cancelling checkout, returning to Products page")
        self.cancel_button.click()

    def finish_checkout(self):
        pass

    def get_all_items(self):
        logger.info(f"Getting all Checkout Items on page")
        items = []
        for i in range(self.item_container.count()):
            items.append(CheckoutItem(self.page, self.item_container.nth(i)))
        return items

    def get_item(self, position):
        logger.info(f"Getting Checkout Item by given position")
        items = self.get_all_items()
        return items[position]

    @staticmethod
    def get_price_value(locator: Locator):
        price_str = re.search(r"\d+\.\d+", locator.text_content()).group()
        return Decimal(price_str)

    def verify_prices(self, checkout_item: CheckoutItem):
        item_price = self.get_price_value(self.price_item_total_value)
        tax_price = self.get_price_value(self.price_tax_value)
        total_price = self.get_price_value(self.price_total_value)
        checkout_item_price = self.get_price_value(checkout_item.item_price)

        assert item_price == checkout_item_price
        assert total_price - item_price == tax_price
        assert item_price + tax_price == total_price
    
    def verify_basic_state_single_item(self):
        expect(self.page_title).to_be_visible()
        expect(self.page_title).to_have_text("Checkout: Overview")
        expect(self.item_container).to_be_visible()
        expect(self.item_container).not_to_be_empty()
        expect(self.quantity_label).not_to_be_empty()
        expect(self.description_label).not_to_be_empty()
        expect(self.payment_info_label).not_to_be_empty()
        expect(self.payment_info).not_to_be_empty()
        expect(self.shipping_info_label).not_to_be_empty()
        expect(self.shipping_info).not_to_be_empty()
        expect(self.price_total_label).not_to_be_empty()
        expect(self.price_item_total_value).not_to_be_empty()
        expect(self.price_tax_value).not_to_be_empty()
        expect(self.price_total_value).not_to_be_empty()
        expect(self.cancel_button).to_be_visible()
        expect(self.finish_button).to_be_visible()
        expect(self.shopping_cart_count).to_have_text("1")

    def verify_basic_state_two_items(self):
        expect(self.page_title).to_be_visible()
        expect(self.page_title).to_have_text("Checkout: Overview")
        expect(self.item_container).to_have_count(2)
        expect(self.quantity_label).not_to_be_empty()
        expect(self.description_label).not_to_be_empty()
        expect(self.payment_info_label).not_to_be_empty()
        expect(self.payment_info).not_to_be_empty()
        expect(self.shipping_info_label).not_to_be_empty()
        expect(self.shipping_info).not_to_be_empty()
        expect(self.price_total_label).not_to_be_empty()
        expect(self.price_item_total_value).not_to_be_empty()
        expect(self.price_tax_value).not_to_be_empty()
        expect(self.price_total_value).not_to_be_empty()
        expect(self.cancel_button).to_be_visible()
        expect(self.finish_button).to_be_visible()
        expect(self.shopping_cart_count).to_have_text("2")

        for i in range(self.item_container.count()):
            expect(self.item_container.nth(i)).to_be_visible()
            expect(self.item_container.nth(i)).not_to_be_empty()