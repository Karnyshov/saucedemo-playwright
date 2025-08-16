from playwright.sync_api import expect
from src.test_data import data_generation as td
from conftest import login_page
import constants

#TODO: Should I hide more steps as methods of Page Object?
class TestLogin:
    def test_invalid_credentials(self, login_page):
        login_page.input_username(td.random_username())
        login_page.input_password(td.random_password())
        login_page.click_login()
        expect(login_page.error_message_close_button).to_be_visible()
        expect(login_page.error_sign_username).to_be_visible()
        expect(login_page.error_sign_password).to_be_visible()
        expect(login_page.username_field).to_have_css("border-bottom-color","rgb(226, 35, 26)")
        expect(login_page.password_field).to_have_css("border-bottom-color","rgb(226, 35, 26)")
        expect(login_page.error_message).to_have_text(
            "Epic sadface: Username and password do not match any user in this service")

    def test_password_required(self,login_page):
        login_page.input_username(td.random_username())
        login_page.click_login()
        login_page.verify_input_error_state()
        # expect(login_page.error_message_close_button).to_be_visible()
        # expect(login_page.error_sign_username).to_be_visible()
        # expect(login_page.error_sign_password).to_be_visible()
        # expect(login_page.username_field).to_have_css("border-bottom-color","rgb(226, 35, 26)")
        # expect(login_page.password_field).to_have_css("border-bottom-color","rgb(226, 35, 26)")
        expect(login_page.error_message).to_have_text("Epic sadface: Password is required")


    def test_username_required(self,login_page):
        login_page.input_password(td.random_password())
        login_page.click_login()
        expect(login_page.error_message_close_button).to_be_visible()
        expect(login_page.error_sign_username).to_be_visible()
        expect(login_page.error_sign_password).to_be_visible()
        expect(login_page.username_field).to_have_css("border-bottom-color","rgb(226, 35, 26)")
        expect(login_page.password_field).to_have_css("border-bottom-color","rgb(226, 35, 26)")
        expect(login_page.error_message).to_have_text("Epic sadface: Username is required")


    def test_invalid_password(self,login_page):
        login_page.input_username(constants.STANDARD_USER)
        login_page.input_password(td.random_password())
        login_page.click_login()
        expect(login_page.error_message_close_button).to_be_visible()
        expect(login_page.error_sign_username).to_be_visible()
        expect(login_page.error_sign_password).to_be_visible()
        expect(login_page.username_field).to_have_css("border-bottom-color","rgb(226, 35, 26)")
        expect(login_page.password_field).to_have_css("border-bottom-color","rgb(226, 35, 26)")
        expect(login_page.error_message).to_have_text(
            "Epic sadface: Username and password do not match any user in this service")


    def test_invalid_username(self,login_page):
        login_page.input_username(td.random_username())
        login_page.input_password(constants.PASSWORD)
        login_page.click_login()
        expect(login_page.error_message_close_button).to_be_visible()
        expect(login_page.error_sign_username).to_be_visible()
        expect(login_page.error_sign_password).to_be_visible()
        expect(login_page.username_field).to_have_css("border-bottom-color","rgb(226, 35, 26)")
        expect(login_page.password_field).to_have_css("border-bottom-color","rgb(226, 35, 26)")
        expect(login_page.error_message).to_have_text(
            "Epic sadface: Username and password do not match any user in this service")

#TODO: need to refine approach?
    def test_standard_user(self, login_page):
        products_page = login_page.login_standard_user().page
        expect(products_page).to_have_url("https://www.saucedemo.com/inventory.html")


    def test_locked_user(self,login_page):
        login_page.login_locked_out_user()
        expect(login_page.error_message_close_button).to_be_visible()
        expect(login_page.error_sign_username).to_be_visible()
        expect(login_page.error_sign_password).to_be_visible()
        expect(login_page.username_field).to_have_css("border-bottom-color","rgb(226, 35, 26)")
        expect(login_page.password_field).to_have_css("border-bottom-color","rgb(226, 35, 26)")
        expect(login_page.error_message).to_have_text("Epic sadface: Sorry, this user has been locked out.")

    def test_problem_user(self,login_page):
        products_page = login_page.login_problem_user().page
        expect(products_page).to_have_url("https://www.saucedemo.com/inventory.html")

    def test_performance_glitch_user(self,login_page):
        products_page = login_page.login_performance_glitch_user().page
        expect(products_page).to_have_url("https://www.saucedemo.com/inventory.html")

    def test_error_user(self,login_page):
        products_page = login_page.login_error_user().page
        expect(products_page).to_have_url("https://www.saucedemo.com/inventory.html")

    def test_visual_user(self,login_page):
        products_page = login_page.login_visual_user().page
        expect(products_page).to_have_url("https://www.saucedemo.com/inventory.html")