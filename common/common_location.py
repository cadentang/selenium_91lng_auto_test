# -*- coding: utf-8 -*-
__author__ = 'caden'
"""
description:定位元素的通用方法,https://www.cnblogs.com/dwdw/p/9998660.html
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

from utils.log import logger


class CommonLocation:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = TIME_OUT
        self.t = T

    def find_element(self, locator, value=''):
        """
        定位单个元素
        :param locator: 定位元素的方式和值，类型为元组，如：("id", "value1")
        :param value: 默认为空，如果传值则通过文本定位
        :return: 返回元素定位的对象
        """
        if not isinstance(locator, tuple):
            logger.info('locator参数类型错误，必须传元组类型：locator = ("id", "value1")')
        else:
            logger.info("正在定位元素信息：定位方式->{locator[0]}, 元素值->{locator[1]}，value值->{value}")
            if value != '':
                element = WebDriverWait(self.driver, self.timeout, self.t).\
                    until(EC.text_to_be_present_in_element_value(locator, value))
                return element
            else:
                element = WebDriverWait(self.driver, self.timeout, self.t).\
                    until(EC.presence_of_element_located(locator))
                if element:
                    return element
                else:
                    logger.info("定位失败：定位方式=>{locator[0]}, value值=>{locator[1]}")
                    return False

    def find_elements(self, locator, value=''):
        """
        定位一组元素
        :param locator: 定位元素的方式和值，类型为元组，如：("id", "value1")
        :param value: 默认为空，如果传值则通过文本定位
        :return: 返回元素对象列表
        """
        if not isinstance(locator, tuple):
            logger.info('locator参数类型错误，必须传元组类型：locator = ("id", "value1")')
        else:
            logger.info("正在定位一组元素信息：定位方式->{locator[0]}, 元素值->{locator[1]}，value值->{value}")
            if value != '':
                elements = WebDriverWait(self.driver, self.timeout, self.t).\
                    until(EC.text_to_be_present_in_element_value(locator, value))
                return elements
            else:
                elements = WebDriverWait(self.driver, self.timeout, self.t).\
                    until(EC.presence_of_element_located(locator))
                if elements:
                    return elements
                else:
                    logger.info("定位失败：定位方式=>{locator[0]}, value值=>{locator[1]}")
                    return False

    def send_key(self, locator, text):
        """向标签中输入值"""
        try:
            self.clear(locator)
            self.find_element(locator).send_keys(text)
        except Exception as e:
            logger.info(f"输入值{text}失败, 报错信息{str(e)}")

    def clear(self, locator):
        try:
            self.find_element(locator).clear()
        except Exception as e:
            logger.info(f"清理标签{locator}失败, 报错信息{str(e)}")

    def is_selected(self, locator, type_=''):
        """判断元素是否被选中，返回bool值 及点（选中/取消选中"""
        ele = self.find_element(locator)
        try:
            if type_ == '':  # 如果type参数为空，返回元素是否为选中状态，True/False (默认)
                r = ele.is_selected()
                return r
            elif type_ == 'click':  # 如果type参数为click，执行元素的点击操作
                ele.click()
            else:
                print(f"type参数 {type_} 错误，仅可为click或''")
        except Exception as e:
            logger.info("元素定位错误，错误信息：%s" % str(e))
            return False

    def is_element_dom_exist(self, locator):
        """
        判断单个元素是否在DOM里面,不一定显示
        :param locator:
        :return:
        """
        try:
            self.find_element(locator)
            return True
        except Exception as e:
            logger.info("元素定位错误，错误信息：%s" % str(e))
            return False

    def is_element_dom_exists(self, locator):
        """
        判断一组元素是否在DOM里面,不一定显示，若不存在，返回一个空的list
        :param locator: 定位元素的方式和值，类型为元组，如：("id", "value1")
        :return:
        """
        ''' 判断一组元素是否在DOM里面 （是否存在），若不存在，返回一个空的list'''
        element = self.find_elements(locator)
        n = len(element)
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            logger.info(f"定位到元素的个数：{n}")
            return True

    def title(self, title):
        """
        获取当前页面的title
        :param title:
        :return:
        """
        try:
            result1 = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(title))
            if result1:
                return result1
            else:
                result2 = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(title))
                if result2:
                    return result2
                else:
                    return False
        except Exception as e:
            logger.info("获取title失败，失败信息：%s" % str(e))
            return False

    def in_element_exist(self, locator, value, type_='text'):
        """
        根据传入的type判断内容是否在指定元素里面
        :param locator:
        :param value:
        :param type_:
        :return:
        """
        if not isinstance(locator, tuple):
            logger.info("locator参数类型错误，必须传元祖类型")
        try:
            if type_ == 'text':
                result = WebDriverWait(self.driver, self.timeout, self.t).until(
                    EC.text_to_be_present_in_element(locator, value))
                return result
            elif type_ == 'value':
                result = self.find_element(locator, value)
                return result
            else:
                print(f"type参数 {type_} 错误，仅可使用text或value属性定位")
                return False
        except Exception as e:
            logger.info("获取title失败，失败信息：%s" % str(e))
            return False

    def alert(self, timeout=3, type_=''):
        """
        对常规警告窗的操作,确定，取消
        :param timeout:
        :param type_:
        :return:
        """
        result = WebDriverWait(self.driver, timeout, self.t).until(EC.alert_is_present())
        try:
            if type_ == '':
                if result:
                    return result
                else:
                    logger.info("alert不存在")
                return False
            elif type_ == 'yes':
                result.accept()
            elif type_ == 'no':
                result.dismiss()
            else:
                logger.info(f"type_参数类型 错误，仅可为yes、no、或''")
        except Exception as e:
            logger.info("发生异常，异常信息：%s" % str(e))
            return False

    def get_title_text_attribute(self, locator=None, _type='text', name=''):
        """
        根据_type类型获取元素指定的内容
        :param locator:元素的定位
        :param _type:获取内容的方式（title，text，attribute）
        :param name:元素属性名称
        :return:
        """
        try:
            if _type == 'title':
                return self.driver.title
            elif _type == 'text':
                return self.find_element(locator).text
            elif _type == 'attribute':  # 获取当前元素属性
                return self.find_element(locator).get_attribute(name)
            else:
                logger.info("_type参数传值错误，类型仅可用title、text、attribute三种类型")
        except Exception as e:
            logger.info("发生异常，获取类容失败,异常信息：%s" % str(e))
            return ''

    def select(self, locator, value, _type='index'):
        """
        根据传值_type获取下拉框的内容
        :param locator:元素定位
        :param value:值
        :param _type:类型
        :return:
        """
        element = self.find_element(locator)
        try:
            if Type == 'index':  # 用下标选择 （默认）
                Select(element).select_by_index(value)
            elif Type == 'value':  # 根据value值选择
                Select(element).select_by_value(value)
            elif Type == 'text':  # 根据选项的文本内容选择
                Select(element).select_by_visible_text(value)
            else:
                print(f"给的type参数 {Type} 错误，仅可为：int、text、value")
        except:
            print(f"根据 {value} 操作下拉框失败")

    def switch_iframe(self, iframe):
        """
        切换iframe
        :param iframe: 如果传入的是数字，则以该数字为下标取值，如果传入的是字符串，
                        则用iframe名字取值，如果是元祖，则根据传入的locator取值
        :return:
        """
        try:
            if isinstance(iframe, int):
                self.driver.switch_to.frame(iframe)
            elif isinstance(iframe, str):
                self.driver.switch_to.frame(iframe)
            elif isinstance(iframe, tuple):
                ele = self.find_element(iframe)
                self.driver.switch_to.frame(ele)
        except Exception as e:
            logger.info("iframe切换异常,异常信息：%s" % str(e))

    def move_to_element(self, locator):
        """
        鼠标悬停操作
        :param locator:
        :return:
        """
        try:
            ele = self.find_element(locator)
            ActionChains(self.driver).move_to_element(ele).perform()
        except Exception as e:
            logger.info("鼠标悬停操作失败,异常信息:%s" % str(e))
            return False

    def js_focus_element(self, locator):
        """
        聚焦元素
        :param locator:
        :return:
        """
        target = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        """
        滚动条滚到顶部
        :return:
        """
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self, x=0):
        """
        滚动条滚到底部某个位置
        :param x:
        :return:
        """
        js = f"window.scrollTo({x},document.body.scrollHeight)"
        self.driver.execute_script(js)

    def js_find(self, action):
        """
        js查找单个元素
        :param action:
        :return:
        """
        js = f"document.getElementById(“id”).{action}"
        self.driver.execute_script(js)

    def js_finds(self, _type, element, index, action):
        '''   js查找元素，并做相应操作   输入值：value='XXX'     点击：click()
        js定位仅可为：id、Name、TagName、ClassName、Selector（CSS） '''
        list = ['Name', 'TagName', 'ClassName', 'Selector']
        if type in list:
            print(f"正在执行js操作：定位方式->{_type}, 元素值->{element}， 下标值->{index}， 执行操作->{action}")
            if type == 'Selector':
                js = f'document.query{_type}All("{element}"){index}.{action}'
            else:
                js = f'document.getElementsBy{_type}({element})[{index}].{action};'
            self.driver.execute_script(js)
        else:
            print(f"type参数 {_type} 错误，js定位仅可为：'Name'、'TagName'、'ClassName'、'Selector'（CSS）")

    def js_readonly(self, idElement, value):
        ''' 去掉只读属性，并输入内容 一般为id '''
        js = f'document.getElementById({idElement}).removeAttribute("readonly");document.getElementById({idElement}).value="{value}"'
        driver.execute_script(js)

    def js_iframe(self, Type, element, action, index=''):
        '''  Js处理iframe   无需先切换到iframe上，再切回来操作
        输入值：value=''         点击：click()           type=id时，index=''  '''
        js = f'document.getElementBy{Type}({element}){index}.contentWindow.document.body.{action}'
        driver.execute_script(js)

    '''
        jquery = '$(CSS).val("XXX");'   # 根据css语法定位到元素，输入内容
        jquery = '$(CSS).val('');'      # 清空
        jquery = '$(CSS).click();'      # 点击
        driver.execute_script(jquery)
    '''

    def get_title(self):
        """
        获取当前页面的title
        :return:
        """
        return self.driver.title

    def get_text(self, locator):
        """
        获取某个元素的文本
        :param locator:
        :return:
        """
        try:
            t = self.find_element(locator).text
            return t
        except Exception as e:
            logger.info("获取text失败，返回'',错误信息：%s" % str(e))
            return ""

    def get_attribute(self, locator, name):
        """
        获取元素的属性
        :param locator: 定位方式元组
        :param name: 属性名称
        :return:
        """
        try:
            element = self.find_element(locator)
            return element.get_attribute(name)
        except Exception as e:
            logger.info("获取%s属性失败，返回'',错误信息:%s" % (name, str(e)))
            return ""

    def select_by_index(self, locator, index=0):
        """
        下拉选择框通过索引选择元素
        :param locator: 定位的下拉框
        :param index: 索引
        :return:
        """
        element = self.find_element(locator)
        Select(element).select_by_index(index)

    def select_by_value(self, locator, value):
        """
        下拉框通过值选择元素
        :param locator: 定位的下拉框
        :param value: 值
        :return:
        """
        element = self.find_element(locator)
        Select(element).select_by_value(value)

    def select_by_text(self, locator, text):
        """
        下拉框通过文本选择元素
        :param locator:定位的下拉框
        :param text:文本
        :return:
        """
        element = self.find_element(locator)
        Select(element).select_by_visible_text(text)

    def current_window(self):
        """获取当前窗口的句柄"""
        return self.driver.current_window.handle

    def handle(self, value):
        """
        根据传入的参数类型自动判断切换窗口
        :param value:参数类型为int/str，int：根据下标切换对应的窗口，str：根据名称切换窗口
        :return:
        """
        try:
            if isinstance(value, int):
                handles = self.driver.window_handles
                self.driver.switch_to.window(handles[value])
            elif isinstance(value, str):
                self.driver.switch_to.window(value)
            else:
                logger.info("传入的type参数 %s 错误，仅可传int、str" % type(value))
        except Exception as e:
            logger.info("切换句柄失败，错误信息：%s" % str(e))

    # def js_find(self, action):
    #     '''
    #     输入值：value='XXX'     点击：click()
    #     '''
    #     print("正在执行js操作，操作行为：%s"%action)
    #     js = "document.getElementById(“id”).%s"%action
    #     self.driver.execute_script(js)


