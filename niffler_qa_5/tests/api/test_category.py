from niffler_qa_5.clients.spends_client import SpendsHttpClient
from niffler_qa_5.databases.spend_db import SpendDB
from niffler_qa_5.models.spend import SpendAdd
import allure
from niffler_qa_5.marks import Labels, Feature

@allure.label(Labels.api)
@allure.feature(Feature.category)
class TestCategoryApi:
    def test_add_category(self, envs, auth_token, clear_all_db_for_test_user):
        name = "new_cat"
        client = SpendsHttpClient(envs.gateway_url, auth_token)
        result_category = client.add_category(name)
        with allure.step('Check adding category'):
            assert result_category.name == name
            assert result_category.username == envs.test_username

    def test_update_category(self, envs, auth_token, clear_all_db_for_test_user, category):
        name = "new_dog"
        client = SpendsHttpClient(envs.gateway_url, auth_token)
        client.update_category(id=category.id, name=name)
        with allure.step('Check updating category'):
            assert SpendDB(envs.spend_db_url).get_category_by_id(category.id).name == name


    def test_delete_category(self, envs, auth_token, clear_all_db_for_test_user, category):
        db_session = SpendDB(envs.spend_db_url)
        db_session.delete_category(category.id)
        res=db_session.get_category_by_id(category.id)
        with allure.step('Check deleting of category'):
            assert res is None


    def test_delete_category_with_spend(self, envs, auth_token, clear_all_db_for_test_user, category):
        spend_client=SpendsHttpClient(envs.gateway_url, auth_token)
        spend =spend_client.add_spends(
            SpendAdd(amount=108.51,
                     description="QA.GURU Python Advanced 1",
                     category={"name": category.name},
                     spendDate="2024-08-08T18:39:27.955Z",
                     currency="RUB"))
        db_session = SpendDB(envs.spend_db_url)
        res_delete=db_session.delete_category(category.id)
        with allure.step('Check constraint for deleting category with spends'):
            assert 'update or delete on table "category" violates foreign key constraint "fk_spend_category" on table "spend"' in res_delete
            res = db_session.get_category_by_id(category.id)
            assert str(res.id) == category.id
            spend_client.remove_spends(ids=[spend['id']])

    def test_category_count_constraint(self, envs, auth_token, clear_all_db_for_test_user):
        spend_client = SpendsHttpClient(envs.gateway_url, auth_token)
        categories_list = [spend_client.add_category(name="name"+str(x)) for x in range(8)]
        last_category_error = spend_client.add_category("last")
        with allure.step('Check count constraint when adding categories'):
            assert "Can`t add over than 8 categories" in last_category_error.text
            assert last_category_error.status_code == 406




