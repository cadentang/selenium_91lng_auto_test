# -*- coding: utf-8 -*-
__author__ = 'caden'
"""
description:
"""
import xlrd
import xlwt
from datetime import timedelta

# 读取Excel文件
def read_excel(file_path):
    workbook = xlrd.open_workbook(file_path)
    sheets = workbook.sheet_names()
    print(sheets[0])
    work_sheet = workbook.sheet_by_name(sheets[0])
    for i in range(0, work_sheet.nrows):
        for j in range(0, work_sheet.ncols):
            print(work_sheet.cell_value(i, j), "\t", end="")


def write_excel_xls(path, sheet_name, value):
    index = len(value)
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet(sheet_name)
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])
    workbook.save(path)
    print("xls格式表格写入数据成功！")


def write_excel_xls_append(path, value):
    index = len(value)
    workbook = xlrd.open_workbook(path)
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])
    rows_old = worksheet.nrows
    new_workbook = copy(workbook)
    new_worksheet = new_workbook.get_sheet(0)
    for i in range(0, index):
        for j in range(0, len(value[i])):
            new_worksheet.write(i + rows_old, j, value[i][j])
    new_workbook.save(path)


def read_excels(file_excel):#读excel并将需要的数据分类放在数组里
    infos=[]
    info_file=xlrd.open_workbook(file_excel)
    info_sheet=info_file.sheets()[0]
    row_count=info_sheet.nrows
    for row in range(1,row_count):
        time_string=info_sheet.cell(row,3).value
        time_s_sp=time_string.split(':')
        infos.append(
            {
                'type':info_sheet.cell(row,2).value,
                'other_cellphone':info_sheet.cell(row,0).value,
                'timespan':timedelta(seconds=int(time_s_sp[2]),minutes=int(time_s_sp[1]),hours=int(time_s_sp[0])),
                'gpscity':info_sheet.cell(row,5).value

            }
        )
    return infos

def count_cell(list_dirs,infotype):#统计总通话及分类统计结果，存在字典里
    result_dir={}
    time_all=timedelta(seconds=0)
    for list_dir in list_dirs:
        time_all +=list_dir['timespan']
        info_type = list_dir[infotype]
        if info_type not in result_dir:
            result_dir[info_type]=list_dir['timespan']
        else:
            result_dir[info_type]+=list_dir['timespan']
    return time_all,result_dir
def print_result(result_dir):#打印数据
    for k,v in result_dir.items():
        print k.encode('utf-8'),v

if __name__ == "__main__":
    read_excel("5.xlsx")



