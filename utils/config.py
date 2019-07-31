#coding=utf8
import os
from utils.read_file import YamlReader

# 所有相关文件的路径

# 用os.path.split()和os.path.join()拼接路径，不要直接+'\\xxx\\ss'这样
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_FILE = os.path.join(BASE_PATH, 'config_file', 'config.yml')
DATA_PATH = os.path.join(BASE_PATH, 'data')
DRIVER_PATH = os.path.join(BASE_PATH, 'drivers')
LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'report')
XML_REPORT_PATH = os.path.join(REPORT_PATH, "xml_report")
HTML_REPORT_PATH = os.path.join(REPORT_PATH, "html_report")
TMS_TESTCASE_PATH = os.path.join(BASE_PATH, '/test_case/test_tms')
BPM_TESTCASE_PATH = os.path.join(BASE_PATH, '/test_case/test_bpm')
SCREENSHOT_PATH = os.path.join(BASE_PATH, 'screenshots')


class Config:
    def __init__(self, config_file=CONFIG_FILE):
        self.config = YamlReader(config_file).get_yaml_data

    def get(self, element, index=0):
        """
        yaml是可以通过'---'分节的。用YamlReader读取返回的是一个list，第一项是默认的节，如果有多个节，可以传入index来获取。
        这样我们其实可以把框架相关的配置放在默认节，其他的关于项目的配置放在其他节中。可以在框架中实现多个项目的测试。
        """
        return self.config[index][element]


if __name__ == '__main__':
    c = Config()
    s = c.get('log')
    print(s)
