import xlrd
import os

excle_path = os.path.dirname(__file__)+'/../element_infos_datas/element_infos.xlsx'
workbook = xlrd.open_workbook(excle_path)
sheet = workbook.sheet_by_name('element_infos')
row_count = sheet.nrows
element_infos = {}
for i in range(1,row_count):
    element_info = {}
    element_info['element_name'] = sheet.cell_value(i, 1)
    element_info['locator_type'] = sheet.cell_value(i, 2)
    element_info['locator_value'] = sheet.cell_value(i, 3)
    element_infos[sheet.cell_value(i, 0)] = element_info
print(element_infos)
