import os
from selene import config
from selene.support.conditions import have, be

from src.domain.user import User
from src.pages.LoginPage import LoginPage

config.browser_name = "chrome"


def test_admin_can_login():
    admin = User(os.environ.get("admin_username"), os.environ.get("admin_password"))
    (LoginPage()
     .open()
     .login_as(admin)
     .message_after_login.should(be.existing))
