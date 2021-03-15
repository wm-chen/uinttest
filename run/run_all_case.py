# encoding: utf-8
# author: wm-chen
# run_all_case.py
# 2021/3/5 3:10 下午
# desc:执行测试用例

from common import HTMLTestReportCN
from common.config_utils import local_config
import os
import unittest
from common.send_email_utils import SendEmail

current_path = os.path.abspath(os.path.dirname(__file__))
case_path = os.path.join(current_path, '..', local_config.get_case_path)
report_path = os.path.join(current_path, '..', local_config.get_report_path)\



class RunAllCases():

    def __init__(self):
        self.test_case_path = case_path
        self.report_path = report_path
        self.title = '自动化测试报告'
        self.description = '练习'

    def run(self):
        discover = unittest.defaultTestLoader.discover(
            start_dir=self.test_case_path, pattern='qa_case.py', top_level_dir=self.test_case_path)
        all_suite = unittest.TestSuite()
        all_suite.addTest(discover)
        report_dir = HTMLTestReportCN.ReportDirectory(self.report_path)
        report_dir.create_dir(self.title)
        dir_path = HTMLTestReportCN.GlobalMsg.get_value('dir_path')
        report_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
        fp = open(report_path, 'wb')
        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                                 title=self.title,
                                                 description=self.description,
                                                 tester='CWM')
        runner.run(all_suite)
        fp.close()
        return dir_path

    def run_and_send_zip_email(self, subject, body):
        report_path = self.run()
        SendEmail(subject, body, report_path).send_zip_email()


if __name__ == '__main__':
    path = RunAllCases().run_and_send_zip_email('测试', '测试')