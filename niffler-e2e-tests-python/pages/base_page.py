import os
import time
from datetime import datetime, timedelta

from selene import browser, command
# import allure
# import keyboard
# from dotenv import load_dotenv
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    # def __init__(self, driver: WebDriver, timeout=5):
    #     self.driver = driver
    #     self.driver.implicitly_wait(timeout)

    def click_on(self, locator):
        # locator.perform(command.js.scroll_into_view).click()
        locator.click()

    def go_to_element(self, locator):
        locator.perform(command.js.scroll_into_view)
        # browser.driver.execute_script("arguments[0].scrollIntoView();", element)




    # def click_on(self, locator, timeout=5):
    #     self.get_element(locator, timeout=timeout).click()



    #
    #
    # def open(self, url):
    #     self.driver.get(url)
    #
    # # @allure.step('Подождать видимость элемента')
    # def get_element(self, locator: tuple, timeout=10):
    #     wait = WebDriverWait(self.driver, timeout)
    #     return wait.until(EC.visibility_of_element_located(locator), ' : '.join(locator))
    #
    # def get_element_without_wait(self, locator: tuple):
    #     return self.driver.find_element(*locator)
    #
    # def get_elements_without_wait(self, locator: tuple):
    #     return self.driver.find_elements(*locator)
    #
    # def get_elements(self, locator: tuple, timeout=5):
    #     wait = WebDriverWait(self.driver, timeout)
    #     return wait.until(EC.visibility_of_any_elements_located(locator), ' : '.join(locator))
    #
    # def get_present_elements(self, locator: tuple, timeout=5):
    #     wait = WebDriverWait(self.driver, timeout)
    #     return wait.until(EC.presence_of_all_elements_located(locator), ' : '.join(locator))
    #
    # def go_to_element(self, element):
    #     self.driver.execute_script("arguments[0].scrollIntoView();", element)
    #
    # def go_to_page_bottom(self):
    #     self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)", "")
    #
    # def elements_are_visible(self, locator, timeout=5):
    #     wait = WebDriverWait(self.driver, timeout)
    #     return wait.until(EC.visibility_of_all_elements_located(locator))
    #
    # def get_clickable_element(self, locator: tuple, timeout=10):
    #     wait = WebDriverWait(self.driver, timeout)
    #     return wait.until(EC.element_to_be_clickable(locator))
    #
    # # Проверка присутсвия элемента на странице
    # def is_element_present(self, locator: tuple):
    #     try:
    #         self.driver.find_element(*locator)
    #     except NoSuchElementException:
    #         return False
    #     return True
    #
    # def check_elements(self, item_list: tuple, count):
    #     item_count = 0
    #     while count != 0:
    #         item = item_list[item_count]
    #         if count > 0:
    #             self.go_to_element(item)
    #             count -= 1
    #             item_count += 1
    #         else:
    #             break
    #
    # def get_element_by_text(self, text):
    #     return self.driver.find_element(By.XPATH, f"//*[contains(text(), '{text}')]")
    #
    # # @allure.step('Нажать на элемент')
    #
    #
    # # @allure.step('Выбрать чекбокс')
    # def select_checkbox(self, locator, timeout=5):
    #     if "checked" in self.get_element(locator, timeout).get_attribute('class'):
    #         pass
    #     else:
    #         self.get_element(locator, timeout=timeout).click()
    #
    # # @allure.step('Получить токен из DevTools > Application > Storage')
    # def get_token(self):
    #     return self.driver.execute_script("return window.localStorage.getItem('token')")
    #
    # def refresh_page(self, timeout: int = 5):
    #     time.sleep(timeout)
    #     self.driver.refresh()
    #
    # # @allure.step('Очистить инпут')
    # def clear_input(self, element):
    #     element.click()
    #     element.send_keys(Keys.BACKSPACE*10)
    #
    # # @allure.step('Навести курсор на элемент')
    # def hover_cursor_over_element(self, locator):
    #     element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
    #     ActionChains(self.driver).move_to_element(element).perform()
    #
    # # @allure.step('Нажатие на стрелки вниз дважды,а затем "Entrer"')
    # def click_enter(self):
    #     keyboard.send(84)
    #     keyboard.send(84)
    #     keyboard.send('enter')
    #
    # @allure.step('Ожидание отображения элемента')
    # def wait_for_element(self, locator):
    #     WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
    #
    # @allure.step('Ожидание что элемент скрыт')
    # def wait_for_invisibility_of_element(self, locator):
    #     WebDriverWait(self.driver, 60).until(EC.invisibility_of_element(locator))
    #
    # def assert_text_in_element(self, locator, text):
    #     with allure.step(f'Ожидание что в элементе отобразится текст - {text}'):
    #         WebDriverWait(self.driver, timeout=10, poll_frequency=0.1).until(EC.text_to_be_present_in_element(locator, text))
    #
    # def assert_text_in_url(self, url):
    #     with allure.step(f'Проверить что текущий url содержит {url}'):
    #         WebDriverWait(self.driver, 5, poll_frequency=0.1).until(EC.url_contains(url))
    #
    # def switch_on_tab(self, handle):
    #     with allure.step(f'Переключиться на вкладку {handle}'):
    #         for handle in self.driver.window_handles:
    #             self.driver.switch_to.window(handle)
    #
    # @allure.step('Ожидание что элемент кликабельный')
    # def wait_for_clickable_element(self, locator):
    #     WebDriverWait(self.driver, 10, poll_frequency=0.1).until(EC.element_to_be_clickable(locator))
    #
    # @allure.step('Получить id сессии браузера')
    # def get_browser_session_id(self):
    #     return self.driver.session_id
    #
