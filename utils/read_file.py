#coding=utf8
import yaml
import os
from xlrd import open_workbook


class YamlReader:
    """yaml文件的读取, get_yaml_data返回一条list"""
    def __init__(self, yamlFilePath):
        if os.path.exists(yamlFilePath):
            self.yamlFilePath = yamlFilePath
        else:
            raise FileNotFoundError('文件不存在！')
        self._data = None

    @property
    def get_yaml_data(self):
        if not self._data:
            with open(self.yamlFilePath, 'rb') as f:
                self._data = list(yaml.safe_load_all(f))
        return self._data


class SheetTypeError(Exception):
    pass


class ExcelReader:
    """读取excel文件内容
        如果 print(ExcelReader(excel, title_line=True).data)，输出结果：
        [{A: A1, B: B1, C:C1}, {A:A2, B:B2, C:C2}]
        如果 print(ExcelReader(excel, title_line=False).data)，输出结果：
        [[A,B,C], [A1,B1,C1], [A2,B2,C2]]
    """
    def __init__(self, excelFilePath, sheet=0, title_line=True):
        if os.path.exists(excelFilePath):
            self.excelFilePath = excelFilePath
        else:
            raise FileNotFoundError("文件不存在！")
        self.sheet = sheet
        self.title_line = title_line
        self._data = list()

    @property
    def get_excel_data(self):
        workbook = open_workbook(self.excelFilePath)

        if type(self.sheet) not in [int, str]:
            raise SheetTypeError('please pass in <int> or <str>, not {0}'.format(type(self.sheet)))
        elif type(self.sheet) == int:
            s = workbook.sheet_by_index(self.sheet)
        else:
            s = workbook.sheet_by_name(self.sheet)

        if self.title_line:
            title = s.row_values(0)
            for col in range(1, s.nrows):
                # 依次遍历其余行，与首行组成dict，拼到self._data中
                self._data.append(dict(zip(title, s.row_values(col))))
        else:
            for col in range(0, s.nrows):
                # 遍历所有行，拼到self._data中
                self._data.append(s.row_values(col))
        return self._data


if __name__ == "__main__":
    yam = YamlReader("D:\my-git-project\91lng\selenium_91lng_auto_test\config_file\config.yml")
    data = yam.get_yaml_data
    print(data)