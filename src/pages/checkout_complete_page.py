from playwright.sync_api import Page,expect
from src.pages.base_page import BasePage
from utils.logger import logger

class CheckoutCompletePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.page = page

        self.page_title = page.locator("//span[@class='title']")
        self.back_to_home_button = page.locator("//button[@id='back-to-products']")
        self.complete_image = page.locator("//img[@class='pony_express']")
        self.complete_header = page.locator("//h2[@class='complete-header']")
        self.complete_text = page.locator("//div[@class='complete-text']")

    def open_products_page(self):
        logger.info("Pressing Back to Home button and opening Products page")
        self.back_to_home_button.click()

    def verify_basic_state(self):
        logger.info("Checking basic state of Checkout Complete page")
        expect(self.complete_image).to_be_visible()
        expect(self.complete_header).to_be_visible()
        expect(self.complete_text).to_be_visible()
        expect(self.back_to_home_button).to_be_visible()

    def verify_image(self):
        logger.info("Checking that image source is not empty and loaded")
        expect(self.complete_image).to_be_visible()
        assert self.complete_image.evaluate("(img) => img.complete && img.naturalWidth > 0 && img.naturalHeight > 0")