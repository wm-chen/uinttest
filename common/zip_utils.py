# encoding: utf-8
# author: wm-chen
# zip_utils.py
# 2021/3/12 5:46 下午
# desc:

import zipfile


class ZipUtils():

    def __init__(self):
        self.filename = '/Users/weimaochen/PycharmProjects/uinttest/zip/test1.zip'

    def zip_utils(self):
        f = zipfile.ZipFile(self.filename, 'w', zipfile.ZIP_DEFLATED)
        f.write('/Users/weimaochen/PycharmProjects/uinttest/report/自动化测试报告V1.5/自动化测试报告V1.5.html')
        f.write('/Users/weimaochen/PycharmProjects/uinttest/report/自动化测试报告V1.5/image/1.png')
        f.close()

ZipUtils().zip_utils()