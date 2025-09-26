import pytest


class Pages:
    auth_page = pytest.mark.usefixtures("auth")
    main_page = pytest.mark.usefixtures("main_page")
    spending_page = pytest.mark.usefixtures("spending_page")

class TestData:
    category = lambda x: pytest.mark.parametrize("category", [x], indirect=True)
    spends = lambda x: pytest.mark.parametrize("spends", [x], indirect=True, ids=lambda param: param.description)