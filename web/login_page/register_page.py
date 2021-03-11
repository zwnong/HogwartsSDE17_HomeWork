#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: register_page.py
@time: 2021/3/1 22:10
"""
from time import sleep

from selenium.webdriver.common.by import By


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    def register(self):
        """
        # 注册按钮
        :return:
        """
        self.driver.find_element(By.XPATH, '//*[@id="submit_btn"]').click()

    def send_company_name_keys(self):
        """
        # 企业名称
        :return: 输入企业名称
        """
        self.driver.find_element(By.XPATH, '//*[@id="corp_name"]').send_keys("123456")
        sleep(5)



