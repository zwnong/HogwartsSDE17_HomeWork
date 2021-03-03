#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: login_page.py
@time: 2021/3/1 22:11
"""
from selenium.webdriver.common.by import By

from page_object.web.login_page.register_page import RegisterPage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def goto_register(self):
        """
        # 进入到企业注册野蛮
        :return:
        """
        self.driver.find_element(By.XPATH, '//*[@class="login_registerBar_link"]').click()
        return RegisterPage(self.driver)

    def login(self):
        """
        # 扫码登录（无法测试）
        :return: 手机扫码登陆无法实现
        """
        pass
