from playwright.sync_api import Page, expect
from src.pages.base_page import BasePage
from utils.logger import logger
from src.constants.users import Users


class LoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.page = page

        self.logo = page.locator("//div[@class='login_logo']")
        self.username_field = page.locator("//form/div[1]/input")
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

        self.password_header = page.locator("//div[@class=\"login_password\"]/h4")
        self.password = page.locator("//div[@class=\"login_password\"]/h4/text()")

    def open_login_page(self) -> None:
        logger.info(f"Opening page")
        self.page.goto(self.base_url)

    # TODO: add check and additional CLEAR action
    def input_username(self, text) -> None:
        logger.info(f"Typing an username: {text}")
        self.username_field.fill(text)

    #TODO: add check and additional CLEAR action
    def input_password(self, text) -> None:
        logger.info(f"Typing a password")
        self.password_field.fill(text)

    def click_login(self) -> None:
        logger.info(f"Clicking on login button")
        self.login_button.click()

    def login(self, username, password) -> None:
        #Generic login action that can be parametrized
        logger.info(f"Logging as user with username: {username} and password")
        self.input_username(username)
        self.input_password(password)
        self.click_login()

    def login_standard_user(self) -> None:
        logger.info(f"Logging as standard user")
        self.input_username(Users.STANDARD_USER)
        self.input_password(Users.PASSWORD)
        self.click_login()

    def login_locked_out_user(self) -> None:
        logger.info(f"Truing to log in as locked out user")
        self.input_username(Users.LOCKED_OUT_USER)
        self.input_password(Users.PASSWORD)
        self.click_login()

    def login_problem_user(self) -> None:
        logger.info(f"Logging as user with problems")
        self.input_username(Users.PROBLEM_USER)
        self.input_password(Users.PASSWORD)
        self.click_login()

    def login_performance_glitch_user(self) -> None:
        logger.info(f"Logging as user with delay")
        self.input_username(Users.GLITCH_USER)
        self.input_password(Users.PASSWORD)
        self.click_login()

    def login_error_user(self) -> None:
        logger.info(f"Logging as user with errors")
        self.input_username(Users.ERROR_USER)
        self.input_password(Users.PASSWORD)
        self.click_login()

    def login_visual_user(self) -> None:
        logger.info(f"Logging as user with UI misalignment")
        self.input_username(Users.VISUAL_USER)
        self.input_password(Users.PASSWORD)
        self.click_login()

    def verify_input_error_state(self) -> None:
        logger.info(f"Checking error state: Error message present, error sign visible, input highlighted")
        expect(self.error_message_container).not_to_be_empty()
        expect(self.error_message_close_button).to_be_visible()
        expect(self.error_sign_username).to_be_visible()
        expect(self.error_sign_password).to_be_visible()
        expect(self.username_field).to_have_css("border-bottom-color","rgb(226, 35, 26)")
        expect(self.password_field).to_have_css("border-bottom-color","rgb(226, 35, 26)")

    def verify_basic_state(self) -> None:
        #Checks for input fields and login button omitted since they're already implemented: https://playwright.dev/python/docs/actionability
        logger.info(f"Checking basic state: input empty, no visible error elements")
        expect(self.page).to_have_url("https://www.saucedemo.com/")
        expect(self.page).to_have_title("Swag Labs")
        expect(self.error_message_container).to_be_empty()
        expect(self.error_message_close_button).to_be_hidden()
        expect(self.error_sign_username).to_be_hidden()
        expect(self.error_sign_password).to_be_hidden()
        expect(self.username_field).to_be_empty()
        expect(self.password_field).to_be_empty()
        expect(self.username_field).not_to_have_css("border-bottom-color","rgb(226, 35, 26)")
        expect(self.password_field).not_to_have_css("border-bottom-color","rgb(226, 35, 26)")
