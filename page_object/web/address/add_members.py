#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: add_members.py
@time: 2021/3/3 20:52
"""
from selenium.webdriver.common.by import By


class AddMembers:
    def __init__(self, driver):
        self.driver = driver

    def click_save_and_continue_adding(self):
        """
        # 点击保存并继续
        :return:
        """
        self.driver.find_element(By.XPATH, '//*[@class="qui_btn ww_btn ww_btn_Blue js_btn_continue"]').click()

    def click_save(self):
        pass

    def user_name(self):
        self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("first add")

    def another_name(self):
        pass
