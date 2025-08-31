import random

import pytest as pytest
from faker import Faker
from niffler_qa_5.pages.auth_page import AuthPage
from niffler_qa_5.pages.register_page import RegisterPage

register_page = RegisterPage()
auth_page = AuthPage()

@pytest.mark.parametrize("name, password, password_submit, error",
                         [("di", "1234", "1234",
                           "Allowed username length should be from 3 to 50 characters"),
                          ("diana", "12", "12",
                           "Allowed password length should be from 3 to 12 characters"),
                          ("diana", "1234567890abc", "1234567890abc",
                           "Allowed password length should be from 3 to 12 characters"),
                          ("diana", "123", "1234",
                           "Passwords should be equal"),
                          ("didarphin", "123", "123",
                          "Username `didarphin` already exists")],
                         ids=["Incorrect login", "Short password", "Long password", "Passwords not equal",
                              "Account exists"])
def test_incorrect_data(app_url, name, password, password_submit, error):
    auth_page.open_main_page(app_url)
    auth_page.click_register()
    register_page.fill_username(name)
    register_page.fill_password(password)
    register_page.fill_password_submit(password_submit)
    register_page.click_register()
    register_page.check_incorrect_pass_label(error)

def test_register(app_url):
    fake = Faker("en_US")
    name = fake.name()
    passw = fake.password(5)

    auth_page.open_main_page(app_url)
    auth_page.click_register()
    register_page.fill_username(name)
    register_page.fill_password(passw)
    register_page.fill_password_submit(passw)
    register_page.click_register()
    register_page.check_correct()


