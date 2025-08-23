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