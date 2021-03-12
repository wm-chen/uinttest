# encoding: utf-8
# author: wm-chen
# main_page.py
# 2021/3/6 12:37 下午
# desc:
from common import base_page
from common.element_infos_utils import ElementInfos
from common.config_utils import local_config


class MainPage(base_page.BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        element_data = ElementInfos(local_config.get_element_path, 'main_element').get_element_info()
        self.qa_button = element_data['qa_button']
        self.my_button = element_data['my_button']
        self.out_button = element_data['out_button']
        self.user_menu_button = element_data['user_menu']
        self.product_button = element_data['product_button']
        self.project_button = element_data['project_button']
        self.doc_button = element_data['doc_button']
        self.report_button = element_data['report_button']
        self.company_button = element_data['company_button']
        self.admin_button = element_data['admin_button']
        self.search_inputbox = element_data['search_inputbox']
        self.go_button = element_data['go_button']
        self.search_button = element_data['search_button']
        self.search_type = element_data['search_type']

    def out(self):
        self.click(self.out_button)

    def click_qa(self):
        self.click(self.qa_button)

    def user_menu(self):
        self.click(self.user_menu_button)

    def get_user_menu(self):
        return self.get_text(self.user_menu_button)

    def click_my(self):
        self.click(self.my_button)

    def click_product(self):
        self.click(self.product_button)

    def click_project(self):
        self.click(self.project_button)

    def click_doc(self):
        self.click(self.doc_button)

    def click_report(self):
        self.click(self.report_button)

    def click_company(self):
        self.click(self.company_button)

    def click_admin(self):
        self.click(self.admin_button)

    def click_search(self):
        self.click(self.search_button)

    def select_search_type(self, index):
        self.get_drop_down(self.search_type, index)

    def input_search(self, text):
        self.send(self.search_inputbox, text)

    def click_go(self):
        self.click(self.go_button)
