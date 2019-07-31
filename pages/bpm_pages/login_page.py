# coding=utf8
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

from .index_page import IndexPage


class LoginPage(IndexPage):

    go_to_username_xpath = "//*[@id='app']/div/form/div[1]/div/div[1]/input"
    go_to_password_xpath = "//*[@id='app']/div/form/div[2]/div/div[1]/input"
    go_to_mark_xpath = "//*[@id='app']/div/form/div[3]/div/div/div[1]/div/input"
    go_to_login_xpath = "//*[@id='app']/div/form/div[4]/div[2]/div/button"


# if __name__ == "__main__":
#     # t = LoginPage(url="http://bpm.hhtdlng.com/#/login", browser_type="firefox")
#     driver = webdriver.Chrome()
#     driver.get("http://bpm.hhtdlng.com/#/login")
#     time.sleep(2)
#     driver.find_element_by_xpath("//*[@id='app']/div/form/div[1]/div/div[1]/input").send_keys("15275457888")
#     driver.find_element_by_xpath("//*[@id='app']/div/form/div[2]/div/div[1]/input").send_keys("457888")
#     driver.find_element_by_xpath("//*[@id='app']/div/form/div[3]/div/div/div[1]/div/input").send_keys("1471")
#     driver.find_element_by_xpath("//*[@id='app']/div/form/div[4]/div[2]/div/button").click()
#     time.sleep(2)
#     driver.close()
