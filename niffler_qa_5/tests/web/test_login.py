import pytest as pytest

from niffler_qa_5.pages.auth_page import AuthPage
from niffler_qa_5.pages.main_page import MainPage

from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


main_page = MainPage()
auth_page = AuthPage()

class TestLogin:
    @pytest.fixture(scope="function")
    def incognito_loh(self, envs):
        options = Options()
        options.add_argument("--incognito")
        browser.config.driver = webdriver.Chrome(options=options)

    def test_success_auth(self, incognito_loh, envs, clear_all_db_for_test_user):
        auth_page.open_main_page(envs.frontend_url)
        auth_page.fill_username(envs.test_username)
        auth_page.fill_password(envs.test_password)
        auth_page.click_login()
        main_page.check_main_page()


    @pytest.mark.parametrize("login, password", [("didarphin", "1234"), ("di", "123")],
                             ids=["Incorrect login", "Incorrect password"])
    def test_unsuccess_login(self, incognito_loh, envs, login, password):
        auth_page.open_main_page(envs.frontend_url)
        auth_page.fill_username(login)
        auth_page.fill_password(password)
        auth_page.click_login()
        auth_page.check_incorrect_pass_label()