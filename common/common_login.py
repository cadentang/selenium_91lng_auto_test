# -*- coding: utf-8 -*-
__author__ = 'caden'
"""
description:封装的登录方法
"""
from pages.bpm_pages.login_page import LoginPage
from utils.log import logger
from data.bpm_data.login_data import LOGIN_URL, INDEX_URL
from time import sleep


# BPM的登录
def common_bpm_login(phone, password, verification_code, driver):

    driver.get(LOGIN_URL)
    driver.find_element_by_xpath(LoginPage.go_to_username_xpath).send_keys(phone)
    driver.find_element_by_xpath(LoginPage.go_to_password_xpath).send_keys(password)
    driver.find_element_by_xpath(LoginPage.go_to_mark_xpath).send_keys(verification_code)
    driver.find_element_by_xpath(LoginPage.go_to_login_xpath).click()
    sleep(3)
    if driver.title == "业务概览":
        logger.info("成功登录!")
        return True
    else:
        logger.info("登录失败！")
        return False


# TMS的登录
def common_tms_login(phone, password, verification_code, login_url):
    t = LoginPage(login_url)
    t.driver.find_element_by_xpath(t.go_to_username_xpath).send_keys(phone)
    t.driver.find_element_by_xpath(t.go_to_password_xpath).send_keys(password)
    t.driver.find_element_by_xpath(t.go_to_mark_xpath).send_keys(verification_code)
    t.driver.find_element_by_xpath(t.go_to_login_xpath).click()
    if t.driver.title == "车辆调度概览":
        logger.info("成功登录!")
        return t.driver
    else:
        logger.info("登录失败！")
        return False