#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: reuse_broweser.py
@time: 2021/2/28 14:29
"""
from selenium import webdriver
from selenium.webdriver.common.by import By


class ReuesBrowser:
    # 复用浏览器
    def test_add_adress(self):
        # 什么chrome参数
        self.chrome_arg = webdriver.ChromeOptions()
        # 调试地址
        self.chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(r'D:\Google\Chrome\Application\chromedriver.exe', options=self.chrome_arg)
        self.driver.find_element(By.XPATH, '//*[@id="menu_contacts"]').click()

