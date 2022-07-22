from selene import browser
from selene.support import by
from selene.support.jquery_style_selectors import s

from src.pages.DashboardPage import DashboardPage


class LoginPage:
    def __init__(self):
        self.username_input = s("#user_email")
        self.password_input = s("#user_password")
        self.agree_checkbox = s("#user_confirm_personal_data_processing")
        self.login_btn = s("#new_user > input.btn.btn-default.submit")

    def open(self):
        browser.open_url('/users/sign_in')
        return self

    def login_as(self, user):
        self.username_input.type(user.name)
        self.password_input.type(user.password)
        self.agree_checkbox.click()
        self.login_btn.click()
        return DashboardPage()
