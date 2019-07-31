# coding=utf8
import time
from selenium.webdriver.common.by import By

from pages.bpm_pages.bpm_base_page import BpmBasePage
from utils.log import logger


class CustomerManagePage(BpmBasePage):
    consumer_manage = '//*[@id="tab-customerManage"]'  # 客户管理tab
    consumer_station = '//*[@id="tab-stationManage"]'  # 客户站点tab
    payer_manage = '//*[@id="tab-customerPayManage"]'  # 客户付款方管理tab
    station_list = '//*[@id="tab-statationList"]'  # 站点列表
    station_map = '//*[@id="tab-statationMap"]' # 站点地图

    consumer_list_title = "客户管理列表"
    station_list_title = "站点列表"
    station_map_title = "站点地图"
    payer_list_title = "付款方列表"
    consumer_detail_title = "客户管理详情"
    consumer_add_title = "客户管理新增编辑"
    add_and_edit_tille = "编辑、新增站点"

    # 客户管理列表页相关元素
    go_to_add = '//*[@id="app"]/section/main/div/div/div/div/div/div/div[2]/button'  # 新增客户
    select_way = '//*[@id="pane-customerManage"]/div/form/div/div[1]/div/div[1]/div/div/input'  # 选择查询方式
    select_input = '//*[@id="pane-customerManage"]/div/form/div/div[1]/div/input'  # 搜索输入框
    select_button = '//*[@id="pane-customerManage"]/div/form/div/div[1]/div/div[2]'  # 搜索按钮
    consumer_status = '//*[@id="pane-customerManage"]/div/form/div/div[2]/div/div/div/div[1]/input'  # 客户状态搜索
    view_consumer = '//*[@id="app"]/section/main/div/div/div/div/div/div/div[3]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[12]/div/button'  # 查看某一条客户信息
    view_consumer_by_css = 'view_consumer'  # 获取一页中所有的tr
    list_no_data = '//*[@id="app"]/section/main/div/div/div/div/div/div/div[3]/div[1]/div[3]/div/span'  # 无数据
    list_consumer = '//*[@id="app"]/section/main/div/div/div/div/div/div/div[3]/div[1]/div[3]/table/tbody/tr/td[1]/div'  # 客户名称

    # 添加客户相关页面元素
    customer_name = '//*[@id="addeditTailCarPage"]//form/div[1]/div[1]/div/div/div[1]/input'  # 客户名称
    short_customer_name = '//*[@id="addeditTailCarPage"]//form/div[1]/div[2]/div/div/div/input'  # 客户简称
    customer_grade = '//*[@id="addeditTailCarPage"]//form/div[1]/div[3]/div/div/div/div[1]'  # 客户等级
    contact_person = '//*[@id="addeditTailCarPage"]//form/div[2]/div[1]/div/div/div/input'  # 联系人
    contact_phone = '//*[@id="addeditTailCarPage"]//form/div[2]/div[2]/div/div/div/input'  # 联系电话
    sale_man_name = '//*[@id="addeditTailCarPage"]/section/main/div/form/div[2]/div[3]/div/div[1]/div/div'  # 分属业务员
    social_credit_code = '//*[@id="addeditTailCarPage"]//form/div[2]/div[4]/div/div/div/input'  # 社会统一信用代码
    consumer_address = '//*[@id="addeditTailCarPage"]//form/div[2]/div[5]/div/div/div/input'  # 地址
    should_pay_money = '//*[@id="addeditTailCarPage"]//form/div[2]/div[6]/div/div/div/input'  # 信用额度
    payer_owner = '//*[@id="addeditTailCarPage"]//form/div[2]/div[7]/div/div/div/div[1]/div/label[1]'  # 设为付款方按钮
    payer_three = '//*[@id="addeditTailCarPage"]//form/div[2]/div[7]/div/div/div/div[1]/div/label[2]'  # 选择现有付款方
    payer_select = '//*[@id="addeditTailCarPage"]//div[2]/div[7]/div/div/div/div[2]/div/div[2]/input'  # 选择现有付款方下拉框
    consumer_category_display = '//*[@id="addeditTailCarPage"]//form/div[2]/div[8]/div/div/div/div'  # 客户类别
    free_hour = '//*[@id="addeditTailCarPage"]//form/div[1]/div[1]/div/div/div/input'  # 免费待时时长
    waiting_price = '//*[@id="addeditTailCarPage"]//form/div[1]/div[2]/div/div/div/input'  # 待时单价
    kui_tons_standard = '//*[@id="addeditTailCarPage"]/section/main/div[1]/form/div[1]/div[3]/div/div/div/input'  # 亏吨标准
    settlement_cycle_display = '//*[@id="addeditTailCarPage"]/section/main/div[1]/form/div[2]/div/div/div/div/div/input' # 结算方式
    contract_no = '//*[@id="addeditTailCarPage"]/section/main/div[1]/form/div[1]/div[1]/div/div/div/input'  # 合同编号
    contract_start_date = '//*[@id="addeditTailCarPage"]/section/main/div[1]/form/div[1]/div[2]/div/div/div/input'  # 合同起始日期
    contract_end_date = '//*[@id="addeditTailCarPage"]/section/main/div[1]/form/div[2]/div/div/div/div/input'  # 合同截止日期

    # 编辑客户页面元素
    edit_base = '//*[@id="addPerson"]/section/main/form/div[1]/div[1]/div/div[2]/button'  # 编辑基础信息
    edit_business = '//*[@id="addPerson"]/section/main/form/div[2]/div[1]/div/div[2]/button'  # 编辑业务信息
    edit_contract = '//*[@id="addPerson"]/section/main/form/div[3]/div[1]/div/div[2]/button'  # 编辑合同信息

    # 编辑，新增页面共同元素
    save_and_next = '//*[@id="addeditTailCarPage"]//button[1]'  # 保存并下一步
    save_and_exit = '//*[@id="addeditTailCarPage"]//button[2]'  # 保存并退出
    save_and_exit1 = '//*[@id="addeditTailCarPage"]/section/main/div[1]/div/div/div/button'  # 保存并推出，最后一页填写时用
    go_to_back = '//*[@id="addeditTailCarPage"]/section/header/div/div[1]/div'  # 返回列表页

    # 站点列表相关元素
    go_to_add_station = '//*[@id="pane-statationList"]/div/div[1]/button'  # 新增客户站点按钮
    station_select = '//*[@id="pane-statationList"]/div/form/div[1]/div/div/div[1]/div/div[1]/input'  # 选择站点搜索项目
    station_select_input = '//*[@id="pane-statationList"]/div/form/div[1]/div/div/input'  # 搜索输入框
    station_select_button = '//*[@id="pane-statationList"]/div/form/div[1]/div/div/div[2]'  # 搜索按钮
    station_consumer_name = '//*[@id="pane-statationList"]/div/form/div[2]/div[1]/div/div/div/div[1]/input'  # 客户名称搜索
    station_consumer_status = '//*[@id="pane-statationList"]/div/form/div[2]/div[2]/div/div/div/div[1]/input'  # 客户状态搜索
    station_edit_button = '//*[@id="pane-statationList"]/div/div[2]/div[1]/div[4]/div[2]/table/tbody/tr/td[12]/div/button'  #编辑按钮

    #列表里面相关元素定位
    list_consumer_name_text = '//*[@id="app"]/section/main/div/div/div/div/div/div/div[3]/div[1]/div[3]/table/tbody/tr/td[1]/div'  # 客户名称文本
    list_consumer_short_name_text = '//*[@id="app"]/section/main/div/div/div/div/div/div/div[3]/div[1]/div[3]/table/tbody/tr/td[2]/div'  # 客户简称文本
    list_contract_phone_text = '//*[@id="app"]/section/main/div/div/div/div/div/div/div[3]/div[1]/div[3]/table/tbody/tr/td[4]/div'  # 客户联系电话文本
    list_sale_man_text = '//*[@id="app"]/section/main/div/div/div/div/div/div/div[3]/div[1]/div[3]/table/tbody/tr/td[9]/div'  # 业务员文本

    # 新增客户站点页面元素
    select_search_input = '//*[@id="app"]/section/main/div/div/div/div/div/form/div/div[1]/div/div/div/div/input'  # 站点选择搜索选项
    add_station_search_input = '//*[@id="app"]/section/main/div/div/div/div/div/form/div/div[1]/div/input'  # 实际站点搜索输入框
    add_back = '//*[@id="app"]/section/main/div/div/div/div/div/header/div[1]/div[1]/a/div'  # 返回
    search_sheng = '//*[@id="app"]/section/main/div/div/div/div/div/form/div/div[2]/div/div/div/div/div[1]/div/div/input'  # 省
    search_shi = '//*[@id="app"]/section/main/div/div/div/div/div/form/div/div[2]/div/div/div/div/div[2]/div/div/input'  # 市
    search_qu = '//*[@id="app"]/section/main/div/div/div/div/div/form/div/div[2]/div/div/div/div/div[3]/div/div/input'  # 区
    add_station_search_button = '//*[@id="app"]/section/main/div/div/div/div/div/form/div/div[3]/div/div/button'  #搜索按钮
    station_name = '//*[@id="app"]/section/main/div/div/div/div/div/div[2]/form/div[1]/div/div/div/div/input'  # 站点名称
    station_icon = '//*[@id="map-container"]/div[1]/div/div[1]/div/div[1]'  # 搜索后站点的icon
    station_button = '//*[@id="choose-Actual-fluid"]'  # 设为客户站点
    station_type = '//*[@id="app"]/section/main/div/div/div/div/div/div[2]/form/div[3]/div/div/div/div/div[1]/input'  # 站点类型
    station_class = '//*[@id="app"]/section/main/div/div/div/div/div/div[2]/form/div[4]/div/div/div/div/div[1]/input'  # 站点类别
    station_consumer_short_name = '//*[@id="app"]/section/main/div/div/div/div/div/div[2]/form/div[5]/div/div/div/div/div[1]/input'  # 客户简称
    station_contract_name = '//*[@id="app"]/section/main/div/div/div/div/div/div[2]/form/div[6]/div/div/div/div/input'  # 联系人
    station_contract_phone = '//*[@id="app"]/section/main/div/div/div/div/div/div[2]/form/div[7]/div/div/div/div/input'  # 联系电话
    station_status = '//*[@id="app"]/section/main/div/div/div/div/div/div[2]/form/div[9]/div/div/div/div'  # 站点状态
    station_save_and_exit = '//*[@id="app"]/section/main/div/div/div/div/div/div[2]/div/button'  # 保存客户站点并退出
    station_pack_up = '//*[@id="app"]/section/main/div/div/div/div/div/div[3]'  # 收起站点栏

    # 站点地图页相关元素
    map_select_consumer = '//*[@id="pane-statationMap"]/div/div/form/div/div[1]/div/div/div/div/input'
    map_input_station_name = '//*[@id="pane-statationMap"]/div/div/form/div/div[2]/div/div/div/input'
    map_select_status = '//*[@id="pane-statationMap"]/div/div/form/div/div[3]/div/div/div/div[1]/input'
    map_select_button = '//*[@id="pane-statationMap"]/div/div/form/div/div[4]/button'

    def go_to_consumer_view(self, consumer_name):
        """
        进入一个客户的详情页
        :param consumer_name:
        :return:
        """
        self.driver.find_element_by_xpath(self.select_input).send_keys(consumer_name)
        self.driver.find_element_by_xpath(self.select_button).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.view_consumer).click()
        self.switch_to_window()
        if self.driver.title == self.consumer_detail_title:
            logger.info("进入客户%s详情页面成功!" % consumer_name)
            return True
        else:
            logger.info("进入客户%s详情页面失败!" % consumer_name)
            return False

    def add_consumer(self, input_dict):
        """
        新增客户的基本信息
        :param input_dict:是一个dict
        {
            "customer_name": "山东蓝水能源有限公司",
            "short_customer_name": "山东蓝水",
            "customer_grade": "一类客户",
            "contact_person": "唐半闲",
            "contact_phone": ""19800000000,
            "sale_man_name": "刘鹏",
            "social_credit_code": ""ABCDEFGHJK12345678,
            "consumer_address": "山东省济南市工业南路57号",
            "should_pay_money": "300000",
            "is_payer": 1, #  0,代表选择已有的付款方，1，代表将新加的客户作为付款方
            "payer_select": "陕西元和石油天然气有限公司"
            "consumer_category_display": "贸易商",
            "is_business_contract": 1,  # 0,代表不填写业务信息，1，代表将填写业务信息， 2，代表填写业务信息和合同信息
            "free_hour": "12",
            "waiting_price": "300",
            "kui_tons_standard": "200",
            "settlement_cycle_display": "周结",
            "contract_no": "NO22222",
            "contract_start_date": ""2019-03-19,
            "contract_end_date": "2019-10-19",
        }
        :return:
        """
        self.driver.find_element_by_xpath(self.go_to_add).click()
        time.sleep(2)
        # print(self.driver.title)
        if self.driver.title == self.consumer_add_title:
            logger.info("进入%s页面成功!" % self.consumer_add_title)
            self.driver.find_element_by_xpath(self.customer_name).send_keys(input_dict["customer_name"])
            self.driver.find_element_by_xpath(self.short_customer_name).send_keys(input_dict["short_customer_name"])
            self.select_input_function(self.customer_grade, self.select_input_xpath1,
                                       input_dict["customer_grade"], self.driver)
            time.sleep(1)
            self.driver.find_element_by_xpath(self.contact_person).send_keys(input_dict["contact_person"])
            self.driver.find_element_by_xpath(self.contact_phone).send_keys(input_dict["contact_phone"])
            self.select_input_function(self.sale_man_name, self.select_input_xpath2,
                                       input_dict["sale_man_name"], self.driver)
            time.sleep(1)
            self.driver.find_element_by_xpath(self.social_credit_code).send_keys(input_dict["social_credit_code"])
            self.driver.find_element_by_xpath(self.consumer_address).send_keys(input_dict["consumer_address"])
            self.driver.find_element_by_xpath(self.should_pay_money).send_keys(input_dict["should_pay_money"])

            if input_dict["is_payer"] == 0:
                self.driver.find_element_by_xpath(self.payer_three).click()
                self.driver.find_element_by_xpath((self.payer_select)).send_keys(input_dict["payer_select"])
            elif input_dict["is_payer"] == 1:
                self.driver.find_element_by_xpath(self.payer_owner).click()
            else:
                logger.info("is_payer参数不符合规范，必须是0,1")

            self.select_input_function(self.consumer_category_display, self.select_input_xpath3,
                                       input_dict["consumer_category_display"], self.driver)
            time.sleep(1)

            if input_dict["is_business_contract"] == 0:
                self.driver.find_element_by_xpath(self.save_and_exit).click()
                message = self.driver.switch_to_alert().text()
                return message
            elif input_dict["is_business_contract"] == 1:
                self.driver.find_element_by_xpath(self.save_and_next).click()
                self.driver.find_element_by_xpath(self.free_hour).send_keys(input_dict["free_hour"])
                self.driver.find_element_by_xpath(self.waiting_price).send_keys(input_dict["waiting_price"])
                self.driver.find_element_by_xpath(self.kui_tons_standard).send_keys(input_dict["kui_tons_standard"])
                self.driver.find_element_by_xpath(self.settlement_cycle_display).send_keys(input_dict["settlement_cycle_display"])
                message = self.driver.switch_to_alert().text()
                return message
            elif input_dict["is_business_contract"] == 2:
                self.driver.find_element_by_xpath(self.save_and_next).click()
                self.driver.find_element_by_xpath(self.free_hour).send_keys(input_dict["free_hour"])
                self.driver.find_element_by_xpath(self.waiting_price).send_keys(input_dict["waiting_price"])
                self.driver.find_element_by_xpath(self.kui_tons_standard).send_keys(input_dict["kui_tons_standard"])
                self.driver.find_element_by_xpath(self.settlement_cycle_display).\
                    send_keys(input_dict["settlement_cycle_display"])

                self.driver.find_element_by_xpath(self.save_and_next).click()
                self.driver.find_element_by_xpath(self.contract_no).send_keys(input_dict["contract_no"])
                self.driver.find_element_by_xpath(self.contract_start_date).send_keys(input_dict["contract_start_date"])
                self.driver.find_element_by_xpath(self.contract_end_date).send_keys(input_dict["contract_end_date"])

                self.driver.find_element_by_xpath(self.save_and_exit1).click()
                # 获取alter信息
                message = self.driver.switch_to_alert().text()
                return message
            else:
                logger.info("is_business_contract参数不符合规范，必须是0，1，2")
                return False
        else:
            logger.info("进入%s页面失败!" % self.consumer_add_title)
            return False

    def list_search(self, consumer, search_type="consumer_name"):
        """
        客户搜索功能
        :param consumer:
        :param search_type:
        :return:
        """
        if search_type == "consumer_name":
            self.driver.find_element_by_xpath(self.select_input).send_keys(consumer)
            self.driver.find_element_by_xpath(self.select_button).click()
        else:
            self.driver.find_element_by_xpath(self.select_way).clear()
            self.driver.find_element_by_xpath(self.select_way).send_keys(search_type)
            self.driver.find_element_by_xpath(self.select_input).send_keys(consumer)
            self.driver.find_element_by_xpath(self.select_button).click()

    def switch_to_consumer(self):
        """
        切换到客户管理页面
        :return:
        """
        if self.driver.title == self.consumer_list_title:
            logger.info("当前页面是在客户管理页面！")
            return True
        else:
            self.driver.find_element_by_xpath(self.consumer_manage).click()
            if self.driver.title == self.consumer_list_title:
                return True
            else:
                return False

    def switch_to_station_list(self):
        """
        切换到客户站点列表页
        :return:
        """
        if self.driver.title == self.station_list_title:
            logger.info("当前页面是在站点列表页面！")
            return True
        else:
            if self.driver.title == self.station_map_title:
                self.driver.find_element_by_xpath(self.station_list).click()
            else:
                self.driver.find_element_by_xpath(self.consumer_station).click()
            if self.driver.title == self.station_list_title:
                return True
            else:
                return False

    def switch_to_station_map(self):
        """
        切换到客户站点地图页
        :return:
        """
        if self.driver.title == self.station_map_title:
            logger.info("当前页面是在站点地图页面！")
            return True
        else:
            if self.driver.title == self.station_list_title:
                self.driver.find_element_by_xpath(self.station_map).click()
            else:
                self.driver.find_element_by_xpath(self.consumer_station).click()
                self.driver.find_element_by_xpath(self.station_map).click()
            if self.driver.title == self.station_map_title:
                return True
            else:
                return False

    def switch_to_payer(self):
        """
        切换到付款方列表页面
        :return:
        """
        if self.driver.title == self.payer_list_title:
            logger.info("当前页面是在%s页面！" % self.payer_list_title)
            return True
        else:
            self.driver.find_element_by_xpath(self.payer_manage).click()
            if self.driver.title == self.payer_list_title:
                logger.info("进入页面%s成功" % self.payer_list_title)
                return True
            else:
                logger.info("进入页面%s失败" % self.payer_list_title)
                return False

    def go_to_add_consumer_station(self):
        """
        进入客户站点新增页面
        :return:
        """
        self.driver.find_element_by_xpath(self.go_to_add_station).click()
        time.sleep(1)
        self.driver.switch_to_window()
        if self.driver.title == self.add_and_edit_tille:
            logger.info("进入新增页面成功!")
            return True
        else:
            logger.info("进入新增页面失败!")
            return False

    def go_to_edit_consumer_station(self, station_name):
        """
        进入客户站点编辑页面
        :return:
        """
        self.driver.find_element_by_xpath(self.station_select_input).send_keys(station_name)
        self.driver.find_element_by_xpath(self.station_select_button).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.station_edit_button).click()
        self.switch_to_window()
        if self.driver.title == self.add_and_edit_tille:
            logger.info("进入客户站点%s详情页面成功!" % station_name)
            return True
        else:
            logger.info("进入客户站点%s详情页面失败!" % station_name)
            return False

    def add_consumer_station(self, station_data):
        """
        station_data是一个dict
        {
            "actual_station_name": "",
            "station_name": "",
            "station_type":"",
            "station_class": "",
            "consumer_short_name": "",
            "consumer_contract_name": "",
            "consumer_contract_phone": "",
            "consumer_status": 0,  # 0默认为开启状态， 1代表关闭
        }
        :param station_data:
        :return:
        """
        self.driver.find_element_by_xpath(self.add_station_search_input).send_keys(station_data["actual_station_name"])
        self.driver.find_element_by_xpath(self.add_station_search_button).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.station_icon).click()
        self.driver.find_element_by_xpath(self.station_button).click()

        self.driver.find_element_by_xpath(self.station_name).send_keys(station_data["station_name"])
        self.driver.find_element_by_xpath(self.station_type).send_keys(station_data["station_type"])
        self.driver.find_element_by_xpath(self.station_consumer_short_name).send_keys(station_data["station_consumer_short_name"])

        # 向下滑动滚动条至底部
        self.scroll_down()
        self.driver.find_element_by_xpath(self.station_save_and_exit).click()
        message = self.driver.switch_to_alert().text()
        return message

    def common_coutomer_search(self, search_type, search_init_name, search_name, path, select_path, select_input_path,
                      search_value, select_button):
        """
        封装的搜索方法
        :param search_type:
        :param search_name:
        :return:
        """
        if search_type == search_init_name:
            self.driver.find_element_by_xpath(select_input_path).send_keys(search_value)
            self.driver.find_element_by_xpath(select_button).click()
            ele = self.driver.find_elements_by_xpath(self.list_consumer)
            for i in ele:
                if i.text == search_value:
                    logger.info("搜索!")
                    return True
                else:
                    logger.info("新建客户失败!")
                    return False
        else:
            self.driver.find_element_by_xpath(path).click()
            ele = self.driver.find_elements_by_xpath(select_path).click()
            for i in ele:
                if i.text == search_name:
                    i.click()
            self.driver.find_element_by_xpath(select_input_path).send_keys(search_value)
            self.driver.find_element_by_xpath(select_button).click()
            ele = self.driver.find_elements_by_xpath(self.list_consumer)

