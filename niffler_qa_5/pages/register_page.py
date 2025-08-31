from selene import browser, by, have


class RegisterPage:
    def open_main_page(self, app_url):
        browser.open(app_url)
        return self

    def fill_username(self, name):
        browser.element(by.name('username')).type(name)

    def fill_password(self, password):
        browser.element(by.name('password')).type(password)

    def fill_password_submit(self, password):
        browser.element(by.name('passwordSubmit')).type(password)

    def click_register(self):
        browser.element('[type=submit]').click()

    def check_auth(self):
        pass

    def check_incorrect_pass_label(self, error):
        browser.element(".form__error").should(have.text(error))

    def check_correct(self):
        browser.element(".form_sign-in").\
            should(have.text("Sign in"))