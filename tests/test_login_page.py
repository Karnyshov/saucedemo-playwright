from playwright.sync_api import expect
from utils.faker import fake
from src.constants.users import Users
from tests.conftest import page_manager as pm


class TestLogin:
    def test_basic_state(self, pm):
        pm.login_page.open_login_page()
        pm.login_page.verify_basic_state()

    def test_invalid_credentials(self, pm):
        pm.login_page.open_login_page()
        pm.login_page.input_username(fake.user_name())
        pm.login_page.input_password(fake.password())
        pm.login_page.click_login()
        pm.login_page.verify_input_error_state()
        expect(pm.login_page.error_message).to_have_text(
            "Epic sadface: Username and password do not match any user in this service")

    def test_password_required(self, pm):
        pm.login_page.open_login_page()
        pm.login_page.input_username(fake.user_name())
        pm.login_page.click_login()
        pm.login_page.verify_input_error_state()
        expect(pm.login_page.error_message).to_have_text("Epic sadface: Password is required")

    def test_username_required(self, pm):
        pm.login_page.open_login_page()
        pm.login_page.input_password(fake.password())
        pm.login_page.click_login()
        pm.login_page.verify_input_error_state()
        expect(pm.login_page.error_message).to_have_text("Epic sadface: Username is required")

    def test_invalid_password(self, pm):
        pm.login_page.open_login_page()
        pm.login_page.input_username(Users.STANDARD_USER)
        pm.login_page.input_password(fake.password())
        pm.login_page.click_login()
        pm.login_page.verify_input_error_state()
        expect(pm.login_page.error_message).to_have_text(
            "Epic sadface: Username and password do not match any user in this service")

    def test_invalid_username(self, pm):
        pm.login_page.open_login_page()
        pm.login_page.input_username(fake.user_name())
        pm.login_page.input_password(Users.PASSWORD)
        pm.login_page.click_login()
        pm.login_page.verify_input_error_state()
        expect(pm.login_page.error_message).to_have_text(
            "Epic sadface: Username and password do not match any user in this service")

#TODO: need to refine approach?
    def test_standard_user(self, pm):
        pm.login_page.open_login_page()
        pm.login_page.login_standard_user()
        expect(pm.products_page.page).to_have_url("https://www.saucedemo.com/inventory.html")

    def test_locked_user(self, pm):
        pm.login_page.open_login_page()
        pm.login_page.login_locked_out_user()
        pm.login_page.verify_input_error_state()
        expect(pm.login_page.error_message).to_have_text("Epic sadface: Sorry, this user has been locked out.")

    def test_problem_user(self, pm):
        pm.login_page.open_login_page()
        pm.login_page.login_problem_user()
        expect(pm.products_page.page).to_have_url("https://www.saucedemo.com/inventory.html")

    def test_performance_glitch_user(self, pm):
        pm.login_page.open_login_page()
        pm.login_page.login_performance_glitch_user()
        expect(pm.products_page.page).to_have_url("https://www.saucedemo.com/inventory.html")

    def test_error_user(self, pm):
        pm.login_page.open_login_page()
        pm.login_page.login_error_user()
        expect(pm.products_page.page).to_have_url("https://www.saucedemo.com/inventory.html")

    def test_visual_user(self, pm):
        pm.login_page.open_login_page()
        pm.login_page.login_visual_user()
        expect(pm.products_page.page).to_have_url("https://www.saucedemo.com/inventory.html")
