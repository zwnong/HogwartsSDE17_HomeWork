#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: test_web_reuse_cookie.py
@time: 2021/2/27 21:28
"""
import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestReuseCookie:
    def setup(self):
        # 什么chrome参数
        self.chrome_arg = webdriver.ChromeOptions()
        # 调试地址
        self.chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(r'D:\Google\Chrome\Application\chromedriver.exe', options=self.chrome_arg)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_reuse_chrome(self):
        """
        # 复用浏览器登录
        :return:
        """
        self.driver.get('https://work.weixin.qq.com/')
        self.driver.find_element(By.XPATH, '//*[@class="index_top_operation_loginBtn"]').click()
        sleep(5)

    def test_4(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.find_element(By.XPATH, '//*[@id="menu_contacts"]').click()
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="menu_customer"]').click()
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="menu_index"]').click()
        sleep(5)

    def test_cookie_login(self):
        """
        使用cookie登录
        :return:
        """
        # 存入cookies
        # cookies = self.driver.get_cookies()
        # with open('cookies.text', 'w', encoding='utf-8') as f:
        #     f.write(json.dumps(cookies))
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        # # 读取cookies
        with open('cookies.text', 'r', encoding='utf-8') as f:
            raw = f.read()
            print(raw)
            cookies = json.loads(raw)
        for i in cookies:
            print(i)
            if 'expiry' in cookies:
                cookies.pop("expiry")
            self.driver.add_cookie(i)
        self.driver.refresh()
        sleep(5)

    def test_1(self):
        pass
