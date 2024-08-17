from selene import browser

from pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME_FIELD = browser.element('input[name=username]')
    PASSWORD_FIELD = browser.element('input[name=password]')
    SIGN_IN_BUTTON = browser.element('button[type=submit]')

    def authorise_with_credentials(self, username, password):
        self.USERNAME_FIELD.set_value(username)
        self.PASSWORD_FIELD.set_value(password)
        self.click_on(self.SIGN_IN_BUTTON)

    def click_on_sign_in_button(self):
        self.click_on(self.SIGN_IN_BUTTON)
