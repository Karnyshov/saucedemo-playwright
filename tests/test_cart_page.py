from playwright.sync_api import expect
from tests.conftest import page_manager as pm
from tests.conftest import open_empty_cart as empty_cart
from tests.conftest import open_cart_with_item as cart
from tests.conftest import open_cart_with_multiple_items as cart_items

class TestCart:
    def test_basic_state_empty_cart(self, pm, empty_cart):
        pm.cart_page.verify_burger_menu_closed()
        pm.cart_page.verify_copyright()
        pm.cart_page.verify_footer_twitter()
        pm.cart_page.verify_footer_facebook()
        pm.cart_page.verify_footer_linkedin()
        pm.cart_page.verify_empty_cart()

    def test_basic_state_cart(self, pm, cart):
        pm.cart_page.verify_burger_menu_closed()
        pm.cart_page.verify_copyright()
        pm.cart_page.verify_footer_twitter()
        pm.cart_page.verify_footer_facebook()
        pm.cart_page.verify_footer_linkedin()
        expect(pm.cart_page.item_container).to_be_visible()
        expect(pm.cart_page.remove_button).to_be_visible()
        expect(pm.cart_page.remove_button).to_have_text("Remove")

    def test_footer_twitter(self, pm, cart):
        pm.cart_page.verify_footer_twitter()
        pm.twitter = pm.cart_page.click_footer_button(pm.cart_page.footer_twitter)
        expect(pm.twitter.page).to_have_url("https://x.com/saucelabs")
        expect(pm.twitter.page).to_have_title("Sauce Labs (@saucelabs) / X")

    def test_footer_facebook(self, pm, cart):
        pm.cart_page.verify_footer_facebook()
        pm.facebook = pm.cart_page.click_footer_button(pm.cart_page.footer_facebook)
        expect(pm.facebook_page.page).to_have_url("https://www.facebook.com/saucelabs")
        expect(pm.facebook_page.page).to_have_title("Sauce Labs | Facebook")

    def test_footer_linkedin(self, pm, cart):
        pm.cart_page.verify_footer_linkedin()
        pm.linkedin = pm.cart_page.click_footer_button(pm.cart_page.footer_linkedin)
        expect(pm.linkedin_page.page).to_have_url("https://www.linkedin.com/company/sauce-labs/")
        expect(pm.linkedin_page.page).to_have_title("Sauce Labs | LinkedIn")

    def test_burger_menu(self, pm, cart):
        pm.cart_page.verify_burger_menu_closed()
        pm.cart_page.open_burger_menu()
        pm.cart_page.verify_burger_menu_opened()
        pm.cart_page.close_burger_menu()
        pm.cart_page.verify_burger_menu_closed()

    #TODO: add check if menu already opened?
    def test_burger_menu_all_items(self, pm, cart):
        pm.cart_page.open_burger_menu()
        expect(pm.cart_page.burger_menu_all_items).to_have_attribute("href","#")
        pm.cart_page.burger_menu_all_items.click()

    def test_burger_menu_about(self, pm, cart):
        pm.cart_page.open_burger_menu()
        expect(pm.cart_page.burger_menu_about).to_have_attribute("href","https://saucelabs.com/")
        pm.cart_page.open_about_page()
        expect(pm.about_page.page).to_have_url("https://saucelabs.com/")
        expect(pm.about_page.page).to_have_title("Sauce Labs: Cross Browser Testing, Selenium Testing & Mobile Testing")

    def test_burger_menu_logout(self, pm, cart):
        pm.cart_page.open_burger_menu()
        expect(pm.cart_page.burger_menu_logout).to_have_attribute("href","#")
        pm.cart_page.logout()
        expect(pm.login_page.page).to_have_url("https://www.saucedemo.com/")
        expect(pm.login_page.page).to_have_title("Swag Labs")

    def test_back_to_products(self, pm, cart):
        pm.cart_page.open_products_page()
        expect(pm.products_page.page).to_have_url("https://www.saucedemo.com/inventory.html")

    def test_start_checkout(self, pm, cart):
        pm.cart_page.open_checkout_page()
        expect(pm.checkout_info_page.page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

    def test_remove_single_item_from_cart(self, pm, cart):
        item = pm.cart_page.get_item(0)
        item.verify_cart_item()
        item.remove_item()
        pm.cart_page.verify_empty_cart()

    def test_remove_item_from_cart(self, pm, cart_items):
        item2 = pm.cart_page.get_item(1)
        item2.remove_item()
        item2.verify_removed_item()
        expect(pm.cart_page.shopping_cart_count).to_have_text("1")

    def test_content_consistency(self, pm, cart):
        item = pm.cart_page.get_item(0)
        item.verify_content(cart)

    def test_content_consistency_two_items(self, pm, cart_items):
        item1 = pm.cart_page.get_item(0)
        item1.verify_content(cart_items[0])
        item2 = pm.cart_page.get_item(1)
        item2.verify_content(cart_items[1])