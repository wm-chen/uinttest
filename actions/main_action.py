# encoding: utf-8
# author: wm-chen
# main_action.py
# 2021/3/6 1:25 下午
# desc:
from element_infos.login_page import LoginPage
from element_infos.main_page import MainPage
from element_infos.qa_page import QaPage


class MainAction():

    def __init__(self, driver):
        self.main_page = MainPage(driver)

    def quit(self):
        self.main_page.out()
        #页面链接
        return LoginPage(self.main_page.driver)

    def qa(self):
        self.main_page.click_qa()
        return QaPage(self.main_page.driver)

    def my(self):
        self.main_page.click_my()

    def product(self):
        self.main_page.click_product()

    def project(self):
        self.main_page.click_project()

    def report(self):
        self.main_page.click_report()

    def company(self):
        self.main_page.click_company()

    def admin(self):
        self.main_page.click_admin()

    def doc(self):
        self.main_page.click_doc()

    def search_bug(self, index, text):
        self.main_page.click_search()
        self.main_page.select_search_type(index)
        self.main_page.input_search(text)
        self.main_page.click_go()
