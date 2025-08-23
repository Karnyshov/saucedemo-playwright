from playwright.sync_api import Page,expect
import abc


class BasePage(abc.ABC):
    def __init__(self, page: Page) -> None:
        self.page = page
        self.base_url = "https://www.saucedemo.com/"

        self.app_logo = page.locator("//div[@class=\"app_logo\"]")
        self.title = page.locator("//title")

        self.burger_button = page.locator("//button[@id=\"react-burger-menu-btn\"]")
        self.burger_close_button = page.locator("//button[@id=\"react-burger-cross-btn\"]")
        self.burger_menu = page.locator("//div[@class=\"bm-menu-wrap\"]")
        self.burger_menu_all_items = page.locator("//a[@id=\"inventory_sidebar_link\"]")
        self.burger_menu_about = page.locator("//a[@id=\"about_sidebar_link\"]")
        self.burger_menu_logout = page.locator("//a[@id=\"logout_sidebar_link\"]")
        self.burger_menu_reset = page.locator("//a[@id=\"reset_sidebar_link\"]")

        self.shopping_cart = page.locator("//a[@class=\"shopping_cart_link\"]")
        self.shopping_cart_count = page.locator("//span[@class=\"shopping_cart_badge\"]")

        self.footer_copyright = page.locator("//footer/div[@class=\"footer_copy\"]")
        self.footer_twitter = page.locator("//footer/ul/li[@class=\"social_twitter\"]/a")
        self.footer_facebook = page.locator("//footer/ul/li[@class=\"social_facebook\"]/a")
        self.footer_linkedin = page.locator("//footer/ul/li[@class=\"social_linkedin\"]/a")

    def verify_burger_menu_opened(self) -> None:
        expect(self.burger_menu).not_to_be_hidden()
        expect(self.burger_close_button).not_to_have_attribute("tabindex","-1")
        expect(self.burger_menu_all_items).not_to_have_attribute("tabindex","-1")
        expect(self.burger_menu_about).not_to_have_attribute("tabindex","-1")
        expect(self.burger_menu_logout).not_to_have_attribute("tabindex","-1")
        expect(self.burger_menu_reset).not_to_have_attribute("tabindex","-1")

    def verify_burger_menu_closed(self) -> None:
        expect(self.burger_menu).to_be_hidden()
        expect(self.burger_close_button).to_have_attribute("tabindex","-1")
        expect(self.burger_menu_all_items).to_have_attribute("tabindex","-1")
        expect(self.burger_menu_about).to_have_attribute("tabindex","-1")
        expect(self.burger_menu_logout).to_have_attribute("tabindex","-1")
        expect(self.burger_menu_reset).to_have_attribute("tabindex","-1")

    def open_burger_menu(self) -> None:
        self.burger_button.click()
        self.verify_burger_menu_opened()

    def close_burger_menu(self) -> None:
        self.burger_close_button.click()
        self.verify_burger_menu_closed()

    def click_footer_button(self, locator):
        with self.page.context.expect_page() as new_page_info:
            locator.click()

        return new_page_info.value

    def verify_copyright(self) -> None:
        expect(self.footer_copyright).not_to_be_empty()
        expect(self.footer_copyright).to_have_text("© 2025 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy")

    def verify_footer_twitter(self) -> None:
        expect(self.footer_twitter).to_have_attribute("href", "https://twitter.com/saucelabs")
        expect(self.footer_twitter).to_have_text("Twitter")

    def verify_footer_facebook(self) -> None:
        expect(self.footer_facebook).to_have_attribute("href","https://www.facebook.com/saucelabs")
        expect(self.footer_facebook).to_have_text("Facebook")

    def verify_footer_linkedin(self) -> None:
        expect(self.footer_linkedin).to_have_attribute("href","https://www.linkedin.com/company/sauce-labs/")
        expect(self.footer_linkedin).to_have_text("LinkedIn")