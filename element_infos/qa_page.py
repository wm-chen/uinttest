# encoding: utf-8
# author: wm-chen
# qa_page.py
# 2021/3/5 4:55 下午
# desc:测试界面

from common import base_page
from common.element_infos_utils import ElementInfos
from common.config_utils import local_config


class QaPage(base_page.BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        element_data = ElementInfos(local_config.get_element_path, 'qa_element').get_element_info()
        self.bug_button = element_data['bug_button']
        self.create_bug_button = element_data['create_bug_button']
        self.version_button = element_data['version_button']
        self.choose_version = element_data['choose_version']
        self.bug_title_inputbox = element_data['bug_title_inputbox']
        self.submit_button = element_data['submit_button']
        self.case_text = element_data['case_text']

    #跳转提交bug页面
    def bug_page(self):
        self.click(self.bug_button)

    def create_bug(self):
        self.click(self.create_bug_button)

    def click_version(self):
        self.click(self.version_button)

    def chooseversion(self, index):
        self.get_drop_down(self.choose_version, index)

    def bug_title(self, title):
        self.send(self.bug_title_inputbox, title)

    def submitbutton(self):
        self.scroll_bottom_page()
        self.click(self.submit_button)

    def first_case_text(self):
        return  self.get_text(self.case_text)

    def get_page_title(self):
        title = self.get_title()
        return title



