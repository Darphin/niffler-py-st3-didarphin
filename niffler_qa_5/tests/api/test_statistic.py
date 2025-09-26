import pytest as pytest

from niffler_qa_5.clients.spends_client import SpendsHttpClient
from datetime import datetime

from niffler_qa_5.models.spend import SpendAdd


@pytest.mark.parametrize(
    'spend_fixture',
    [
        SpendAdd(amount=108.51,
                 description="QA.GURU Python Advanced 1",
                 category={"name": "new_cat"},
                 spendDate="2024-08-08T18:39:27.955Z",
                 currency="RUB"),
        SpendAdd(amount=108.51,
                 description="QA.GURU Python Advanced 1",
                 category={"name": "new_cat2"},
                 spendDate="2024-08-08T18:39:27.955Z",
                 currency="USD"),
        SpendAdd(amount=108.51,
                 description="QA.GURU Python Advanced 1",
                 category={"name": "new_cat3"},
                 spendDate="2024-08-08T18:39:27.955Z",
                 currency="KZT"),
        SpendAdd(amount=108.51,
                 description="QA.GURU Python Advanced 1",
                 category={"name": "new_cat4"},
                 spendDate="2024-08-08T18:39:27.955Z",
                 currency="EUR")
    ],
    indirect=True, ids=["RUB", "USD", 'KZT', 'EUR']
)
def test_get_statistic_1_spend_and_currency(envs, auth_token, clear_all_db_for_test_user, spend_fixture):
    client = SpendsHttpClient(envs.gateway_url, auth_token)
    result_stat = client.get_statistics(username=envs.test_username, user_currency=spend_fixture["currency"],
                                        from_value=datetime.today(), to_value=datetime.today(),
                                        filter_currency=spend_fixture["currency"])
    assert len(result_stat) == 4
    for x in result_stat:
        if x["currency"] == spend_fixture['currency']:
            assert x["total"] == spend_fixture['amount']
            assert len(x['categoryStatistics']) == 1
            stat = x['categoryStatistics'][0]
            assert stat['total'] == spend_fixture['amount']
            assert stat["category"] == spend_fixture['category']['name']
            assert len(stat["spends"]) == 1
        else:
            assert x["total"] == 0.0

@pytest.mark.parametrize(
    'list_of_spend',
    [
        [SpendAdd(amount=108.51,
                 description="QA.GURU Python Advanced 1",
                 category={"name": "new_cat"},
                 spendDate="2024-08-08T18:39:27.955Z",
                 currency="RUB"),
        SpendAdd(amount=1,
                 description="QA.GURU Python Advanced 1",
                 category={"name": "new_cat2"},
                 spendDate="2024-08-08T18:39:27.955Z",
                 currency="USD"),
        SpendAdd(amount=1500,
                 description="QA.GURU Python Advanced 1",
                 category={"name": "new_cat3"},
                 spendDate="2024-08-08T18:39:27.955Z",
                 currency="KZT"),
        SpendAdd().random_init()]
    ],
    indirect=True, ids = ["different_currency"]
)
def test_get_statistic_some_spends(envs, auth_token, clear_all_db_for_test_user, list_of_spend):
    client = SpendsHttpClient(envs.gateway_url, auth_token)
    result_stat = client.get_statistics(username=envs.test_username,
                                        from_value=datetime.today(), to_value=datetime.today())
    assert len(result_stat) == 4
