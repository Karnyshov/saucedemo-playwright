from playwright.sync_api import Page, expect
from src.pages.products_page import ProductPage
import constants

class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.username_field = self.page.locator("//form/div[1]/input")
        # optimized_username_input = "//input[@id='user-name']"
        self.password_field = page.locator("//form/div[2]/input")
        # optimized_password_input = "//input[@id='password']"
        self.login_button = page.locator("//form/input")
        # optimized_login_button = "//input[@id='login-button']"
        self.error_message_container = page.locator("//form/div[3]")
        # optimized_error_message_container = "//div[@class='error-message-container error']"
        self.error_message_close_button = page.locator("//form/div[3]/h3/button")
        # optimized_error_message_close_button = "//button[@class='error-button']"
        self.error_message = page.locator("//form/div[3]/h3")
        self.error_sign_username = page.locator("//form/div[1]/*[2]")
        self.error_sign_password = page.locator("//form/div[2]/*[2]")

        self.usernames_header = page.locator("//div[@id=\"login_credentials\"]/h4")
        self.standard_user_title = page.locator("//div[@id=\"login_credentials\"]/text()[1]")
        self.locked_out_user_title = page.locator("//div[@id=\"login_credentials\"]/text()[2]")
        self.problem_user_title = page.locator("//div[@id=\"login_credentials\"]/text()[3]")
        self.performance_glitch_user_title = page.locator("//div[@id=\"login_credentials\"]/text()[4]")
        self.error_user_title = page.locator("//div[@id=\"login_credentials\"]/text()[5]")
        self.visual_user_title = page.locator("//div[@id=\"login_credentials\"]/text()[6]")

        self.password_header = page.locator("//div[@class=\"login_password\"]/h4")
        self.password = page.locator("//div[@class=\"login_password\"]/h4/text()")

    def open_page(self) -> None:
        self.page.goto("https://www.saucedemo.com/")

    def input_username(self, text) -> None:
        self.username_field.fill(text)

    def input_password(self, text) -> None:
        self.password_field.fill(text)

    def click_login(self) -> None:
        self.login_button.click()

    def login_standard_user(self) -> ProductPage:
        self.input_username(constants.STANDARD_USER)
        self.input_password(constants.PASSWORD)
        self.click_login()
        return ProductPage(self.page)

    def login_locked_out_user(self) -> None:
        self.input_username(constants.LOCKED_OUT_USER)
        self.input_password(constants.PASSWORD)
        self.click_login()

    def login_problem_user(self) -> ProductPage:
        self.input_username(constants.PROBLEM_USER)
        self.input_password(constants.PASSWORD)
        self.click_login()
        return ProductPage(self.page)

    def login_performance_glitch_user(self) -> ProductPage:
        self.input_username(constants.GLITCH_USER)
        self.input_password(constants.PASSWORD)
        self.click_login()
        return ProductPage(self.page)

    def login_error_user(self) -> ProductPage:
        self.input_username(constants.ERROR_USER)
        self.input_password(constants.PASSWORD)
        self.click_login()
        return ProductPage(self.page)

    def login_visual_user(self) -> ProductPage:
        self.input_username(constants.VISUAL_USER)
        self.input_password(constants.PASSWORD)
        self.click_login()
        return ProductPage(self.page)

    def verify_input_error_state(self) -> None:
        expect(self.error_message_close_button).to_be_visible()
        expect(self.error_sign_username).to_be_visible()
        expect(self.error_sign_password).to_be_visible()
        expect(self.username_field).to_have_css("border-bottom-color","rgb(226, 35, 26)")
        expect(self.password_field).to_have_css("border-bottom-color","rgb(226, 35, 26)")