#coding=utf8
import time
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

from .browser import Browser
from utils.log import logger


class BasePage(Browser):

    # 获取当前窗口句柄
    @property
    def current_window(self):
        return self.driver.current_window.handle

    # 获取网页标题
    @property
    def get_title(self):
        return self.driver.title

    # 获取当前网址
    @property
    def get_current_url(self):
        return self.driver.current_url

    # 获取浏览器的驱动
    def get_driver(self):
        return self.driver

    # 睡眠一段时间
    def wait(self, seconds=3):
        time.sleep(seconds)

    # 执行js脚本
    def execute_js(self, js, *args):
        self.driver.execute_script(js, *args)

    # 移动到指定的元素
    def move_to(self, element):
        ActionChains(self.driver).move_to_element(element).perform()

    # 寻找指定的元素
    def find_element(self, *args):
        self.driver.find_element(*args)

    # 滑动滚动条（上）
    def scroll_up(self):
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    # 滑动滚动条（下）
    def scroll_down(self):
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

    # 左滑
    def scroll_left(self):
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    # 右滑
    def scroll_right(self):
        js = "window.scrollTo(document.body.scrollWidth,0)"
        self.driver.execute_script(js)

    # 元素聚焦
    def element_target(self, ele):
        target = self.driver.find_element_by_xpath(ele)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    # 寻找一组指定的元素
    def find_elements(self, *args):
        self.driver.find_elements(*args)

    # 切换窗口
    def switch_to_window(self, partial_url='', partial_title=''):
        all_windows = self.driver.window_handles
        if len(all_windows) == 1:
            logger.warning('只有一个窗口，无法进行切换！')
        elif len(all_windows) == 2:
            other_window = all_windows[1 - all_windows.index(self.current_window)]
            self.driver.switch_to.window(other_window)
        else:
            for window in all_windows:
                self.driver.switch_to.window(window)
                if partial_url in self.driver.current_url or partial_title in self.driver.title:
                    break
        logger.debug(self.driver.current_url, self.driver.title)

    # 切换frame页面
    def switch_to_frame(self, params):
        self.driver.switch_to.frame(params)

    # 切换alter
    def switch_to_alter(self):
        self.driver.switch_to.alter()

    # 截图

    # 鼠标拖动

    # 键盘输入

    # 上传文件
    def upload_file(self, file_path, *args):
        self.find_element(*args).send_keys(file_path)

    # 下载文件
    def download_file(self, file_path, *args, type):
        if type == "firefox":
            fp = webdriver.FirefoxProfile()
            fp.set_preference("browser.download.folderList", 2)
            fp.set_preference("browser.download.manager.showWhenStarting", False)
            fp.set_preference("browser.download.dir", os.getcwd())
            fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

            browser = webdriver.Firefox(firefox_profile=fp)
            browser.get("http://pypi.python.org/pypi/selenium")
            browser.find_element_by_partial_link_text("selenium-2").click()

    def check_btn(self, elem):
        """检查元素是否存在"""
        logger.info('====check_elem: %s is exists?====' % elem)
        try:
            element = self.driver.find_element_by_xpath(elem)
        except NoSuchElementException:
            logger.info('====no %s====' % elem)
            return False
        else:
            # cancelBtn.click()
            logger.info('====element %s exist====' % elem)
            return True

    def get_time(self):
        """获取当前时间"""
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def get_screens_hot(self, module):
        """截图操作"""
        time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png' % (module, time)
        logger.info('%s 截图' % module)
        self.driver.get_screenshot_as_file(image_file)
