# coding=utf-8
import pytest
import sys
import time

from utils.run_cmd import RunCmd
from utils.config import Config, CONFIG_FILE
from utils.log import logger
from utils.config import XML_REPORT_PATH, HTML_REPORT_PATH


class RunTestCase:
    """测试执行类"""
    def __init__(self, type_, cmd_type, ):
        pass

    def get_test_suit(self):
        pass

    def run_test(self):
        pass


if __name__ == "__main__":

    """
        1.全部用例执行
        2.指定某个目录下运行
        3.指定具体的py文件运行
        4.指定某个py文件某个类运行
        5.指定某个py文件某个类下的方法运行
        6.指定优先级运行
        allure
        pytest -q 静默模式，只输出异常case
        pytest -v 详细，显示明细及case结果标志灯
        pytest casefile.py	指定case文件执行
        pytest casedir	指定路径运行
        pytest casedir/casefile::caseclass::casefunc	运行具体的case方法、类等
        pytest --pyargs pkgname	指定包执行，根据系统文件路径定位case，后期可以用pip安装包的方法部署执行case
        pytest -k "key_words_1 and not key_words_1"	执行符合key_words_1命名规则的文件、类及方法，忽略key_words_2命名规则的文件、类及方法
        pytest -m "mark_name"	需要在指定case方法上添加@pytest.mark.mark_name来指定方法属于哪个mark
        pytest --junitxml=file.xml 生成xml报告，方便对执行结果进一步分析，后期可以通过xmltodict库转成json格式分析入库及自定义报告
        pytest --html=./report.html 生成html格式报告，需要提前安装pytest-html模块，个人测试时发现生成的html报告没有teardown里面的内容，控制台却是有teardown里的内容输出的，这算是个小bug？
        退出代码0成功地收集并传递了所有测试
        退出代码1测试被收集和运行, 但一些测试失败
        退出代码2测试执行被用户中断
        退出代码3执行测试时发生内部错误
        退出代码 4 pytest 命令行使用错误
        退出代码5未收集任何测试
        
        https://www.cnblogs.com/zztxiaodeng/p/10656582.html
        --allure-features  指定features执行
        --allure-story 指定story执行
        pytest test_1.py --allure-stories "这里是第二个二级标签", "这里是第三个二级标签"
        
    """
    # args = ['-s', '-q', '--alluredir', XML_REPORT_PATH]
    # print(XML_REPORT_PATH)
    # path = XML_REPORT_PATH + '/report.xml'
    # pytest.main(["-s", "-q", "../test_case/", '--alluredir', path])
    # conf = Config()
    # print(conf.config)

    xml_report_path = XML_REPORT_PATH
    html_report_path = HTML_REPORT_PATH
    logger.info("初始化配置文件，文件路径=" + CONFIG_FILE)

    # 定义测试集, 通过allure.feature控制测试用例集, 读取yaml中的配置文件
    # allure_list = '--allure_features=Home,Personal'

    test_case_path = "../test_case/test_bpm/test_customer_manage.py"
    args_v = ['-s', '-q', '--alluredir', xml_report_path, test_case_path]
    # logger.info('执行用例集为：%s' % allure_list)
    pytest.main(args_v)
    time.sleep(10)

    # 使用allure将xml报告生成为html报告
    cmd = 'allure generate %s -o %s' % (xml_report_path, html_report_path)
    try:
        RunCmd().running_cmd(cmd)
    except Exception:
        logger.info("报告转换失败")
        raise








