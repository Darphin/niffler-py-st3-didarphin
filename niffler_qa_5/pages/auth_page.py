from selene import browser, by, have


class AuthPage:
    def open_main_page(self, app_url):
        browser.open(app_url)
        return self

    def fill_username(self, name):
        browser.element(by.name('username')).type(name)

    def fill_password(self, password):
        browser.element(by.name('password')).type(password)

    def click_login(self):
        browser.element('[type=submit]').click()

    def click_register(self):
        browser.element('.form__register').click()
    def check_auth(self):
        pass

    def check_incorrect_pass_label(self):
        browser.element(".form__error").should(have.text("Неверные учетные данные пользователя"))



