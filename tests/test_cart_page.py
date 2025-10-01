from playwright.sync_api import expect
from tests.conftest import page_manager as pm
from tests.conftest import open_empty_cart as empty_cart
from tests.conftest import open_cart_with_item as cart

class TestCart:
    #TODO: add more checks
    def test_basic_state_empty_cart(self, pm, empty_cart):
        pm.product_item_page.verify_burger_menu_closed()
        pm.product_item_page.verify_copyright()
        pm.product_item_page.verify_footer_twitter()
        pm.product_item_page.verify_footer_facebook()
        pm.product_item_page.verify_footer_linkedin()
        pass

    # TODO: add more checks
    def test_basic_state_cart(self, pm, cart):
        pm.product_item_page.verify_burger_menu_closed()
        pm.product_item_page.verify_copyright()
        pm.product_item_page.verify_footer_twitter()
        pm.product_item_page.verify_footer_facebook()
        pm.product_item_page.verify_footer_linkedin()
        pass

    def test_footer_twitter(self, pm, cart):
        pm.product_item_page.verify_footer_twitter()
        pm.twitter = pm.product_item_page.click_footer_button(pm.product_item_page.footer_twitter)
        expect(pm.twitter_page.page).to_have_url("https://x.com/saucelabs")
        expect(pm.twitter_page.page).to_have_title("Sauce Labs (@saucelabs) / X")

    def test_footer_facebook(self, pm, cart):
        pm.product_item_page.verify_footer_facebook()
        pm.facebook = pm.product_item_page.click_footer_button(pm.product_item_page.footer_facebook)
        expect(pm.facebook_page.page).to_have_url("https://www.facebook.com/saucelabs")
        expect(pm.facebook_page.page).to_have_title("Sauce Labs | Facebook")

    def test_footer_linkedin(self, pm, cart):
        pm.product_item_page.verify_footer_linkedin()
        pm.linkedin = pm.product_item_page.click_footer_button(pm.product_item_page.footer_linkedin)
        expect(pm.linkedin_page.page).to_have_url("https://www.linkedin.com/company/sauce-labs/")
        expect(pm.linkedin_page.page).to_have_title("Sauce Labs | LinkedIn")

    def test_burger_menu(self, pm, cart):
        pm.product_item_page.verify_burger_menu_closed()
        pm.product_item_page.open_burger_menu()
        pm.product_item_page.verify_burger_menu_opened()
        pm.product_item_page.close_burger_menu()
        pm.product_item_page.verify_burger_menu_closed()

    #TODO: add check if menu already opened?
    def test_burger_menu_all_items(self, pm, cart):
        pm.product_item_page.open_burger_menu()
        expect(pm.product_item_page.burger_menu_all_items).to_have_attribute("href","#")
        pm.product_item_page.burger_menu_all_items.click()

    def test_burger_menu_about(self, pm, cart):
        pm.product_item_page.open_burger_menu()
        expect(pm.product_item_page.burger_menu_about).to_have_attribute("href","https://saucelabs.com/")
        pm.product_item_page.open_about_page()
        expect(pm.about_page.page).to_have_url("https://saucelabs.com/")
        expect(pm.about_page.page).to_have_title("Sauce Labs: Cross Browser Testing, Selenium Testing & Mobile Testing")

    def test_burger_menu_logout(self, pm, cart):
        pm.product_item_page.open_burger_menu()
        expect(pm.product_item_page.burger_menu_logout).to_have_attribute("href","#")
        pm.product_item_page.logout()
        expect(pm.login_page.page).to_have_url("https://www.saucedemo.com/")
        expect(pm.login_page.page).to_have_title("Swag Labs")

    def test_back_to_products(self, pm, cart):
        pass

    def test_start_checkout(self, pm, cart):
        pass

    def test_remove_from_cart(self, pm, cart):
        pass

    def test_content_consistency(self, pm, cart):
        pass