from playwright.sync_api import expect
from tests.conftest import page_manager as pm
from tests.conftest import open_checkout_info_page as checkout
from utils.faker import fake

class TestCheckoutInfo:
    def test_basic_state(self, pm, checkout):
        pm.cart_page.verify_burger_menu_closed()
        pm.cart_page.verify_copyright()
        pm.cart_page.verify_footer_twitter()
        pm.cart_page.verify_footer_facebook()
        pm.cart_page.verify_footer_linkedin()
        pm.checkout_info_page.verify_last_name_field()
        pm.checkout_info_page.verify_last_name_field()
        pm.checkout_info_page.verify_postal_code_field()
        pm.checkout_info_page.verify_cancel_button()
        pm.checkout_info_page.verify_continue_button()
        pm.checkout_info_page.verify_basic_input_state()
        expect(pm.checkout_info_page.page_title).to_have_text("Checkout: Your Information")
        expect(pm.checkout_info_page.shopping_cart_count).to_have_text("1")
        expect(pm.checkout_info_page.shopping_cart).to_be_visible()

    def test_footer_twitter(self, pm, checkout):
        pm.checkout_info_page.verify_footer_twitter()
        pm.twitter = pm.checkout_info_page.click_footer_button(pm.checkout_info_page.footer_twitter)
        expect(pm.twitter.page).to_have_url("https://x.com/saucelabs")
        expect(pm.twitter.page).to_have_title("Sauce Labs (@saucelabs) / X")

    def test_footer_facebook(self, pm, checkout):
        pm.checkout_info_page.verify_footer_facebook()
        pm.facebook = pm.checkout_info_page.click_footer_button(pm.checkout_info_page.footer_facebook)
        expect(pm.facebook_page.page).to_have_url("https://www.facebook.com/saucelabs")
        expect(pm.facebook_page.page).to_have_title("Sauce Labs | Facebook")

    def test_footer_linkedin(self, pm, checkout):
        pm.checkout_info_page.verify_footer_linkedin()
        pm.linkedin = pm.checkout_info_page.click_footer_button(pm.checkout_info_page.footer_linkedin)
        expect(pm.linkedin_page.page).to_have_url("https://www.linkedin.com/company/sauce-labs/")
        expect(pm.linkedin_page.page).to_have_title("Sauce Labs | LinkedIn")

    def test_burger_menu(self, pm, checkout):
        pm.checkout_info_page.verify_burger_menu_closed()
        pm.checkout_info_page.open_burger_menu()
        pm.checkout_info_page.verify_burger_menu_opened()
        pm.checkout_info_page.close_burger_menu()
        pm.checkout_info_page.verify_burger_menu_closed()

    #TODO: add check if menu already opened?
    def test_burger_menu_all_items(self, pm, checkout):
        pm.checkout_info_page.open_burger_menu()
        expect(pm.checkout_info_page.burger_menu_all_items).to_have_attribute("href","#")
        pm.checkout_info_page.burger_menu_all_items.click()

    def test_burger_menu_about(self, pm, checkout):
        pm.checkout_info_page.open_burger_menu()
        expect(pm.checkout_info_page.burger_menu_about).to_have_attribute("href","https://saucelabs.com/")
        pm.checkout_info_page.open_about_page()
        expect(pm.about_page.page).to_have_url("https://saucelabs.com/")
        expect(pm.about_page.page).to_have_title("Sauce Labs: Cross Browser Testing, Selenium Testing & Mobile Testing")

    def test_burger_menu_logout(self, pm, checkout):
        pm.checkout_info_page.open_burger_menu()
        expect(pm.checkout_info_page.burger_menu_logout).to_have_attribute("href","#")
        pm.checkout_info_page.logout()
        expect(pm.login_page.page).to_have_url("https://www.saucedemo.com/")
        expect(pm.login_page.page).to_have_title("Swag Labs")

    def test_cancel_checkout(self, pm, checkout):
        pm.checkout_info_page.cancel_checkout()
        expect(pm.cart_page.page).to_have_url("https://www.saucedemo.com/cart.html")

    #TODO: move clicking to Base Page
    def test_open_cart(self, pm, checkout):
        pm.checkout_info_page.shopping_cart.click()
        expect(pm.cart_page.page).to_have_url("https://www.saucedemo.com/cart.html")

    def test_open_checkout_overview(self, pm, checkout):
        pm.checkout_info_page.continue_checkout()
        pass

    def test_shipping_info_required(self, pm, checkout):
        pm.checkout_info_page.continue_checkout()
        pm.checkout_info_page.verify_input_error_state()
        expect(pm.checkout_info_page.error_message).to_have_text("Error: First Name is required")

    def test_first_name_required(self, pm, checkout):
        pm.checkout_info_page.input_last_name(fake.last_name())
        pm.checkout_info_page.input_postal_code(fake.postalcode())
        pm.checkout_info_page.continue_checkout()
        pm.checkout_info_page.verify_input_error_state()
        expect(pm.checkout_info_page.error_message).to_have_text("Error: First Name is required")

    def test_last_name_required(self, pm, checkout):
        pm.checkout_info_page.input_first_name(fake.first_name())
        pm.checkout_info_page.input_postal_code(fake.postalcode())
        pm.checkout_info_page.continue_checkout()
        pm.checkout_info_page.verify_input_error_state()
        expect(pm.checkout_info_page.error_message).to_have_text("Error: Last Name is required")

    def test_postal_code_required(self, pm, checkout):
        pm.checkout_info_page.input_first_name(fake.first_name())
        pm.checkout_info_page.input_last_name(fake.last_name())
        pm.checkout_info_page.continue_checkout()
        pm.checkout_info_page.verify_input_error_state()
        expect(pm.checkout_info_page.error_message).to_have_text("Error: Postal Code is required")

    def test_last_name_postal_code_required(self, pm, checkout):
        pm.checkout_info_page.input_first_name(fake.first_name())
        pm.checkout_info_page.continue_checkout()
        pm.checkout_info_page.verify_input_error_state()
        expect(pm.checkout_info_page.error_message).to_have_text("Error: Last Name is required")
    
    def test_first_name_postal_code_required(self, pm, checkout):
        pm.checkout_info_page.input_last_name(fake.last_name())
        pm.checkout_info_page.continue_checkout()
        pm.checkout_info_page.verify_input_error_state()
        expect(pm.checkout_info_page.error_message).to_have_text("Error: First Name is required")