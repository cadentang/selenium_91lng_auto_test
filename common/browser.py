# -*- coding: utf-8 -*-
__author__ = 'caden'

import time
import os
from selenium import webdriver
from utils.config import DRIVER_PATH, REPORT_PATH, SCREENSHOT_PATH
from utils.log import logger

CHROME_DRIVER_PATH = DRIVER_PATH + '\chromedriver.exe'
IEDRIVER_PATH = DRIVER_PATH + '\IEDriverServer.exe'
PHANTOMJSDRIVER_PATH = DRIVER_PATH + '\phantomjs.exe'
FIREFOX_PATH = DRIVER_PATH + '\geckodriver.exe'


class UnSupportBrowserTypeError(Exception):
    pass


class Browser(object):
    """浏览器启动初始化"""
    def __init__(self, url, maximize_window=True, implicitly_wait=30, browser_type="chrome"):
        if browser_type == "chrome":
            self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        elif browser_type == "firefox":
            self.driver = webdriver.Firefox(executable_path=FIREFOX_PATH)
        elif browser_type == "ie":
            self.driver = webdriver.Ie(executable_path=IEDRIVER_PATH)
        elif browser_type == "phantomjs":
            self.driver = webdriver.PhantomJS(executable_path=PHANTOMJSDRIVER_PATH)
        else:
            logger.info("不支持该浏览器!")

        self.driver.get(url)

        if maximize_window:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)

    def save_screen_shot(self, name='screen_shot'):
        day = time.strftime('%Y%m%d', time.localtime(time.time()))
        screenshot_path = SCREENSHOT_PATH + '\screenshot_%s' % day
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)

        tm = time.strftime('%H%M%S', time.localtime(time.time()))
        screenshot = self.driver.save_screenshot(screenshot_path + '\\%s_%s.png' % (name, tm))
        return screenshot

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    b = Browser(url="https://www.baidu.com/")
    b.save_screen_shot('test_baidu')
    time.sleep(3)
    b.quit()
