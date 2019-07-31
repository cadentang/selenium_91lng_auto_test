# -*- coding: utf-8 -*-
__author__ = 'caden'
"""
description:新建客户的相关数据
"""
# 只新增客户的基础信息
consumer_data_base = {
    "customer_name": "山东蓝水能源有限公司",
    "short_customer_name": "山东蓝水",
    "customer_grade": "一类客户",
    "contact_person": "唐半闲",
    "contact_phone": "19800000000",
    "sale_man_name": "刘鹏",
    "social_credit_code": "ABCDEFGHJK12345678",
    "consumer_address": "山东省济南市工业南路57号",
    "should_pay_money": "300000",
    "is_payer": 1,  # 0,代表选择已有的付款方，1，代表将新加的客户作为付款方
    "payer_select": "陕西元和石油天然气有限公司",
    "consumer_category_display": "贸易商",
    "is_business_contract": 0,  # 0,代表不填写业务信息，1，代表将填写业务信息， 2，代表填写业务信息和合同信息
    "free_hour": "12",
    "waiting_price": "300",
    "kui_tons_standard": "200",
    "settlement_cycle_display": "周结",
    "contract_no": "NO22222",
    "contract_start_date": "2019-03-19",
    "contract_end_date": "2019-10-19",
    }

# 只新增客户的基础信息和业务信息
consumer_data_base_and_business = {
    "customer_name": "山东蓝水能源有限公司",
    "short_customer_name": "山东蓝水",
    "customer_grade": "一类客户",
    "contact_person": "唐半闲",
    "contact_phone": "19800000000",
    "sale_man_name": "刘鹏",
    "social_credit_code": "ABCDEFGHJK12345678",
    "consumer_address": "山东省济南市工业南路57号",
    "should_pay_money": "300000",
    "is_payer": 1,  # 0,代表选择已有的付款方，1，代表将新加的客户作为付款方
    "payer_select": "陕西元和石油天然气有限公司",
    "consumer_category_display": "贸易商",
    "is_business_contract": 1,  # 0,代表不填写业务信息，1，代表将填写业务信息， 2，代表填写业务信息和合同信息
    "free_hour": "12",
    "waiting_price": "300",
    "kui_tons_standard": "200",
    "settlement_cycle_display": "周结",
    "contract_no": "NO22222",
    "contract_start_date": "2019-03-19",
    "contract_end_date": "2019-10-19",
    }

# 新增客户的所有信息
consumer_data_all = {
    "customer_name": "山东蓝水能源有限公司",
    "short_customer_name": "山东蓝水",
    "customer_grade": "一类客户",
    "contact_person": "唐半闲",
    "contact_phone": "19800000000",
    "sale_man_name": "刘鹏",
    "social_credit_code": "ABCDEFGHJK12345678",
    "consumer_address": "山东省济南市工业南路57号",
    "should_pay_money": "300000",
    "is_payer": 1,  # 0,代表选择已有的付款方，1，代表将新加的客户作为付款方
    "payer_select": "陕西元和石油天然气有限公司",
    "consumer_category_display": "贸易商",
    "is_business_contract": 1,  # 0,代表不填写业务信息，1，代表将填写业务信息， 2，代表填写业务信息和合同信息
    "free_hour": "12",
    "waiting_price": "300",
    "kui_tons_standard": "200",
    "settlement_cycle_display": "周结",
    "contract_no": "NO22222",
    "contract_start_date": "2019-03-19",
    "contract_end_date": "2019-10-19",
    }

# 编辑客户业务信息成功
consumer_data_edit_free_hour_success = {
    "free_hour": "12",
}

# 编辑客户名称信息失败
consumer_data_edit_consumer_name_fail = {
    "customer_name": "中广核东力燃气有限公司",
}

# 客户列表搜索用例数据
consumer_search_data = {
    "name": "山东蓝水能源有限公司",
    "short_name": "山东蓝水",
    "contact_phone": "19800000000",
    "sale_man_name": "刘鹏",
    "no_data": "aaaaaa"
}