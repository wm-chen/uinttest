# encoding: utf-8
# author: wm-chen
# read_excel.py
# 2021/3/5 2:14 下午
# desc:去读excel文件，生成列表

import xlrd
import os

element_excle_path = os.path.dirname(__file__)+'/../element_infos_datas/element_infos.xlsx'
test_data_path = os.path.dirname(__file__)+'/../test_datas/test_datas.xlsx'


class ReadExcel(object):

    #定义参数，excel_path, sheet_name
    def __init__(self, excel_path, sheet_name):
        #excel_path，打开对应excel的路径
        self.workbook = xlrd.open_workbook(excel_path)
        #sheet_name，打开excel对应的表名
        self.sheet = self.workbook.sheet_by_name(sheet_name)

    #获取excel的行数
    def get_nrow(self):
        nrow = self.sheet.nrows
        return nrow

    #返回excel的烈数
    def get_ncol(self):
        ncol = self.sheet.ncols
        return ncol

    #循环将excle的数据添加到get_excel_datas的列表中
    def get_excel_data(self):
        get_excel_datas = []
        for i in range(1, self.get_nrow()):
            get_excel_data = []
            for j in range(self.get_ncol()):
                #读取excel第i行，第j列的单元格数据
                data = self.sheet.cell_value(i, j)
                get_excel_data.append(data)
            get_excel_datas.append(get_excel_data)
        return get_excel_datas


if __name__ == '__main__':
    element_data = ReadExcel(element_excle_path, 'login_element').get_excel_data()
    #test_data = ReadExcel(test_data_path, 'login_test').get_excel_data()

    print(element_data)
