# coding=utf8
import time
from selenium.webdriver.common.by import By

from common.common_base_page import BasePage


class IndexPage(BasePage):
    go_to_login = (By.LINK_TEXT, "登录")
    go_to_start = '//*[@id="app"]/section/main/div[1]/div/div/div[2]/button'


# if __name__ == "__main__":
#     t = IndexPage(url="http://bpm.hhtdlng.com")
#     time.sleep(2)
#     print(t.go_to_start)
#     # t.driver.find_element_by_xpath("//*[@id='app']/section/main/div[1]/div/div/div[2]/button")
#     t.driver.find_element_by_xpath(t.go_to_start).click()
#     t.close()
