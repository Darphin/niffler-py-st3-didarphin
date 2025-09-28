from selene import browser, by, have
import allure

class RegisterPage:
    @allure.step("Open main page ")
    def open_main_page(self, app_url):
        browser.open(app_url)
        return self

    @allure.step("Check empty history ")
    def fill_username(self, name):
        browser.element(by.name('username')).type(name)

    @allure.step("Check empty history ")
    def fill_password(self, password):
        browser.element(by.name('password')).type(password)

    @allure.step("Check empty history ")
    def fill_password_submit(self, password):
        browser.element(by.name('passwordSubmit')).type(password)

    @allure.step("Check empty history ")
    def click_register(self):
        browser.element('[type=submit]').click()

    @allure.step("Check empty history ")
    def check_auth(self):
        pass

    @allure.step("Check empty history ")
    def check_incorrect_pass_label(self, error):
        browser.element(".form__error").should(have.text(error))

    @allure.step("Check empty history ")
    def check_correct(self):
        browser.element(".form_sign-in").\
            should(have.text("Sign in"))