from playwright.sync_api import expect
from tests.conftest import open_products_page as products_page
from tests.conftest import open_login_page

class TestProducts:
    #TODO: add more checks
    def test_basic_state(self, products_page):
        products_page.verify_burger_menu_closed()

    def test_footer(self):
        pass

    def test_burger_menu(self, products_page):
        products_page.verify_burger_menu_closed()
        products_page.open_burger_menu()
        products_page.verify_burger_menu_opened()
        products_page.close_burger_menu()
        products_page.verify_burger_menu_closed()

    #TODO: add check if menu already opened?
    def test_burger_menu_all_items(self, products_page):
        products_page.open_burger_menu()
        expect(products_page.burger_menu_all_items).to_have_attribute("href","#")
        products_page.burger_menu_all_items.click()

    #TODO: refine
    def test_burger_menu_about(self, products_page):
        products_page.open_burger_menu()
        expect(products_page.burger_menu_about).to_have_attribute("href","https://saucelabs.com/")
        about_page = products_page.open_about_page().page
        expect(about_page).to_have_url("https://saucelabs.com/")
        expect(about_page).to_have_title("Sauce Labs: Cross Browser Testing, Selenium Testing & Mobile Testing")

    def test_burger_menu_logout(self, products_page, open_login_page):
        products_page.open_burger_menu()
        expect(products_page.burger_menu_logout).to_have_attribute("href","#")
        #products_page.logout().page
        products_page.burger_menu_logout.click()

        expect(open_login_page).to_have_url("https://saucelabs.com/")
        expect(open_login_page).to_have_title("Swag Labs")