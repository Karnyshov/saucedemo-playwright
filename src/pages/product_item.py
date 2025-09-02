from playwright.sync_api import Page
from src.pages.base_page import BasePage
from utils.logger import logger

class ProductItem(BasePage):
    def __init__(self, page: Page, base_locator):
        super().__init__(page)
        self.page = page
        self.base_locator = page.locator(base_locator)
        self.image = base_locator.locator("//div[@class=\"inventory_item_img\"]/a/img")
        self.image_link = base_locator.locator("//div[@class=\"inventory_item_img\"]/a")
        self.item_name = base_locator.locator("//div[@class=\"inventory_item_label\"]/a/div")
        self.item_name_link = base_locator.locator("//div[@class=\"inventory_item_label\"]/a")
        self.description = base_locator.locator("//div[@class=\"inventory_item_desc\"]")
        self.price = base_locator.locator("//div[@class=\"inventory_item_price\"]")
        self.price_text = self.price.text_content()
        self.add_button = base_locator.locator("//button[@class=\"btn btn_primary btn_small btn_inventory \"]")
        self.remove_button = base_locator.locator("//button[@class=\"btn btn_secondary btn_small btn_inventory \"]")
