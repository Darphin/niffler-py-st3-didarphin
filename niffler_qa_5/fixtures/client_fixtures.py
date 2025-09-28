import pytest
from _pytest.fixtures import FixtureRequest

from niffler_qa_5.clients.oauth_client import OAuthClient
from niffler_qa_5.clients.spends_client import SpendsHttpClient
from niffler_qa_5.databases.spend_db import SpendDB
from niffler_qa_5.models.config import Envs


@pytest.fixture(scope="function")
def clear_all_db_for_test_user(envs: Envs):
    db_session = SpendDB(envs.spend_db_url)
    db_session.delete_all_spendings_for_user(username = envs.test_username)
    db_session.delete_all_categories_for_user(username= envs.test_username)

@pytest.fixture(scope="function")
def category(envs: Envs, auth_token):
    name = "new_cat"
    client = SpendsHttpClient(envs.gateway_url, auth_token)
    result_category = client.add_category(name)
    yield result_category
    SpendDB(envs.spend_db_url).delete_category(category_id=result_category.id)

@pytest.fixture(scope="function", params=[])
def spend_fixture(envs: Envs, auth_token, request: FixtureRequest):
    client = SpendsHttpClient(envs.gateway_url, auth_token)
    result_spend = client.add_spends(request.param)
    yield result_spend
    client.remove_spends(ids=[result_spend['id']])

@pytest.fixture(scope="function", params=[])
def list_of_spend(envs: Envs, auth_token, request: FixtureRequest):
    client = SpendsHttpClient(envs.gateway_url, auth_token)
    spend_list = [ client.add_spends(x) for x in request.param]
    yield spend_list
    client.remove_spends(ids=[x['id'] for x in spend_list])





