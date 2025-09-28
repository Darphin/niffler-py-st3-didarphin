from selene import browser, by, have
import allure

class SpendingPage:
    @allure.step("Open main page")
    def open_page(self, spending_url):
        browser.driver.maximize_window()
        browser.open(spending_url)
        return self

    @allure.step("Fill amount")
    def fill_amount(self, amount):
        browser.element(by.name('amount')).type(amount)

    @allure.step("Fill description")
    def fill_description(self, description):
        browser.element(by.name('description')).type(description)

    @allure.step("Fill category")
    def fill_category(self, category):
        browser.element(by.name('category')).type(category)

    @allure.step("Fill currency")
    def fill_currency(self, currency):
        browser.element(by.name('currency')).type(currency)

    @allure.step("Click add button")
    def click_add(self):
        browser.element('[type=submit]').click()

    @allure.step("Check amount error")
    def check_amount_error(self):
        browser.element(".input__helper-text").should(have.text("Amount has to be not less then 0.01"))

    @allure.step("Check category error")
    def check_category_error(self):
        browser.element(".input_helper-text").should(have.text("Please choose category"))