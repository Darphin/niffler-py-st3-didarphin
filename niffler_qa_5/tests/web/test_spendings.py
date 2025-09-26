
from niffler_qa_5.marks import Pages
from niffler_qa_5.models.spend import Spend, SpendAdd
from niffler_qa_5.pages.main_page import MainPage
from niffler_qa_5.pages.spending_page import SpendingPage

spend_page = SpendingPage()
main_page = MainPage()

@Pages.auth_page
def test_incorrect_spending(clear_all_db_for_test_user, envs):
    spend_page.open_page(envs.spending_url)
    spend_page.click_add()
    spend_page.check_amount_error()

@Pages.auth_page
def test_new_spending(clear_all_db_for_test_user, category, envs):
    spend = SpendAdd().random_init(category=category.name)
    spend_page.open_page(envs.spending_url)
    spend_page.fill_amount(spend.amount)
    spend_page.fill_category(spend.category)
    spend_page.fill_description(spend.description)
    spend_page.click_add()
    assert main_page.get_element_count()==1
    pass

