import pytest


class Pages:
    auth_page = pytest.mark.usefixtures("auth")
    main_page = pytest.mark.usefixtures("main_page")
    spending_page = pytest.mark.usefixtures("spending_page")

class TestData:
    category = lambda x: pytest.mark.parametrize("category", [x], indirect=True)
    spends = lambda x: pytest.mark.parametrize("spends", [x], indirect=True, ids=lambda param: param.description)

class Feature:
    login = "Login test"
    singin = "Sign in test"
    spending = "Spend test"
    history = "History test"
    category = "Category test"
    statistics = "Statistics test"

class Labels:
    api = "API test"
    web = "WEB test"
    db = "Database test"
