# coding=utf8
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from pages.bpm_pages.login_page import LoginPage


class BpmBasePage(LoginPage):

    go_to_index_xpath = "//*[@id='app']/div/header/div/a/div"  # 进入引导页面
    go_to_message_center_xpath = "//*[@id='app']/div/header/div/div/div/div[2]/div/span[1]/span/div/i"  # 进入消息中心
    go_to_personal_center_xpath = "//*[@id='app']/div/header/div/div/div/div[2]/div/div/span"  # 进入个人中心

    # 左边菜单栏
    # #一级菜单
    overview_xpath = '//*[@id="app"]/section/aside/ul/li[1]'  # 概览
    order_management_xpath = '//*[@id="app"]/section/aside/ul/li[2]'  # 订单管理
    logistics_management_xpath = '//*[@id="app"]/section/aside/ul/li[3]'  # 物流管理
    map_xpath = '//*[@id="app"]/section/aside/ul/li[4]'  # 地图
    base_message_management_xpath = '//*[@id="app"]/section/aside/ul/li[5]'  # 基础信息管理
    data_statistics_xpath = '//*[@id="app"]/section/aside/ul/li[6]'  # 数据统计
    arap_xpath = '//*[@id="app"]/section/aside/ul/li[7]'  # 应收应付
    setting_xpath = '//*[@id="app"]/section/aside/ul/li[8]'  # 设置

    # #二级菜单
    business_overview_xpath = '//*[@id="app"]/section/aside/ul/li[1]/ul/li[1]'  # 概览->业务概览
    car_overview_xpath = '//*[@id="app"]/section/aside/ul/li[1]/ul/li[2]'  # 概览->车辆调度概览
    sale_overview_xpath = '//*[@id="app"]/section/aside/ul/li[1]/ul/li[3]'  # 概览->销售统计概览
    procurement_overview_xpath = '//*[@id="app"]/section/aside/ul/li[1]/ul/li[4]'  # 概览->采购统计概览

    pickup_orders_xpath = '//*[@id="app"]/section/aside/ul/li[2]/ul/li[1]'  # 订单管理->托运订单
    outside_pick_xpath = '//*[@id="app"]/section/aside/ul/li[2]/ul/li[2]'  # 订单管理->外销订单
    outside_buy_xpath = '//*[@id="app"]/section/aside/ul/li[2]/ul/li[3]'  # 订单管理->外采订单
    sales_order_xpath = '//*[@id="app"]/section/aside/ul/li[2]/ul/li[4]'  # 订单管理->销售订单

    platform_order_xpath = '//*[@id="app"]/section/aside/ul/li[3]/ul/li'  # 物流管理->平台运单

    car_monitor_xpath = '//*[@id="app"]/section/aside/ul/li[4]/ul/li[1]'  # 地图->车辆监控
    landmark_xpath = '//*[@id="app"]/section/aside/ul/li[4]/ul/li[2]'  # 地图->地标及路线

    customer_manage_xpath = '//*[@id="app"]/section/aside/ul/li[5]/ul/li[1]'  # 基础信息管理->贸易客户管理
    supplier_manage_xpath = '//*[@id="app"]/section/aside/ul/li[5]/ul/li[2]'  # 基础信息管理->供应商管理
    purchase_price_manage_xpath = '//*[@id="app"]/section/aside/ul/li[5]/ul/li[3]'  # 基础信息管理->采购价管理
    carrier_manage_xpath = '//*[@id="app"]/section/aside/ul/li[5]/ul/li[4]'  # 基础信息管理->承运商管理
    standard_data_manage_xpath = '//*[@id="app"]/section/aside/ul/li[5]/ul/li[5]'  # 基础信息管理->标准数据设置

    purchase_xpath = '//*[@id="app"]/section/aside/ul/li[6]/ul/li[1]'  # 数据统计->采购数据
    sale_xpath = '//*[@id="app"]/section/aside/ul/li[6]/ul/li[2]'  # 数据统计->销售数据
    consignment_xpath = '//*[@id="app"]/section/aside/ul/li[6]/ul/li[3]'  # 数据统计->托运数据
    income_xpath = '//*[@id="app"]/section/aside/ul/li[6]/ul/li[4]'  # 数据统计->业务台账

    supplier_meet_manage_xpath = '//*[@id="app"]/section/aside/ul/li[7]/ul/li[1]'  # 应收应付->供应商应付
    payer_manage_xpath = '//*[@id="app"]/section/aside/ul/li[7]/ul/li[2]'  # 应收应付->付款方应收
    carrier_meet_manage_xpath = '//*[@id="app"]/section/aside/ul/li[7]/ul/li[3]'  # 应收应付->承运方应付

    personal_settings_xpath = '//*[@id="app"]/section/aside/ul/li[8]/ul/li[1]'  # 设置->个人设置
    organizational_structure_xpath = '//*[@id="app"]/section/aside/ul/li[8]/ul/li[2]'  # 设置->组织架构
    staffs_manage_xpath = '//*[@id="app"]/section/aside/ul/li[8]/ul/li[3]'  # 设置->员工管理
    power_manage_xpath = '//*[@id="app"]/section/aside/ul/li[8]/ul/li[4]'  # 设置->权限管理

    pack_up_xpath = '//*[@id="app"]/section/aside/div/div'  # 收起/打开菜单栏
    mybread1_xpath = '//*[@id="mybread"]/span[1]/span'  # 面包屑，第一个导航栏元素
    mybread2_xpath = '//*[@id="mybread"]/span[2]/span'  # 面包屑，第二个导航栏元素
    mybread3_xpath = '//*[@id="mybread"]/span[3]/span'  # 面包屑，第三个导航栏元素
    mybread4_xpath = '//*[@id="mybread"]/span[4]/span'  # 面包屑，第四个导航栏元素

    username_xpath = '//*[@id="app"]/div/header/div/div/div/div[2]/div/div'  # 登录的个人信息
    # 下拉选择框定位，定位到具体的某一个选项
    # select_input_xpath = '//div[@class="el-select-dropdown el-popper"]//ul[@class="el-scrollbar__view el-select-dropdown__list"]/li/span'
    # select_input_xpath1 = '/html/body/div[@class="el-select-dropdown el-popper"]/div[1]/div[1]/ul/li/span'
    select_input_xpath1 = '/html/body/div[@class="el-select-dropdown el-popper"]/div[1]/div[1]/ul/li/span'
    select_input_xpath2 = '/html/body/div[3]/div[1]/div[1]/ul/li/span'
    select_input_xpath3 = '/html/body/div[4]/div[1]/div[1]/ul/li/span'

    # select_input_xpath1 = '/html/body/div[4]/div[1]/div[1]/ul/li/span'
    # select_input_xpath2 = '/html/body/div[3]/div[1]/div[1]/ul/li/span'
    # select_input_xpath3 = '/html/body/div[2]/div[1]/div[1]/ul/li/span'

    # 判断二级菜单是否打开
    def is_opened(self, ele):
        class_ = self.driver.find_element_by_xpath(ele).get_attribute("class")
        if "menu-title el-submenu is-opened" == class_:
            return True
        else:
            return False

    def is_now_page(self, global_text):
        """判断当前页面是不是二级菜单打开的页面"""
        now_text = self.driver.find_element_by_xpath(self.mybread3_xpath).text
        judge = True if now_text == global_text else False
        return judge

    def pack_up_menu(self):
        """收起/展开菜单栏"""
        self.driver.find_element_by_xpath(self.pack_up_xpath)

    def go_to_business_overview_page(self):
        """进入业务概览页面"""
        self.driver.find_element_by_xpath(self.overview_xpath).click()
        self.driver.find_element_by_xpath(self.business_overview_xpath).click()

    def go_to_car_overview_page(self):
        """进入车辆调度概览页面"""
        self.driver.find_element_by_xpath(self.overview_xpath).click()
        self.driver.find_element_by_xpath(self.car_overview_xpath).click()

    def go_to_sale_overview_page(self):
        """进入销售统计概览页面"""
        self.driver.find_element_by_xpath(self.overview_xpath).click()
        self.driver.find_element_by_xpath(self.sale_overview_xpath).click()

    def go_to_procurement_overview_page(self):
        """进入采购统计概览页面"""
        self.driver.find_element_by_xpath(self.overview_xpath).click()
        self.driver.find_element_by_xpath(self.procurement_overview_xpath).click()

    def go_to_pickup_orders_page(self):
        """进入托运订单管理页面"""
        self.driver.find_element_by_xpath(self.order_management_xpath).click()
        self.driver.find_element_by_xpath(self.pickup_orders_xpath).click()

    def go_to_outside_pick_page(self):
        """进入外销订单管理页面"""
        self.driver.find_element_by_xpath(self.order_management_xpath).click()
        self.driver.find_element_by_xpath(self.outside_pick_xpath).click()

    def go_to_outside_buy_page(self):
        """进入外采订单管理页面"""
        self.driver.find_element_by_xpath(self.order_management_xpath).click()
        self.driver.find_element_by_xpath(self.outside_buy_xpath).click()

    def go_to_sales_order_page(self):
        """进入销售订单管理页面"""
        self.driver.find_element_by_xpath(self.order_management_xpath).click()
        self.driver.find_element_by_xpath(self.sales_order_xpath).click()

    def go_to_platform_order_page(self):
        """进入平台运单页面"""
        self.driver.find_element_by_xpath(self.logistics_management_xpath).click()
        self.driver.find_element_by_xpath(self.platform_order_xpath).click()

    def go_to_car_monitor_page(self):
        """进入车辆监控页面"""
        self.driver.find_element_by_xpath(self.map_xpath).click()
        self.driver.find_element_by_xpath(self.car_monitor_xpath).click()

    def go_to_landmark_page(self):
        """进入地标页面"""
        self.driver.find_element_by_xpath(self.map_xpath).click()
        self.driver.find_element_by_xpath(self.landmark_xpath).click()

    def go_to_customer_manage_page(self):
        """进入客户管理页面"""
        self.driver.find_element_by_xpath(self.base_message_management_xpath).click()
        self.driver.find_element_by_xpath(self.customer_manage_xpath).click()

    def go_to_supplier_manage_page(self):
        """进入供应商管理页面"""
        self.driver.find_element_by_xpath(self.base_message_management_xpath).click()
        self.driver.find_element_by_xpath(self.supplier_manage_xpath).click()

    def go_to_purchase_price_manage_page(self):
        """进入采购价管理页面"""
        self.driver.find_element_by_xpath(self.base_message_management_xpath).click()
        self.driver.find_element_by_xpath(self.purchase_price_manage_xpath).click()

    def go_to_carrier_manage_page(self):
        """进入承运商管理页面"""
        self.driver.find_element_by_xpath(self.base_message_management_xpath).click()
        self.driver.find_element_by_xpath(self.carrier_manage_xpath).click()

    def go_to_standard_data_manage_page(self):
        """进入标准数据设置页面"""
        self.driver.find_element_by_xpath(self.base_message_management_xpath).click()
        self.driver.find_element_by_xpath(self.standard_data_manage_xpath).click()

    def go_to_purchase_page(self):
        """进入采购数据页面"""
        self.driver.find_element_by_xpath(self.data_statistics_xpath).click()
        self.driver.find_element_by_xpath(self.purchase_xpath).click()

    def go_to_sale_page(self):
        """进入销售数据页面"""
        self.driver.find_element_by_xpath(self.data_statistics_xpath).click()
        self.driver.find_element_by_xpath(self.sale_xpath).click()

    def go_to_consignment_page(self):
        """进入托运数据页面"""
        self.driver.find_element_by_xpath(self.data_statistics_xpath).click()
        self.driver.find_element_by_xpath(self.consignment_xpath).click()

    def go_to_income_page(self):
        """进入业务台账页面"""
        self.driver.find_element_by_xpath(self.data_statistics_xpath).click()
        self.driver.find_element_by_xpath(self.income_xpath).click()

    def go_to_supplier_meet_manage_page(self):
        """进入供应商应付页面"""
        self.driver.find_element_by_xpath(self.arap_xpath).click()
        self.driver.find_element_by_xpath(self.supplier_meet_manage_xpath).click()

    def go_to_payer_manage_page(self):
        """进入付款方应收页面"""
        self.driver.find_element_by_xpath(self.arap_xpath).click()
        self.driver.find_element_by_xpath(self.payer_manage_xpath).click()

    def go_to_carrier_meet_manage_page(self):
        """进入承运商应付页面"""
        self.driver.find_element_by_xpath(self.arap_xpath).click()
        self.driver.find_element_by_xpath(self.carrier_meet_manage_xpath).click()

    def go_to_personal_settings_page(self):
        """进入个人设置页面"""
        self.driver.find_element_by_xpath(self.setting_xpath).click()
        self.driver.find_element_by_xpath(self.personal_settings_xpath).click()

    def go_to_organizational_structure_page(self):
        """进入组织架构页面"""
        self.driver.find_element_by_xpath(self.setting_xpath).click()
        self.driver.find_element_by_xpath(self.organizational_structure_xpath).click()

    def go_to_staffs_manage_page(self):
        """进入员工管理页面"""
        self.driver.find_element_by_xpath(self.setting_xpath).click()
        self.driver.find_element_by_xpath(self.staffs_manage_xpath).click()

    def go_to_power_manage_page(self):
        """进入权限管理页面"""
        self.driver.find_element_by_xpath(self.setting_xpath).click()
        self.driver.find_element_by_xpath(self.power_manage_xpath).click()

    @staticmethod
    def select_input_function(path, next_path, value, driver):
        """
        下拉框输入封装方法
        :param path:输入框的定位
        :param select_input_xpath: 下拉框元素值为value的定位
        :param value:下拉框中输入的值
        :param driver: 当前driver
        :return:
        """
        driver.find_element_by_xpath(path).click()
        # print(driver.find_element_by_xpath('/html/body/div[2]').get_attribute('style'))
        # print(next_path)
        # if driver.find_element_by_xpath(path).get_attribute('class') == 'el-input el-input--suffix is-focus':
        # print(driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[1]/span'))
        eles = driver.find_elements_by_xpath(next_path)
        for i in eles:
            if i.text == value:
                i.click()
                break
