#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: address_main_page.py
@time: 2021/3/3 20:39
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from page_object.web.address.add_members import AddMembers


class AddressMainPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_members(self):
        """
        # 点击添加成员
        :return: 添加成员
        """
        def wait_name(driver):
            """
            # 加了隐式等待点击成功却没有跳转页面：隐式等待只判断元素可点击
            需要使用显示等待：（until（）传等待条件函数名） 首先点击添加成员，判断下一个页面的某一个元素出现（长度大于0）
            :param driver:
            :return:
            """
            self.driver.find_elements(By.XPATH, '//*[@class="qui_btn ww_btn js_add_member"]')[1].click()
            return len(self.driver.find_elements(By.XPATH, '//*[@id="username"]')) > 0
        WebDriverWait(self.driver, 10).until(wait_name)

        return AddMembers(self.driver)

    def click_del_member(self):
        pass