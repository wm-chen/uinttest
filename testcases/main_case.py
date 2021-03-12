# encoding: utf-8
# author: wm-chen
# main_case.py
# 2021/3/10 11:08 上午
# desc:测试各个页面之间的跳转
import unittest

from actions.main_action import MainAction
from common.base_page import BasePage
from common.base_selenium import BaseSelenium
from common.config_utils import local_config
from common.test_data_utils import TestData
from actions.login_action import LoginAction


class MainCase(BaseSelenium):

    testdata = TestData(local_config.get_test_case_path, 'main_test').get_test_data()

    @unittest.skipUnless(testdata['test_qa_page']['is_not'], '为否时不执行跳过')
    def test_qa_page(self):
        test_data = self.testdata['test_qa_page']
        self._testMethodDoc = test_data['test_name']
        login_action = LoginAction(self.base_page.driver).login_success_default()
        MainAction(login_action.driver).qa()
        self.assertEqual(self.base_page.get_title(), test_data['export'], '跳转测试页面失败')

    @unittest.skipUnless(testdata['test_my_page']['is_not'], '为否时不执行跳过')
    def test_my_page(self):
        test_data = self.testdata['test_my_page']
        self._testMethodDoc = test_data['test_name']
        login_action = LoginAction(self.base_page.driver).login_success_default()
        MainAction(login_action.driver).my()
        self.assertEqual(self.base_page.get_title(), test_data['export'], '跳转我的地盘页面失败')

    @unittest.skipUnless(testdata['test_product_page']['is_not'], '为否时不执行跳过')
    def test_product_page(self):
        test_data = self.testdata['test_product_page']
        self._testMethodDoc = test_data['test_name']
        login_action = LoginAction(self.base_page.driver).login_success_default()
        MainAction(login_action.driver).product()
        self.assertEqual(self.base_page.get_title(), test_data['export'], '跳转产品页面失败')

    @unittest.skipUnless(testdata['test_project_page']['is_not'], '为否时不执行跳过')
    def test_project_page(self):
        test_data = self.testdata['test_project_page']
        self._testMethodDoc = test_data['test_name']
        login_action = LoginAction(self.base_page.driver).login_success_default()
        MainAction(login_action.driver).project()
        self.assertEqual(self.base_page.get_title(), test_data['export'], '跳转项目页面失败')

    @unittest.skipUnless(testdata['test_doc_page']['is_not'], '为否时不执行跳过')
    def test_doc_page(self):
        test_data = self.testdata['test_doc_page']
        self._testMethodDoc = test_data['test_name']
        login_action = LoginAction(self.base_page.driver).login_success_default()
        MainAction(login_action.driver).doc()
        self.assertEqual(self.base_page.get_title(), test_data['export'], '跳转文档页面失败')

    @unittest.skipUnless(testdata['test_report_page']['is_not'], '为否时不执行跳过')
    def test_report_page(self):
        test_data = self.testdata['test_report_page']
        self._testMethodDoc = test_data['test_name']
        login_action = LoginAction(self.base_page.driver).login_success_default()
        MainAction(login_action.driver).report()
        self.assertEqual(self.base_page.get_title(), test_data['export'], '跳转统计页面失败')

    @unittest.skipUnless(testdata['test_company_page']['is_not'], '为否时不执行跳过')
    def test_company_page(self):
        test_data = self.testdata['test_company_page']
        self._testMethodDoc = test_data['test_name']
        login_action = LoginAction(self.base_page.driver).login_success_default()
        MainAction(login_action.driver).company()
        self.assertEqual(self.base_page.get_title(), test_data['export'], '跳转组织页面失败')

    @unittest.skipUnless(testdata['test_admin_page']['is_not'], '为否时不执行跳过')
    def test_admin_page(self):
        test_data = self.testdata['test_admin_page']
        self._testMethodDoc = test_data['test_name']
        login_action = LoginAction(self.base_page.driver).login_success_default()
        MainAction(login_action.driver).admin()
        self.assertEqual(self.base_page.get_title(), test_data['export'], '跳转后台页面失败')

    @unittest.skipUnless(testdata['test_search_bug']['is_not'], '为否时不执行跳过')
    def test_search_bug(self):
        test_data = self.testdata['test_search_bug']
        self._testMethodDoc = test_data['test_name']
        login_action = LoginAction(self.base_page.driver).login_success_default()
        MainAction(login_action.driver).search_bug(test_data['test_para']['index'], test_data['test_para']['text'])
        #断言test_data['export']包含在base_page.get_title()中则通过
        self.assertIn(test_data['export'], self.base_page.get_title(), '提交bug失败')


if __name__ == '__main__':
    unittest.main