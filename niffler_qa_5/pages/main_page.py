from urllib.parse import urljoin

from selene import browser, by, have, query
import allure

class MainPage:
    @allure.step("Open main page")
    def open_main_page(self, frontend_url):
        browser.driver.maximize_window()
        browser.open(urljoin(frontend_url, "/main"))
        return self

    @allure.step("Check main page")
    def check_main_page(self):
        browser.element(".MuiTypography-h5 ").should(have.text("Niffler"))

    @allure.step("Get elements in spends history table")
    def get_element_count(self):
        return int(browser.element('.css-1xnox0e').get(query.attribute("childElementCount")))

    @allure.step("Filter elements in spends history table by name")
    def filter_element(self, filter_name):
        browser.element('.css-mnn31').type(filter_name).press_enter()

    @allure.step("Filter elements in spends history table by currency")
    def filter_currency(self, currency):
        browser.element('[id=currency]').press_enter()
        browser.element('[data-value=KZT]').press_enter()

    @allure.step("Check row in spend history table")
    def check_row(self, number):
        browser.all('[type=checkbox]')[number].click()

    @allure.step("Check all rows in spend history table")
    def check_all_rows(self):
        browser.element('.css-1m9pwf3').click()

    @allure.step("Click delete button")
    def delete_checked_rows(self):
        browser.element('[id=delete]').click()
        browser.element('[aria-describedby="alert-dialog-slide-description"]').element('.css-1v1p78s').click()

    @allure.step("Check empty history ")
    def check_empty_history(self):
        assert browser.element('.css-1m7obeg').should(have.text("There are no spendings"))

