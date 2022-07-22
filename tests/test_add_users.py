import os
from src.domain.user import User
from src.pages.LoginPage import LoginPage


def test_admin_can_add_user():
    admin = User(os.environ.get("admin_username"), os.environ.get("admin_password"))
    (LoginPage()
     .open()
     .login_as(admin)
     .goto_users_page()
     .add_user_btn
     .click())
