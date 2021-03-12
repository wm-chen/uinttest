# encoding: utf-8
# author: wm-chen
# qa_action.py
# 2021/3/5 5:18 下午
# desc:
from element_infos.qa_page import QaPage


class QaAction():

    def __init__(self, driver):
        self.qa_page = QaPage(driver)

    def submit_bug(self, title, index):
        self.qa_page.bug_page()
        self.qa_page.create_bug()
        self.qa_page.click_version()
        self.qa_page.chooseversion(index)
        self.qa_page.bug_title(title)
        self.qa_page.submitbutton()
        return self.qa_page.first_case_text()