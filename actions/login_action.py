# encoding: utf-8
# author: wm-chen
# login_action.py
# 2021/3/5 5:18 下午
# desc:
from element_infos.login_page import LoginPage
from element_infos.main_page import MainPage
from common.config_utils import local_config


class LoginAction():

    def __init__(self, driver):
        self.login = LoginPage(driver)

    def login_first(self, username, password):
        self.login.input_username(username)
        self.login.input_password(password)
        self.login.click_login()

    def login_success(self, username, password):
        self.login_first(username, password)
        return MainPage(self.login.driver).get_user_menu()

    def login_fail(self, uesrname, password):
        self.login_first(uesrname, password)
        return self.login.alter_text()

    def login_success_default(self):
        self.login_success(local_config.get_username, local_config.get_password)
        return MainPage(self.login.driver)