from playwright.sync_api import expect
from tests.conftest import page_manager as pm

class TestProducts:
    #TODO: add more checks
    def test_basic_state(self, pm):
        pm.login_page.open_login_page()
        pm.login_page.login_standard_user()
        pm.products_page.verify_burger_menu_closed()
        pm.products_page.verify_copyright()
        pm.products_page.verify_footer_twitter()
        pm.products_page.verify_footer_facebook()
        pm.products_page.verify_footer_linkedin()
        expect(pm.products_page.shopping_cart).to_be_visible()
        expect(pm.products_page.shopping_cart_count).not_to_be_visible()
        expect(pm.products_page.products_page_title).to_have_text("Products")
        expect(pm.products_page.product_item_element).not_to_have_count(0)


    def test_footer_twitter(self, pm):
        pm.login_page.open_login_page()
        pm.login_page.login_standard_user()
        pm.products_page.verify_footer_twitter()
        pm.twitter = pm.products_page.click_footer_button(pm.products_page.footer_twitter)
        expect(pm.twitter_page.page).to_have_url("https://x.com/saucelabs")
        expect(pm.twitter_page.page).to_have_title("Sauce Labs (@saucelabs) / X")

    def test_footer_facebook(self, pm):
        pm.login_page.open_login_page()
        pm.login_page.login_standard_user()
        pm.products_page.verify_footer_facebook()
        pm.facebook = pm.products_page.click_footer_button(pm.products_page.footer_facebook)
        expect(pm.facebook_page.page).to_have_url("https://www.facebook.com/saucelabs")
        expect(pm.facebook_page.page).to_have_title("Sauce Labs | Facebook")

    def test_footer_linkedin(self, pm):
        pm.login_page.open_login_page()
        pm.login_page.login_standard_user()
        pm.products_page.verify_footer_linkedin()
        pm.linkedin = pm.products_page.click_footer_button(pm.products_page.footer_linkedin)
        expect(pm.linkedin_page.page).to_have_url("https://www.linkedin.com/company/sauce-labs/")
        expect(pm.linkedin_page.page).to_have_title("Sauce Labs | LinkedIn")

    def test_burger_menu(self, pm):
        pm.login_page.open_login_page()
        pm.login_page.login_standard_user()
        pm.products_page.verify_burger_menu_closed()
        pm.products_page.open_burger_menu()
        pm.products_page.verify_burger_menu_opened()
        pm.products_page.close_burger_menu()
        pm.products_page.verify_burger_menu_closed()

    #TODO: add check if menu already opened?
    def test_burger_menu_all_items(self, pm):
        pm.login_page.open_login_page()
        pm.login_page.login_standard_user()
        pm.products_page.open_burger_menu()
        expect(pm.products_page.burger_menu_all_items).to_have_attribute("href","#")
        pm.products_page.burger_menu_all_items.click()

    def test_burger_menu_about(self, pm):
        pm.login_page.open_login_page()
        pm.login_page.login_standard_user()
        pm.products_page.open_burger_menu()
        expect(pm.products_page.burger_menu_about).to_have_attribute("href","https://saucelabs.com/")
        pm.products_page.open_about_page()
        expect(pm.about_page.page).to_have_url("https://saucelabs.com/")
        expect(pm.about_page.page).to_have_title("Sauce Labs: Cross Browser Testing, Selenium Testing & Mobile Testing")

    def test_burger_menu_logout(self, pm):
        pm.login_page.open_login_page()
        pm.login_page.login_standard_user()
        pm.products_page.open_burger_menu()
        expect(pm.products_page.burger_menu_logout).to_have_attribute("href","#")
        pm.products_page.logout()
        expect(pm.login_page.page).to_have_url("https://www.saucedemo.com/")
        expect(pm.login_page.page).to_have_title("Swag Labs")

    def test_get_all_items(self, pm):
        pm.login_page.open_login_page()
        pm.login_page.login_standard_user()
        items = pm.products_page.get_all_items()
        pm.products_page.verify_product_items(items)

    def test_random_item(self, pm):
        pm.login_page.open_login_page()
        pm.login_page.login_standard_user()
        item = pm.products_page.get_random_item()
        pm.products_page.verify_product_item(item)

    # How to optimize?
    def test_add_to_cart_single_item(self, pm):
        pm.login_page.open_login_page()
        pm.login_page.login_standard_user()
        item = pm.products_page.get_random_item()
        expect(pm.products_page.shopping_cart_count).not_to_be_visible()
        pm.products_page.add_to_cart(item)
        expect(pm.products_page.shopping_cart_count).to_have_text("1")
        expect(item.remove_button).to_be_visible()
        expect(item.add_button).not_to_be_visible()

    #How to optimize?
    def test_remove_from_cart_single_item(self, pm):
        pm.login_page.open_login_page()
        pm.login_page.login_standard_user()
        item = pm.products_page.get_random_item()
        expect(pm.products_page.shopping_cart_count).not_to_be_visible()
        pm.products_page.add_to_cart(item)
        expect(pm.products_page.shopping_cart_count).to_have_text("1")
        expect(item.remove_button).to_be_visible()
        expect(item.add_button).not_to_be_visible()
        pm.products_page.remove_from_cart(item)
        expect(pm.products_page.shopping_cart_count).not_to_be_visible()
        expect(item.add_button).to_be_visible()
        expect(item.remove_button).not_to_be_visible()

    # How to optimize?
    def test_add_to_cart_multi_items(self, pm):
        pm.login_page.open_login_page()
        pm.login_page.login_standard_user()
        item1 = pm.products_page.get_item(0)
        item2 = pm.products_page.get_item(1)
        pm.products_page.add_to_cart(item1)
        pm.products_page.add_to_cart(item2)
        expect(pm.products_page.shopping_cart_count).to_have_text("2")

    # How to optimize?
    def test_remove_from_cart_multi_items(self, pm):
        pm.login_page.open_login_page()
        pm.login_page.login_standard_user()
        item1 = pm.products_page.get_item(0)
        item2 = pm.products_page.get_item(1)
        pm.products_page.add_to_cart(item1)
        pm.products_page.add_to_cart(item2)
        expect(pm.products_page.shopping_cart_count).to_have_text("2")
        pm.products_page.remove_from_cart(item1)
        pm.products_page.remove_from_cart(item2)