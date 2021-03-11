#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: test_login_in_cookie.py
@time: 2021/3/1 20:22
"""
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLoginInCookie:
    def setup(self):
        self.driver = webdriver.Chrome(r'D:\Google\Chrome\Application\chromedriver.exe')
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_login_cookie(self):
        self.driver.get('https://work.weixin.qq.com/')
        a = self.driver.find_elements(By.XPATH, '//*[@class="index_head_info_pCDownloadBtn"]')
        print(len(a))
