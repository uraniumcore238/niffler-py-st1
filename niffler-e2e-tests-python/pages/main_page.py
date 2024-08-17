from selene import browser, be, have
from pages.base_page import BasePage


class MainPage(BasePage):

    LOGOUT_BUTTON = browser.element("[data-tooltip-id='logout']")
    MAIN_CONTENT = browser.element('.main-content')
    TABLE_BODY = browser.element('.spendings-table tbody')
    CHECKBOX_ALL = browser.element('.spendings-table tbody input[type=checkbox]')
    DELETE_SELECTED_BUTTON = browser.element('.spendings__bulk-actions button')
    SPENDING_CONTENT = browser.element('.spendings__content')

    def logout_button_should_be_visible(self):
        self.LOGOUT_BUTTON.matching(be.visible)

    def get_user_token(self):
        return browser.driver.execute_script('return window.sessionStorage.getItem("id_token")')

    def main_content_should_have_text(self, text):
        self.MAIN_CONTENT.should(have.text(text))

    def spending_content_should_have_text(self, text):
        self.SPENDING_CONTENT.should(have.text(text))

    def table_should_have_text(self, text):
        self.TABLE_BODY.should(have.text(text))

    def click_on_select_all_checkbox(self):
        self.click_on(self.CHECKBOX_ALL)


    def click_on_delete_selected_button(self):
        self.click_on(self.DELETE_SELECTED_BUTTON)

