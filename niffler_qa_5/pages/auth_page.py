from selene import browser, by, have
import allure

class AuthPage:
    @allure.step("Open auth page")
    def open_main_page(self, app_url):
        browser.open(app_url)
        return self

    @allure.step("Fill username block")
    def fill_username(self, name):
        browser.element(by.name('username')).type(name)

    @allure.step("Fill password block")
    def fill_password(self, password):
        browser.element(by.name('password')).type(password)

    @allure.step("Click login button")
    def click_login(self):
        browser.element('[type=submit]').click()

    @allure.step("Click register button")
    def click_register(self):
        browser.element('.form__register').click()

    @allure.step("Open auth page")
    def check_auth(self):
        pass

    @allure.step("Check incorrect login label")
    def check_incorrect_pass_label(self):
        browser.element(".form__error").should(have.text("Неверные учетные данные пользователя"))



