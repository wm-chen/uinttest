# encoding: utf-8
# author: wm-chen
# test_data_utils.py
# 2021/3/5 2:32 下午
# desc:读取测试数据
from common.read_excel import ReadExcel
from common.config_utils import local_config


class TestData(object):

    def __init__(self, excel_path, sheet_name):
        self.test_data = ReadExcel(excel_path, sheet_name).get_excel_data()

    def get_test_data(self):
        get_test_datas ={}
        for i in range(len(self.test_data)):
            get_test_data = {}
            get_test_data['test_name'] = self.test_data[i][1]
            get_test_data['test_class'] = self.test_data[i][2]
            get_test_data['is_not'] = True if self.test_data[i][3].__eq__('是') else False
            get_test_data['export'] = self.test_data[i][4]
            parameter = {}
            for j in range(5, len(self.test_data[i])):
                if self.test_data[i][j].__contains__('=') and len(self.test_data[i][j]) > 2:
                    parameter_info = self.test_data[i][j].split('=')
                    parameter[parameter_info[0]] = parameter_info[1]
                get_test_data['test_para'] = parameter
            get_test_datas[self.test_data[i][0]] = get_test_data
        return get_test_datas


if __name__ == '__main__':
    tt = TestData(local_config.get_test_case_path, 'qa_test').get_test_data()
    print(type(tt['test_submit_bug']['test_para']['version']))
