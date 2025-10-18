from playwright.sync_api import expect
from tests.conftest import page_manager as pm
from tests.conftest import open_checkout_complete_page as checkout_complete

class TestCheckoutComplete:
    def test_basic_state(self, pm, checkout_complete):
        pass

    def test_footer_twitter(self, pm, checkout_complete):
        pm.checkout_complete_page.verify_footer_twitter()
        pm.twitter = pm.checkout_complete_page.click_footer_button(pm.checkout_complete_page.footer_twitter)
        expect(pm.twitter.page).to_have_url("https://x.com/saucelabs")
        expect(pm.twitter.page).to_have_title("Sauce Labs (@saucelabs) / X")

    def test_footer_facebook(self, pm, checkout_complete):
        pm.checkout_complete_page.verify_footer_facebook()
        pm.facebook = pm.checkout_complete_page.click_footer_button(pm.checkout_complete_page.footer_facebook)
        expect(pm.facebook_page.page).to_have_url("https://www.facebook.com/saucelabs")
        expect(pm.facebook_page.page).to_have_title("Sauce Labs | Facebook")

    def test_footer_linkedin(self, pm, checkout_complete):
        pm.checkout_complete_page.verify_footer_linkedin()
        pm.linkedin = pm.checkout_complete_page.click_footer_button(pm.checkout_complete_page.footer_linkedin)
        expect(pm.linkedin_page.page).to_have_url("https://www.linkedin.com/company/sauce-labs/")
        expect(pm.linkedin_page.page).to_have_title("Sauce Labs | LinkedIn")

    def test_burger_menu(self, pm, checkout_complete):
        pm.checkout_complete_page.verify_burger_menu_closed()
        pm.checkout_complete_page.open_burger_menu()
        pm.checkout_complete_page.verify_burger_menu_opened()
        pm.checkout_complete_page.close_burger_menu()
        pm.checkout_complete_page.verify_burger_menu_closed()

    #TODO: add check if menu already opened?
    def test_burger_menu_all_items(self, pm, checkout_complete):
        pm.checkout_complete_page.open_burger_menu()
        expect(pm.checkout_complete_page.burger_menu_all_items).to_have_attribute("href","#")
        pm.checkout_complete_page.burger_menu_all_items.click()

    def test_burger_menu_about(self, pm, checkout_complete):
        pm.checkout_complete_page.open_burger_menu()
        expect(pm.checkout_complete_page.burger_menu_about).to_have_attribute("href","https://saucelabs.com/")
        pm.checkout_complete_page.open_about_page()
        expect(pm.about_page.page).to_have_url("https://saucelabs.com/")
        expect(pm.about_page.page).to_have_title("Sauce Labs: Cross Browser Testing, Selenium Testing & Mobile Testing")

    def test_burger_menu_logout(self, pm, checkout_complete):
        pm.checkout_complete_page.open_burger_menu()
        expect(pm.checkout_complete_page.burger_menu_logout).to_have_attribute("href","#")
        pm.checkout_complete_page.logout()
        expect(pm.login_page.page).to_have_url("https://www.saucedemo.com/")
        expect(pm.login_page.page).to_have_title("Swag Labs")

    def test_back_to_home(self, pm, checkout_complete):
        pass

    def test_open_cart_page(self, pm, checkout_complete):
        pass

    def test_complete_header(self, pm, checkout_complete):
        pass

    def test_complete_text(self, pm, checkout_complete):
        pass