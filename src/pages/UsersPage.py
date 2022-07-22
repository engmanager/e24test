from selene.support import by
from selene.support.jquery_style_selectors import s
from selene import browser


class UsersPage:
    def __init__(self):
        self.add_user_btn = s(by.xpath('//a[@href="/users/new"]'))
        self.users_search_input = s(by.xpath('//input[@type="search"]'))

    def open(self):
        browser.open_url("/users")
        return self
