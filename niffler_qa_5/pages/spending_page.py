from urllib.parse import urljoin

from selene import browser, by, have


class SpendingPage:
    def open_page(self, spending_url):
        browser.driver.maximize_window()
        browser.open(spending_url)
        return self

    def fill_amount(self, amount):
        browser.element(by.name('amount')).type(amount)

    def fill_description(self, description):
        browser.element(by.name('description')).type(description)

    def fill_category(self, category):
        browser.element(by.name('category')).type(category)

    def fill_currency(self, currency):
        browser.element(by.name('currency')).type(currency)


    def click_add(self):
        browser.element('[type=submit]').click()

    def check_amount_error(self):
        browser.element(".input__helper-text").should(have.text("Amount has to be not less then 0.01"))

    def check_category_error(self):
        browser.element(".input_helper-text").should(have.text("Please choose category"))