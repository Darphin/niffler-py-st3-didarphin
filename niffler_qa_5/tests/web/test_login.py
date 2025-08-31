import pytest as pytest

from niffler_qa_5.pages.auth_page import AuthPage

auth_page = AuthPage()
def test_success_auth(app_url):
    auth_page.open_main_page(app_url)
    auth_page.fill_username("didarphin")
    auth_page.fill_password("123")
    auth_page.click_login()

@pytest.mark.parametrize("login, password", [("didarphin","1234"),("di","123")],
                         ids=["Incorrect login", "Incorrect password"])
def test_unsuccess_login(app_url, login, password):
    auth_page.open_main_page("http://frontend.niffler.dc/main")
    auth_page.fill_username(login)
    auth_page.fill_password(password)
    auth_page.click_login()
    auth_page.check_incorrect_pass_label()
