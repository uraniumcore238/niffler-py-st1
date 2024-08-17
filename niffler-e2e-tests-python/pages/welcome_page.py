from selene import browser
from pages.base_page import BasePage


class WelcomePage(BasePage):

    LOGIN_BUTTON = browser.element('a[href*=redirect]')

    def click_on_login_button(self):
        self.click_on(self.LOGIN_BUTTON)
