# -*- coding: utf-8 -*-
__author__ = 'caden'
"""
description:这里是登录相关数据
"""
LOGIN_URL = "http://bpm.hhtdlng.com/#/login"
INDEX_URL = "http://bpm.hhtdlng.com"

# 测试登录的账号
test_login_data = {
    "success_data": ["15275457888", "457888", "1471"],
    "fail_data_phone_error": ["15275457889", "457888", "1471"],
    "fail_data_password_error": ["15275457888", "457999", "1471"],
    "fail_data_verification_error": ["15275457888", "457888", "1111"],
}

# 测试基础信息添加的账号
add_base_login_data = {
    "base_data": ["15275457888", "457888", "1471", "http://bpm.hhtdlng.com/#/login"],
}

# 测试业务业务流程账号
business_login_data = {
    "success_data": ["15275457888", "457888", "1471"],
}
