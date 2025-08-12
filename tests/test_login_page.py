from playwright.sync_api import expect
from src.test_data import data_generation as td
from conftest import login_page

#TODO: Should I hide more steps as methods of Page Object?
class TestLogin:
    def test_invalid_credentials(self, login_page):
        login_page.input_username(td.random_username())
        login_page.input_password(td.random_password())
        login_page.click_login()
        expect(login_page.error_message_close_button).to_be_visible()
        expect(login_page.error_sign_username).to_be_visible()
        expect(login_page.error_sign_password).to_be_visible()
        expect(login_page.username_field).to_have_css("border-bottom-color", "rgb(226, 35, 26)")
        expect(login_page.password_field).to_have_css("border-bottom-color", "rgb(226, 35, 26)")
        expect(login_page.error_message).to_have_text("Epic sadface: Username and password do not match any user in this service")

    def test_password_required(self, login_page):
        login_page.input_username(td.random_username())
        login_page.click_login()
        expect(login_page.error_message_close_button).to_be_visible()
        expect(login_page.error_sign_username).to_be_visible()
        expect(login_page.error_sign_password).to_be_visible()
        expect(login_page.username_field).to_have_css("border-bottom-color", "rgb(226, 35, 26)")
        expect(login_page.password_field).to_have_css("border-bottom-color", "rgb(226, 35, 26)")
        expect(login_page.error_message).to_have_text("Epic sadface: Password is required")

    def test_username_required(self, login_page):
        login_page.input_password(td.random_password())
        login_page.click_login()
        expect(login_page.error_message_close_button).to_be_visible()
        expect(login_page.error_sign_username).to_be_visible()
        expect(login_page.error_sign_password).to_be_visible()
        expect(login_page.username_field).to_have_css("border-bottom-color", "rgb(226, 35, 26)")
        expect(login_page.password_field).to_have_css("border-bottom-color", "rgb(226, 35, 26)")
        expect(login_page.error_message).to_have_text("Epic sadface: Username is required")