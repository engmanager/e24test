from selene.support import by
from selene.support.jquery_style_selectors import s

from src.pages.UsersPage import UsersPage


class DashboardPage:
    def __init__(self):
        self.message_after_login = s(by.text("Ви успішно ввійшли у систему"))
        self.users_link = s(by.xpath('//a[@href="/users"]'))

    def goto_users_page(self):
        self.users_link.click()
        return UsersPage()
