import pytest

from niffler_qa_5.clients.oauth_client import OAuthClient
from niffler_qa_5.models.config import Envs


@pytest.fixture(scope="session")
def auth_token(envs: Envs):
    return OAuthClient(envs).get_token(envs.test_username, envs.test_password)