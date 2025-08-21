from playwright.sync_api import expect, Playwright
from tests.conftest import page_manager as pm
from src.pages.twitter_page import TwitterPage

class TestProducts:
    #TODO: add more checks
    def test_basic_state(self, pm):
        pm.login_page.open_login_page()
        pm.login_page.login_standard_user()
        pm.products_page.verify_burger_menu_closed()

    def test_footer(self, pm):
        pm.login_page.open_login_page()
        pm.login_page.login_standard_user()
        expect(pm.products_page.footer_copyright).not_to_be_empty()
        expect(pm.products_page.footer_copyright).to_have_text("© 2025 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy")
        expect(pm.products_page.footer_twitter).to_have_attribute("href", "https://twitter.com/saucelabs")
        expect(pm.products_page.footer_twitter).to_have_text("Twitter")
        expect(pm.products_page.footer_facebook).to_have_attribute("href","https://www.facebook.com/saucelabs")
        expect(pm.products_page.footer_facebook).to_have_text("Facebook")
        expect(pm.products_page.footer_linkedin).to_have_attribute("href","https://www.linkedin.com/company/sauce-labs/")
        expect(pm.products_page.footer_linkedin).to_have_text("LinkedIn")

    def test_footer_twitter(self, pm):
        pm.login_page.open_login_page()
        pm.login_page.login_standard_user()
        #returns page that can be used to create Page Object. But Page Object is already initialized
        with pm.products_page.page.context.expect_page() as new_page_info:
            pm.products_page.footer_twitter.click()

        twitter_page = TwitterPage(new_page_info.value)
        twitter_page.page.wait_for_load_state()
        expect(twitter_page.page).to_have_url("https://x.com/saucelabs")
        expect(twitter_page.page).to_have_title("Sauce Labs (@saucelabs) / X")

    def test_footer_twitter1(self, pm):
        pm.login_page.open_login_page()
        pm.login_page.login_standard_user()

        #returns page, but not Page Object, and it needs to already initialized Page Object
        twitter = pm.products_page.click_footer_twitter_button(pm.twitter_page.page.context)
        expect(twitter).to_have_url("https://x.com/saucelabs")

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