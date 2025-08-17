from playwright.sync_api import expect
from utils.faker import fake
from tests.conftest import open_login_page
from src.core.Users import Users


class TestLogin:
    def test_basic_state(self, open_login_page):
        open_login_page.verify_basic_state()

    def test_invalid_credentials(self, open_login_page):
        open_login_page.input_username(fake.user_name())
        open_login_page.input_password(fake.password())
        open_login_page.click_login()
        open_login_page.verify_input_error_state()
        expect(open_login_page.error_message).to_have_text(
            "Epic sadface: Username and password do not match any user in this service")

    def test_password_required(self,open_login_page):
        open_login_page.input_username(fake.user_name())
        open_login_page.click_login()
        open_login_page.verify_input_error_state()
        expect(open_login_page.error_message).to_have_text("Epic sadface: Password is required")

    def test_username_required(self,open_login_page):
        open_login_page.input_password(fake.password())
        open_login_page.click_login()
        open_login_page.verify_input_error_state()
        expect(open_login_page.error_message).to_have_text("Epic sadface: Username is required")

    def test_invalid_password(self,open_login_page):
        open_login_page.input_username(Users.STANDARD_USER)
        open_login_page.input_password(fake.password())
        open_login_page.click_login()
        open_login_page.verify_input_error_state()
        expect(open_login_page.error_message).to_have_text(
            "Epic sadface: Username and password do not match any user in this service")

    def test_invalid_username(self,open_login_page):
        open_login_page.input_username(fake.user_name())
        open_login_page.input_password(Users.PASSWORD)
        open_login_page.click_login()
        open_login_page.verify_input_error_state()
        expect(open_login_page.error_message).to_have_text(
            "Epic sadface: Username and password do not match any user in this service")

#TODO: need to refine approach?
    def test_standard_user(self, open_login_page):
        products_page = open_login_page.login_standard_user().page
        expect(products_page).to_have_url("https://www.saucedemo.com/inventory.html")

    def test_locked_user(self,open_login_page):
        open_login_page.login_locked_out_user()
        open_login_page.verify_input_error_state()
        expect(open_login_page.error_message).to_have_text("Epic sadface: Sorry, this user has been locked out.")

    def test_problem_user(self,open_login_page):
        products_page = open_login_page.login_problem_user().page
        expect(products_page).to_have_url("https://www.saucedemo.com/inventory.html")

    def test_performance_glitch_user(self,open_login_page):
        products_page = open_login_page.login_performance_glitch_user().page
        expect(products_page).to_have_url("https://www.saucedemo.com/inventory.html")

    def test_error_user(self,open_login_page):
        products_page = open_login_page.login_error_user().page
        expect(products_page).to_have_url("https://www.saucedemo.com/inventory.html")

    def test_visual_user(self,open_login_page):
        products_page = open_login_page.login_visual_user().page
        expect(products_page).to_have_url("https://www.saucedemo.com/inventory.html")
