from playwright.sync_api import Page

from src.pages.about_page import AboutPage
from src.pages.facebook_page import FacebookPage
from src.pages.linkedin_page import LinkedInPage
from src.pages.login_page import LoginPage
from src.pages.products_page import ProductsPage
from src.pages.twitter_page import TwitterPage


class PagesManager:
    def __init__(self, page: Page):
        self.login_page = LoginPage(page)
        self.products_page = ProductsPage(page)
        self.about_page = AboutPage(page)
        self.facebook_page = FacebookPage(page)
        #self.twitter_page = TwitterPage(page)
        self.twitter_page = None
        self.linkedin_page = LinkedInPage(page)

    @property
    def twitter(self):
        return self.twitter_page

    @twitter.setter
    def twitter(self, page: Page):
        if self.twitter_page is None:
            self.twitter_page = TwitterPage(page)
