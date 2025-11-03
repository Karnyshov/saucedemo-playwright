import random
from playwright.sync_api import Page, expect
from src.pages.base_page import BasePage
from src.pages.product_item import ProductItem
from utils.logger import logger
from urllib.parse import urljoin


class ProductsPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.page = page
        self.page_url = urljoin(self.base_url, "inventory.html")
        self.products_page_title = page.locator("//span[@class=\"title\"]")

        self.product_items_list = page.locator("//div[@class=\"inventory_list\"]")
        self.product_item_element = page.locator("//div[@class=\"inventory_item\"]")

        self.active_sorting = page.locator("//span[@class='active_option']")
        self.sorting_dropdown = page.locator("//select[@class='product_sort_container']")

    def open_products_page(self) -> None:
        logger.info(f"Opening Products page")
        self.page.goto(self.page_url)

    def get_all_items(self):
        logger.info(f"Getting all Product Items on page")
        items = []
        for i in range(self.product_item_element.count()):
            items.append(ProductItem(self.page, self.product_item_element.nth(i)))
        return items

    @staticmethod
    def get_item_names(items) -> list:
        logger.info(f"Getting list of names from Product Items")
        return [item.item_name.inner_text() for item in items]

    @staticmethod
    def get_item_prices(items) -> list:
        logger.info(f"Getting list of prices from Product Items")
        return [float(item.price.inner_text().replace("$","")) for item in items]

    def get_random_item(self) -> ProductItem:
        logger.info(f"Getting random Product Item on page")
        items = self.get_all_items()
        return random.choice(items)

    def get_item(self, position):
        logger.info(f"Getting Product Item by given position")
        items = self.get_all_items()
        return items[position]

    @staticmethod
    def verify_product_items(product_items) -> None:
        logger.info(f"Verifying all Product Items on page")
        for item in product_items:
            item.verify_product_item()

    def select_sorting(self, sorting_option) -> None:
        logger.info(f"Applying provided sorting to Product Items on the page: {sorting_option}")
        self.sorting_dropdown.select_option(value = sorting_option.value)

    def verify_sorting(self, sorting_option) -> None:
        logger.info(f"Checking if Product Items are sorted by provided option: {sorting_option}")

        items = self.get_all_items()
        match sorting_option.value:
            case "az":
                item_names = self.get_item_names(items)
                assert all(item_names[i] <= item_names[i+1] for i in range(len(item_names) - 1))
            case "za":
                item_names = self.get_item_names(items)
                assert all(item_names[i] >= item_names[i + 1] for i in range(len(item_names) - 1))
            case "lohi":
                item_prices = self.get_item_prices(items)
                assert all(item_prices[i] <= item_prices[i + 1] for i in range(len(item_prices) - 1))
            case "hilo":
                item_prices = self.get_item_prices(items)
                assert all(item_prices[i] >= item_prices[i + 1] for i in range(len(item_prices) - 1))

    @staticmethod
    def open_item_page(locator) -> None:
        logger.info(f"Opening Item Details page by locator (image/name): {locator}")
        locator.click()

    def open_cart_page(self) -> None:
        logger.info(f"Opening Cart page")
        self.shopping_cart.click()

    def verify_basic_state(self):
        logger.info("Checking basic state of the page")
        expect(self.active_sorting).to_have_text("Name (A to Z)")
        expect(self.products_page_title).to_have_text("Products")
        expect(self.product_item_element).not_to_have_count(0)