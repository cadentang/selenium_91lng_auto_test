# -*- coding: utf-8 -*-
__author__ = 'caden'
"""
description:BPM-基础信息管理-客户管理-客户管理-新增，查看，搜索，编辑
"""
import allure
import time

from pages.bpm_pages import customer_manage_page
from common.common_login import common_bpm_login
from data.bpm_data import consumer_data as C
from data.bpm_data.login_data import add_base_login_data


@allure.feature("测试客户管理-新增")
class TestCustomerManageAdd:

    def setup_method(self):
        self.customer_page = customer_manage_page.CustomerManagePage(add_base_login_data["base_data"][3])
        common_bpm_login(add_base_login_data["base_data"][0], add_base_login_data["base_data"][1],
                         add_base_login_data["base_data"][2], self.customer_page.driver)
        self.customer_page.go_to_customer_manage_page()

    @allure.story("新增客户成功")
    @allure.title("新增客户只填写基础信息")
    def test_consumer_base_success(self):
        message = self.customer_page.add_consumer(C.consumer_data_base)
        print(message)
        # assert self.customer_page.driver.title == self.customer_page.consumer_list_title

    # @allure.story("新增客户成功")
    # @allure.title("新增客户只填写基础信息和业务信息")
    # def test_consumer_add_base_and_business_success(self):
    #     message = self.customer_page.add_consumer(C.consumer_data_base_and_business)
    #     assert self.customer_page.driver.title == self.customer_page.consumer_list_title
    #
    # @allure.story("新增客户成功")
    # @allure.title("新增客户时填写所有的信息")
    # def test_consumer_add_all_success(self):
    #     message = self.customer_page.add_consumer(C.consumer_data_all)
    #     assert self.customer_page.driver.title == self.customer_page.consumer_list_title
    #
    # @allure.story("新增客户失败")
    # @allure.title("新增客户时填写的客户名称重复")
    # def test_consumer_add_repeat_fail(self):
    #     message = self.customer_page.add_consumer(C.consumer_data_all)
    #     assert not message
    #     assert self.customer_page.driver.title == self.customer_page.consumer_add_title

    def teardown_method(self):
        time.sleep(10)
        self.customer_page.driver.close()

#
# @allure.feature("测试客户管理-编辑")
# class TestCustomerManageEdit:
#
#     def setup_method(self):
#         self.customer_page = customer_manage_page.CustomerManagePage(add_base_login_data["base_data"][3])
#         common_bpm_login(add_base_login_data["base_data"][0], add_base_login_data["base_data"][1],
#                          add_base_login_data["base_data"][2], self.customer_page.driver)
#         self.customer_page.go_to_customer_manage_page()
#
#     @allure.story("测试客户管理-编辑-编辑成功")
#     @allure.title("测试客户管理-编辑-编辑客户业务信息成功")
#     def test_customer_edit_success(self, consumer_name):
#         self.customer_page.go_to_consumer_view(consumer_name)
#         self.customer_page.driver.find_element_by_xpath(self.customer_page.edit_business).click()
#         self.customer_page.driver.find_element_by_xpath(self.customer_page.free_hour).clear()
#         self.customer_page.driver.find_element_by_xpath(self.customer_page.free_hour).send_keys(C.consumer_data_edit_free_hour_success["free_hour"])
#         self.customer_page.driver.find_element_by_xpath(self.customer_page.save_and_exit).click()
#         assert self.customer_page.driver.title == self.customer_page.driver.consumer_list_title
#
#     @allure.story("测试客户管理-编辑-编辑失败")
#     @allure.title("测试客户管理-编辑-客户名称修改失败")
#     def test_customer_edit_fail(self, consumer_name):
#         self.customer_page.go_to_consumer_view(consumer_name)
#         self.customer_page.driver.find_element_by_xpath(self.customer_page.edit_base).click()
#         self.customer_page.driver.find_element_by_xpath(self.customer_page.customer_name).clear()
#         self.customer_page.driver.find_element_by_xpath(self.customer_page.customer_name).send_keys(C.consumer_data_edit_consumer_name_fail["customer_name"])
#         self.customer_page.driver.find_element_by_xpath(self.customer_page.save_and_exit).click()
#         assert self.customer_page.driver.title == self.customer_page.driver.add_and_edit_tille
#
#     def teardown_method(self):
#         self.driver.close()
#
#
# @allure.feature("测试客户管理-搜索")
# class TestCustomerManageSearch:
#
#     def setup_method(self):
#         self.customer_page = customer_manage_page.CustomerManagePage(add_base_login_data["base_data"][3])
#         common_bpm_login(add_base_login_data["base_data"][0], add_base_login_data["base_data"][1],
#                          add_base_login_data["base_data"][2], self.customer_page.driver)
#         self.go_to_customer_manage_page()
#
#     @allure.story("测试客户管理-搜索-搜索成功")
#     @allure.title("测试客户管理-搜索-按客户名称搜索成功")
#     def test_customer_search_consumer_name_success(self):
#         self.customer_page.list_search(consumer=C.consumer_search_data["name"])
#         assert_text = self.customer_page.driver.find_element_by_xpath(self.customer_page.list_consumer_name_text).text
#         assert assert_text == C.consumer_search_data["name"]
#
#     @allure.story("测试客户管理-搜索-搜索成功")
#     @allure.title("测试客户管理-搜索-按客户简称搜索成功")
#     def test_customer_search_consumer_short_name_success(self):
#         self.customer_page.list_search(consumer=C.consumer_search_data["short_name"], search_type="客户简称")
#         assert_text = self.customer_page.driver.find_element_by_xpath(self.customer_page.list_consumer_short_name_text).text
#         assert assert_text == C.consumer_search_data["short_name"]
#
#     @allure.story("测试客户管理-搜索-搜索成功")
#     @allure.title("测试客户管理-搜索-按客户联系电话搜索成功")
#     def test_customer_search_consumer_name_success(self):
#         self.customer_page.list_search(consumer=C.consumer_search_data["name"], search_type="联系电话")
#         assert_text = self.customer_page.driver.find_element_by_xpath(self.customer_page.list_contract_phone_text).text
#         assert assert_text == C.consumer_search_data["name"]
#
#     @allure.story("测试客户管理-搜索-搜索成功")
#     @allure.title("测试客户管理-搜索-按客户分属业务员搜索成功")
#     def test_customer_search_consumer_name_success(self):
#         self.customer_page.list_search(consumer=C.consumer_search_data["name"], search_type="分属业务员")
#         assert_text = self.customer_page.driver.find_element_by_xpath(self.customer_page.list_sale_man_text).text
#         assert assert_text == C.consumer_search_data["name"]
#
#     @allure.story("测试客户管理-搜索-搜索失败")
#     @allure.title("测试客户管理-搜索-客户名称搜索无数据")
#     def test_customer_search_consumer_name_no_data(self):
#         self.customer_page.driver.find_element_by_xpath(self.customer_page.select_input).send_keys(C.consumer_search_data["no_data"])
#         self.customer_page.driver.find_element_by_xpath(self.customer_page.select_button).click()
#         assert_text = self.customer_page.driver.find_element_by_xpath(self.customer_page.list_no_data).text
#         assert assert_text == "暂无数据"
#
#     def teardown_method(self):
#         self.driver.close()


