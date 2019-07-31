# coding=utf8
from selenium.webdriver.common.by import By

from common.common_base_page import BasePage


class ForgetPasswordPage(BasePage):

    go_to_index_ele = (By.XPATH, "//*[@id='app']/div/header/div/a/div")
    go_to_message_center_ele = (By.XPATH, "//*[@id='app']/div/header/div/div/div/div[2]/div/span[1]/span/div/i")
    go_to_personal_center_ele = (By.XPATH, "//*[@id='app']/div/header/div/div/div/div[2]/div/div/span")

