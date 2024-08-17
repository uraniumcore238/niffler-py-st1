import os

import pytest
from dotenv import load_dotenv
from selene import browser
from selene.support.conditions import be

from clients.spends_client import SpendsHttpClient
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.welcome_page import WelcomePage


@pytest.fixture(scope="session")
def envs():
    load_dotenv()


@pytest.fixture(scope="session")
def frontend_url(envs):
    return os.getenv("FRONTEND_URL")


@pytest.fixture(scope="session")
def gateway_url(envs):
    return os.getenv("GATEWAY_URL")


@pytest.fixture(scope="session")
def app_user(envs):
    return os.getenv("TEST_USERNAME"), os.getenv("TEST_PASSWORD")


@pytest.fixture(scope="session")
def auth(frontend_url, app_user):
    welcome_page = WelcomePage()
    login_page = LoginPage()
    main_page = MainPage()
    username, password = app_user

    browser.open(frontend_url)
    welcome_page.click_on_login_button()
    login_page.authorise_with_credentials(username, password)
    login_page.click_on_sign_in_button()
    main_page.logout_button_should_be_visible()
    return main_page.get_user_token()

@pytest.fixture(scope="session")
def auth_client(gateway_url, auth) -> SpendsHttpClient:
    return SpendsHttpClient(gateway_url, auth)



@pytest.fixture(scope="session")
def spends_client(gateway_url, auth) -> SpendsHttpClient:
    return SpendsHttpClient(gateway_url, auth)


@pytest.fixture(params=[])
def category(request, spends_client):
    category_name = request.param
    current_categories = spends_client.get_categories()
    category_names = [category["category"] for category in current_categories]
    if category_name not in category_names:
        spends_client.add_category(category_name)
    return category_name


@pytest.fixture(params=[])
def spends(request, spends_client):
    spend = spends_client.add_spends(request.param)
    yield spend
    try:
        # TODO вместо исключения проверить список текущих spends
        spends_client.remove_spends([spend["id"]])
    except Exception:
        pass


@pytest.fixture()
def main_page(auth, frontend_url):
    browser.open(frontend_url)
