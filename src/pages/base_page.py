from playwright.sync_api import Page
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
        self.footer_twitter = page.locator("//footer/ul/li[@class=\"social_twitter\"]")
        self.footer_facebook = page.locator("//footer/ul/li[@class=\"social_facebook\"]")
        self.footer_linkedin = page.locator("//footer/ul/li[@class=\"social_linkedin\"]")