# encoding: utf-8
# author: wm-chen
# qa_case.py
# 2021/3/5 10:31 下午
# desc:
import os
import unittest

from actions.main_action import MainAction
from actions.qa_action import QaAction
from actions.login_action import LoginAction
from common.base_selenium import BaseSelenium
from common.test_data_utils import TestData
from common.config_utils import local_config


class QaCase(BaseSelenium):

    testdata = TestData(local_config.get_test_case_path, 'qa_test').get_test_data()

    @unittest.skipUnless(testdata['test_submit_bug']['is_not'], '为否时不执行')
    def test_submit_bug(self):
        bug = self.testdata['test_submit_bug']
        self._testMethodDoc = bug['test_name']
        login_action = LoginAction(self.base_page.driver)
        mainpage = login_action.login_success_default()
        mainaction = MainAction(mainpage.driver)
        qapage = mainaction.qa()
        qaction = QaAction(qapage.driver)
        result = qaction.submit_bug(bug['test_para']['title'], bug['test_para']['version'])
        self.assertEqual(result, bug['export'], '提交bug断言失败')


if __name__ == '__main__':
    unittest.main()
