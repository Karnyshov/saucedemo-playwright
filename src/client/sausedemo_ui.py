from playwright.sync_api import Page
from src.pages.about_page import AboutPage
from src.pages.facebook_page import FacebookPage
from src.pages.linkedin_page import LinkedInPage
from src.pages.login_page import LoginPage
from src.pages.products_page import ProductsPage
from src.pages.twitter_page import TwitterPage
from src.pages.product_item_page import ItemPage

#Draft of improvement: https://chatgpt.com/s/t_68ae17983d148191b545e531cba62a21
#TODO: make lazy loading for all pages
class SauceDemoUI:
    def __init__(self, page: Page):
        self.login_page = LoginPage(page)
        self.products_page = ProductsPage(page)
        self.about_page = AboutPage(page)
        self.product_item_page = ItemPage(page)
        self.facebook_page = None
        self.twitter_page = None
        self.linkedin_page = None

    @property
    def twitter(self):
        return self.twitter_page

    @twitter.setter
    def twitter(self, page: Page):
        if self.twitter_page is None:
            self.twitter_page = TwitterPage(page)

    @property
    def facebook(self):
        return self.facebook_page

    @facebook.setter
    def facebook(self, page: Page):
        if self.facebook_page is None:
            self.facebook_page = FacebookPage(page)

    @property
    def linkedin(self):
        return self.linkedin_page

    @linkedin.setter
    def linkedin(self, page: Page):
        if self.linkedin_page is None:
            self.linkedin_page = LinkedInPage(page)
