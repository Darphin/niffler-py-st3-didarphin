from urllib.parse import urljoin

from selene import browser, by, have, query


class MainPage:
    def open_main_page(self, frontend_url):
        browser.driver.maximize_window()
        browser.open(urljoin(frontend_url, "/main"))
        return self

    def check_main_page(self):
        browser.element(".MuiTypography-h5 ").should(have.text("Niffler"))

    def get_element_count(self):
        return int(browser.element('.css-1xnox0e').get(query.attribute("childElementCount")))

    def filter_element(self, filter_name):
        browser.element('.css-mnn31').type(filter_name).press_enter()

    def filter_currency(self, currency):
        browser.element('[id=currency]').press_enter()
        browser.element('[data-value=KZT]').press_enter()

    def check_row(self, number):
        browser.all('[type=checkbox]')[number].click()

    def check_all_rows(self):
        browser.element('.css-1m9pwf3').click()

    def delete_checked_rows(self):
        browser.element('[id=delete]').click()
        browser.element('[aria-describedby="alert-dialog-slide-description"]').element('.css-1v1p78s').click()

    def check_empty_history(self):
        assert browser.element('.css-1m7obeg').should(have.text("There are no spendings"))

