import pytest as pytest

from niffler_qa_5.marks import Pages
from niffler_qa_5.models.spend import SpendAdd
from niffler_qa_5.pages.main_page import MainPage

import allure
from niffler_qa_5.marks import Labels, Feature

page = MainPage()

@allure.label(Labels.web)
@allure.feature(Feature.history)

class TestHistorySpendingWeb:
    @Pages.auth_page
    @pytest.mark.parametrize(
        'list_of_spend',
        [
            [
                SpendAdd().random_init(description="name"),
                SpendAdd().random_init(),
                SpendAdd().random_init()]
        ],
        indirect=True
    )
    def test_find_spending_by_name(self, clear_all_db_for_test_user, list_of_spend, envs):
        page.open_main_page(envs.frontend_url)
        assert page.get_element_count()==3
        page.filter_element("name")
        assert page.get_element_count() == 1

    @Pages.auth_page
    @pytest.mark.parametrize(
        'list_of_spend',
        [
            [
                SpendAdd().random_init(),
                SpendAdd().random_init(),
            ]
        ],
        indirect=True
    )
    def test_delete_1_row(self, clear_all_db_for_test_user, list_of_spend, envs):
        page.open_main_page(envs.frontend_url)
        assert page.get_element_count() == 2
        page.check_row(1)
        page.delete_checked_rows()
        assert page.get_element_count() == 1

    @Pages.auth_page
    @pytest.mark.parametrize(
        'list_of_spend',
        [
            [
                SpendAdd().random_init(),
                SpendAdd().random_init(),
            ]
        ],
        indirect=True
    )
    def test_delete_all_rows(self, clear_all_db_for_test_user, list_of_spend, envs):
        page.open_main_page(envs.frontend_url)
        assert page.get_element_count() == 2
        page.check_all_rows()
        page.delete_checked_rows()
        page.check_empty_history()

    @Pages.auth_page
    @pytest.mark.parametrize(
        'list_of_spend',
        [
            [
                SpendAdd().random_init(),
                SpendAdd().random_init(currency='KZT'),
            ]
        ],
        indirect=True
    )
    def test_filter_by_currency(self, clear_all_db_for_test_user, list_of_spend, envs):
        page.open_main_page(envs.frontend_url)
        assert page.get_element_count() == 2
        page.filter_currency("KZT")
        assert page.get_element_count()==1
