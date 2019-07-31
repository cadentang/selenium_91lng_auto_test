# coding=utf8
import time
from selenium.webdriver.common.by import By

from common.common_base_page import BasePage


class BusinessOverviewPage(BasePage):
    go_to_start = '//*[@id="app"]/section/main/div[1]/div/div/div[2]/button'
    go_to_confirm = '//*[@id="app"]/section/main/div/div/div/div/div[2]/div/div[2]/div'


# if __name__ == "__main__":
#     t = IndexPage(url="http://bpm.hhtdlng.com")
#     time.sleep(2)
#     print(t.go_to_start)
#     # t.driver.find_element_by_xpath("//*[@id='app']/section/main/div[1]/div/div/div[2]/button")
#     t.driver.find_element_by_xpath(t.go_to_start).click()
#     t.close()
