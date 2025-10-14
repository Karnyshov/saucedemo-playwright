from playwright.sync_api import expect
from tests.conftest import page_manager as pm
from tests.conftest import open_checkout_overview_page_with_item as overview_item
from tests.conftest import open_checkout_overview_page_with_two_items as overview_items

class TestCheckoutOverview:
    def test_basic_state_single_item(self, pm, overview_item):
        pm.checkout_overview_page.verify_burger_menu_closed()
        pm.checkout_overview_page.verify_copyright()
        pm.checkout_overview_page.verify_footer_twitter()
        pm.checkout_overview_page.verify_footer_facebook()
        pm.checkout_overview_page.verify_footer_linkedin()
        pm.checkout_overview_page.verify_basic_state_single_item()

    def test_basic_state_two_items(self, pm, overview_items):
        pm.checkout_overview_page.verify_burger_menu_closed()
        pm.checkout_overview_page.verify_copyright()
        pm.checkout_overview_page.verify_footer_twitter()
        pm.checkout_overview_page.verify_footer_facebook()
        pm.checkout_overview_page.verify_footer_linkedin()
        pm.checkout_overview_page.verify_basic_state_two_items()

    def test_footer_twitter(self, pm, overview_item):
        pm.checkout_overview_page.verify_footer_twitter()
        pm.twitter = pm.checkout_overview_page.click_footer_button(pm.checkout_overview_page.footer_twitter)
        expect(pm.twitter.page).to_have_url("https://x.com/saucelabs")
        expect(pm.twitter.page).to_have_title("Sauce Labs (@saucelabs) / X")

    def test_footer_facebook(self, pm, overview_item):
        pm.checkout_overview_page.verify_footer_facebook()
        pm.facebook = pm.checkout_overview_page.click_footer_button(pm.checkout_overview_page.footer_facebook)
        expect(pm.facebook_page.page).to_have_url("https://www.facebook.com/saucelabs")
        expect(pm.facebook_page.page).to_have_title("Sauce Labs | Facebook")

    def test_footer_linkedin(self, pm, overview_item):
        pm.checkout_overview_page.verify_footer_linkedin()
        pm.linkedin = pm.checkout_overview_page.click_footer_button(pm.checkout_overview_page.footer_linkedin)
        expect(pm.linkedin_page.page).to_have_url("https://www.linkedin.com/company/sauce-labs/")
        expect(pm.linkedin_page.page).to_have_title("Sauce Labs | LinkedIn")

    def test_burger_menu(self, pm, overview_item):
        pm.checkout_overview_page.verify_burger_menu_closed()
        pm.checkout_overview_page.open_burger_menu()
        pm.checkout_overview_page.verify_burger_menu_opened()
        pm.checkout_overview_page.close_burger_menu()
        pm.checkout_overview_page.verify_burger_menu_closed()

    #TODO: add check if menu already opened?
    def test_burger_menu_all_items(self, pm, overview_item):
        pm.checkout_overview_page.open_burger_menu()
        expect(pm.checkout_overview_page.burger_menu_all_items).to_have_attribute("href","#")
        pm.checkout_overview_page.burger_menu_all_items.click()

    def test_burger_menu_about(self, pm, overview_item):
        pm.checkout_overview_page.open_burger_menu()
        expect(pm.checkout_overview_page.burger_menu_about).to_have_attribute("href","https://saucelabs.com/")
        pm.checkout_overview_page.open_about_page()
        expect(pm.about_page.page).to_have_url("https://saucelabs.com/")
        expect(pm.about_page.page).to_have_title("Sauce Labs: Cross Browser Testing, Selenium Testing & Mobile Testing")

    def test_burger_menu_logout(self, pm, overview_item):
        pm.checkout_overview_page.open_burger_menu()
        expect(pm.checkout_overview_page.burger_menu_logout).to_have_attribute("href","#")
        pm.checkout_overview_page.logout()
        expect(pm.login_page.page).to_have_url("https://www.saucedemo.com/")
        expect(pm.login_page.page).to_have_title("Swag Labs")

    def test_cancel_checkout(self, pm, overview_item):
        pm.checkout_overview_page.cancel_checkout()
        expect(pm.products_page.page).to_have_url("https://www.saucedemo.com/inventory.html")
        expect(pm.products_page.shopping_cart_count).to_have_text("1")

    def test_finish_checkout(self, pm, overview_item):
        pm.checkout_overview_page.finish_checkout()

        pass

    def test_payment_info(self, pm, overview_item):
        expect(pm.checkout_overview_page.payment_info_label).to_have_text("Payment Information:")
        expect(pm.checkout_overview_page.payment_info).to_contain_text("SauceCard #")

    def test_shipping_info(self, pm, overview_item):
        expect(pm.checkout_overview_page.shipping_info_label).to_have_text("Shipping Information:")
        expect(pm.checkout_overview_page.shipping_info).to_have_text("Free Pony Express Delivery!")

    def test_price_info(self, pm, overview_item):
        expect(pm.checkout_overview_page.price_total_label).to_have_text("Price Total")
        expect(pm.checkout_overview_page.price_item_total_value).to_contain_text("Item total: $")
        expect(pm.checkout_overview_page.price_tax_value).to_contain_text("Tax: $")
        expect(pm.checkout_overview_page.price_total_value).to_contain_text("Total: $")

    def test_price_values_one_item(self, pm, overview_item):
        item = pm.checkout_overview_page.get_item(0)
        pm.checkout_overview_page.verify_prices(item)

    def test_price_values_two_items(self, pm, overview_items):
        pass

    def test_consistency(self, pm, overview_item):
        pass

    def test_consistency_two_items(self, pm, overview_items):
        pass