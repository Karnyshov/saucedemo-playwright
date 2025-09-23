from playwright.sync_api import expect
from tests.conftest import page_manager as pm
from tests.conftest import open_random_item as item

class TestProductItem:
    #TODO: add more checks
    def test_basic_state(self, pm, item):
        pm.product_item_page.verify_burger_menu_closed()
        pm.product_item_page.verify_copyright()
        pm.product_item_page.verify_footer_twitter()
        pm.product_item_page.verify_footer_facebook()
        pm.product_item_page.verify_footer_linkedin()
        pm.product_item_page.verify_empty_cart()

    def test_footer_twitter(self, pm, item):
        pm.product_item_page.verify_footer_twitter()
        pm.twitter = pm.product_item_page.click_footer_button(pm.product_item_page.footer_twitter)
        expect(pm.twitter_page.page).to_have_url("https://x.com/saucelabs")
        expect(pm.twitter_page.page).to_have_title("Sauce Labs (@saucelabs) / X")

    def test_footer_facebook(self, pm, item):
        pm.product_item_page.verify_footer_facebook()
        pm.facebook = pm.product_item_page.click_footer_button(pm.product_item_page.footer_facebook)
        expect(pm.facebook_page.page).to_have_url("https://www.facebook.com/saucelabs")
        expect(pm.facebook_page.page).to_have_title("Sauce Labs | Facebook")

    def test_footer_linkedin(self, pm, item):
        pm.product_item_page.verify_footer_linkedin()
        pm.linkedin = pm.product_item_page.click_footer_button(pm.product_item_page.footer_linkedin)
        expect(pm.linkedin_page.page).to_have_url("https://www.linkedin.com/company/sauce-labs/")
        expect(pm.linkedin_page.page).to_have_title("Sauce Labs | LinkedIn")

    def test_burger_menu(self, pm, item):
        pm.product_item_page.verify_burger_menu_closed()
        pm.product_item_page.open_burger_menu()
        pm.product_item_page.verify_burger_menu_opened()
        pm.product_item_page.close_burger_menu()
        pm.product_item_page.verify_burger_menu_closed()

    #TODO: add check if menu already opened?
    def test_burger_menu_all_items(self, pm, item):
        pm.product_item_page.open_burger_menu()
        expect(pm.product_item_page.burger_menu_all_items).to_have_attribute("href","#")
        pm.product_item_page.burger_menu_all_items.click()

    def test_burger_menu_about(self, pm, item):
        pm.product_item_page.open_burger_menu()
        expect(pm.product_item_page.burger_menu_about).to_have_attribute("href","https://saucelabs.com/")
        pm.product_item_page.open_about_page()
        expect(pm.about_page.page).to_have_url("https://saucelabs.com/")
        expect(pm.about_page.page).to_have_title("Sauce Labs: Cross Browser Testing, Selenium Testing & Mobile Testing")

    def test_burger_menu_logout(self, pm, item):
        pm.product_item_page.open_burger_menu()
        expect(pm.product_item_page.burger_menu_logout).to_have_attribute("href","#")
        pm.product_item_page.logout()
        expect(pm.login_page.page).to_have_url("https://www.saucedemo.com/")
        expect(pm.login_page.page).to_have_title("Swag Labs")

    def test_add_to_cart(self, pm, item):
        expect(pm.products_page.shopping_cart_count).not_to_be_visible()
        pm.product_item_page.add_to_cart()
        pm.product_item_page.verify_item_added_to_cart()
        expect(pm.product_item_page.shopping_cart_count).to_have_text("1")

    def test_remove_from_cart(self, pm, item):
        expect(pm.products_page.shopping_cart_count).not_to_be_visible()
        pm.product_item_page.add_to_cart()
        pm.product_item_page.verify_item_added_to_cart()
        expect(pm.product_item_page.shopping_cart_count).to_have_text("1")
        pm.product_item_page.remove_from_cart()
        pm.product_item_page.verify_item_removed_from_cart()
        expect(pm.products_page.shopping_cart_count).not_to_be_visible()

    def test_back_to_products(self, pm, item):
        pass

    def test_content_consistency(self, pm, item):
        pass