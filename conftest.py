from urllib.parse import urljoin

from dotenv import load_dotenv
import pytest

import os
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from niffler_qa_5.clients.spends_client import SpendsHttpClient
from niffler_qa_5.databases.spend_db import SpendDB
from niffler_qa_5.models.config import Envs


pytest_plugins = ["niffler_qa_5.fixtures.auth_fixtures", "niffler_qa_5.fixtures.client_fixtures"]

@pytest.fixture(scope="session")
def envs() -> Envs:
    load_dotenv()
    return Envs(
        frontend_url=os.getenv("FRONTEND_URL"),
        gateway_url=os.getenv("GATEWAY_URL"),
        spending_url=os.getenv("SPENDING_URL"),
        app_url=os.getenv("APP_URL"),
        test_username=os.getenv("TEST_USERNAME"),
        test_password=os.getenv("TEST_PASSWORD"),
        auth_url=os.getenv("AUTH_URL"),
        auth_secret=os.getenv("AUTH_SECRET"),
        spend_db_url=os.getenv("SPEND_DB_URL")
    )

def pytest_addoption(parser):
    parser.addoption("--env", default="dev")


@pytest.fixture(scope="module")
def auth(envs):
    username, password = envs.test_username, envs.test_password
    browser.driver.maximize_window()
    browser.open(envs.frontend_url)
    browser.element('input[name=username]').set_value(username)
    browser.element('input[name=password]').set_value(password)
    browser.element('button[type=submit]').click()


@pytest.fixture(scope="session")
def spends_client(gateway_url, main_page) -> SpendsHttpClient:
    return SpendsHttpClient(gateway_url, main_page)

@pytest.fixture(scope='function')
def spend_db(envs):
    return SpendDB(envs.spend_db_url)


@pytest.fixture(params=[])
def spends(request, spends_client):
    spend = spends_client.add_spends(request.param)
    yield spend
    try:
        spends_client.remove_spends([spend["id"]])
    except Exception:
        pass

@pytest.fixture(scope="function")
def main_page(auth, envs):
    browser.open(envs.frontend_url)


