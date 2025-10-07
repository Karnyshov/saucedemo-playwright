from playwright.sync_api import Page, expect
from src.pages.base_page import BasePage
from utils.logger import logger
from urllib.parse import urljoin

class CheckoutInfoPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.page = page
        self.page_title = page.locator("//span[@class=\"title\"]")
        self.cancel_button = page.locator("//button[@id=\"cancel\"]")
        self.continue_button = page.locator("//input[@id=\"continue\"]")
        self.first_name_field = page.locator("//input[@id=\"first-name\"]")
        self.last_name_field = page.locator("//input[@id=\"last-name\"]")
        self.postal_code_field = page.locator("//input[@id=\"postal-code\"]")

    def verify_first_name_field(self):
        logger.info("Checking First Name field: visibility, placeholder")
        expect(self.first_name_field).to_be_visible()
        expect(self.first_name_field).to_be_editable()
        expect(self.first_name_field).to_have_attribute("placeholder", "First Name")

    def verify_last_name_field(self):
        logger.info("Checking Last Name field: visibility, placeholder")
        expect(self.last_name_field).to_be_visible()
        expect(self.last_name_field).to_be_editable()
        expect(self.last_name_field).to_have_attribute("placeholder", "Last Name")

    def verify_postal_code_field(self):
        logger.info("Checking Postal Code field: visibility, placeholder")
        expect(self.postal_code_field).to_be_visible()
        expect(self.postal_code_field).to_be_editable()
        expect(self.postal_code_field).to_have_attribute("placeholder", "Zip/Postal Code")

    def verify_continue_button(self):
        logger.info("Checking Continue button: visibility, clickable")
        expect(self.continue_button).to_be_visible()
        expect(self.continue_button).to_be_enabled()

    def verify_cancel_button(self):
        logger.info("Checking Cancel button: visibility, clickable")
        expect(self.cancel_button).to_be_visible()
        expect(self.cancel_button).to_be_enabled()

    def cancel_checkout(self):
        logger.info("Cancelling checkout, opening Cart page")
        self.cancel_button.click()

    def continue_checkout(self):
        logger.info("Continue checkout, opening Checkout Overview page")
        self.continue_button.click()

    def input_first_name(self, text):
        logger.info(f"Typing a First Name: {text}")
        self.first_name_field.fill(text)

    def input_last_name(self, text):
        logger.info(f"Typing a Last Name: {text}")
        self.last_name_field.fill(text)

    def input_postal_code(self, text):
        logger.info(f"Typing a Postal Code: {text}")
        self.postal_code_field.fill(text)