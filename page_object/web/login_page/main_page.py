#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: main_page.py
@time: 2021/3/1 22:03
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from page_object.web.login_page.login_page import LoginPage
from page_object.web.login_page.register_page import RegisterPage


# 首页page
class MainPage:
    def __init__(self):
        self.driver = webdriver.Chrome(r'D:\Google\Chrome\Application\chromedriver.exe')
        self.driver.get('https://work.weixin.qq.com/')
        self.driver.implicitly_wait(5)

    def goto_register(self):
        self.driver.find_element(By.XPATH, '//*[@class="index_head_info_pCDownloadBtn"]').click()
        return RegisterPage(self.driver)

    def goto_login(self):
        self.driver.find_element(By.XPATH, '//*[@class="index_top_operation_loginBtn"]').click()
        return LoginPage(self.driver)

    def driver_quite(self):
        return self.driver.quit()
