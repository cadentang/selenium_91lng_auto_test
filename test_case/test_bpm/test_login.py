# -*- coding: utf-8 -*-
__author__ = 'caden'
"""
description:登录测试
"""
import allure
import pytest

from pages.bpm_pages import login_page
from pages.bpm_pages.bpm_base_page import BpmBasePage
from data.bpm_data.login_data import test_login_data


@allure.feature("测试登录")
class TestLogin:

    def setup_method(self):
        self.d = login_page.LoginPage("http://bpm.hhtdlng.com/#/login")

    @allure.story("测试登录成功")
    @allure.title("测试手机号码登录成功")
    def test_login_success(self):
        self.d.driver.find_element_by_xpath(self.d.go_to_username_xpath).send_keys(test_login_data["success_data"][0])
        self.d.driver.find_element_by_xpath(self.d.go_to_password_xpath).send_keys(test_login_data["success_data"][1])
        self.d.driver.find_element_by_xpath(self.d.go_to_mark_xpath).send_keys(test_login_data["success_data"][2])
        self.d.driver.find_element_by_xpath(self.d.go_to_login_xpath).click()
        is_exist = self.d.check_btn(BpmBasePage.username_xpath)
        assert is_exist

    @allure.story("测试登录失败")
    @allure.title("测试手机号码错误登录失败")
    @allure.description("这里是对test_0用例的一些详细说明")
    @allure.description_html("提供一些HTML在测试用例的描述部分(待研究)")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step('这里是操作步骤打印：name: "{0}", age: "{age}"')
    def test_login_failed_phone_error(self):
        self.d.driver.find_element_by_xpath(self.d.go_to_username_xpath).send_keys(test_login_data["fail_data_phone_error"][0])
        self.d.driver.find_element_by_xpath(self.d.go_to_password_xpath).send_keys(test_login_data["fail_data_phone_error"][1])
        self.d.driver.find_element_by_xpath(self.d.go_to_mark_xpath).send_keys(test_login_data["fail_data_phone_error"][2])
        self.d.driver.find_element_by_xpath(self.d.go_to_login_xpath).click()
        is_exist = self.d.check_btn(BpmBasePage.username_xpath)
        assert not is_exist

    @allure.story("测试登录失败")
    @allure.title("测试密码错误登录失败")
    def test_login_failed_password_error(self):
        self.d.driver.find_element_by_xpath(self.d.go_to_username_xpath).send_keys(test_login_data["fail_data_password_error"][0])
        self.d.driver.find_element_by_xpath(self.d.go_to_password_xpath).send_keys(test_login_data["fail_data_password_error"][1])
        self.d.driver.find_element_by_xpath(self.d.go_to_mark_xpath).send_keys(test_login_data["fail_data_password_error"][2])
        self.d.driver.find_element_by_xpath(self.d.go_to_login_xpath).click()
        is_exist = self.d.check_btn(BpmBasePage.username_xpath)
        assert not is_exist

    @allure.story("测试登录失败")
    @allure.title("测试验证码错误登录失败")
    def test_login_failed_code_error(self, phone, password, mark_code):
        self.d.driver.find_element_by_xpath(self.d.go_to_username_xpath).send_keys(test_login_data["fail_data_verification_error"][0])
        self.d.driver.find_element_by_xpath(self.d.go_to_password_xpath).send_keys(test_login_data["fail_data_verification_error"][1])
        self.d.driver.find_element_by_xpath(self.d.go_to_mark_xpath).send_keys(test_login_data["fail_data_verification_error"][2])
        self.d.driver.find_element_by_xpath(self.d.go_to_login_xpath).click()
        is_exist = self.d.check_btn(BpmBasePage.username_xpath)
        assert not is_exist

    def teardown_method(self):
        self.d.driver.close()



