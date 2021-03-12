# encoding: utf-8
# author: wm-chen
# login_case.py
# 2021/3/5 5:43 下午
# desc:登陆测试用例

from actions.login_action import LoginAction
import unittest
from common.base_selenium import BaseSelenium
from common.test_data_utils import TestData
from common.config_utils import local_config


class LoginCase(BaseSelenium):

    testdata = TestData(local_config.get_test_case_path, 'login_test').get_test_data()

    @unittest.skipUnless(testdata['test_login_success']['is_not'], '为否时不执行跳过')
    def test_login_success(self):
        test_data = self.testdata['test_login_success']
        self._testMethodDoc = test_data['test_name']
        login_action = LoginAction(self.base_page.driver)
        result = login_action.login_success(test_data['test_para']['username'], test_data['test_para']['password'])
        self.assertEqual(result, test_data['export'], '登陆断言失败')

    @unittest.skipUnless(testdata['test_login_fail']['is_not'], '为否时不执行跳过')
    def test_login_fail(self):
        test_data = self.testdata['test_login_fail']
        self._testMethodDoc = test_data['test_name']
        login_action = LoginAction(self.base_page.driver)
        result = login_action.login_fail(test_data['test_para']['username'], test_data['test_para']['password'])
        self.assertEqual(result, test_data['export'], '断言失败')


if __name__ == '__main__':
    unittest.main()