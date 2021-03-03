#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: home_main_page.py
@time: 2021/3/3 20:29
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from page_object.web.address.address_main_page import AddressMainPage


class HomeMainPage:
    def __init__(self):
        self.chrome_arg = webdriver.ChromeOptions()
        self.chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(r'D:\Google\Chrome\Application\chromedriver.exe', options=self.chrome_arg)
        self.driver.implicitly_wait(5)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')

    def display_wait_condition(self, ele1, ele2, num=None):
        """
        # 两种情况适用
        :param num:
        :param ele1: 需要操作的元素
        :param ele2: 需要等待出现的元素
        :param num: 若需要操作的元素为复数，则传num
        :return: 仅用作学习巩固所用
        """
        try:
            self.driver.find_element(By.XPATH, f'//*[@id={ele1}]').click()
            return len(self.driver.find_elements(By.XPATH, f'//*[@id={ele2}]')) > 0
        except Exception:
            self.driver.find_elements(By.XPATH, f'//*[@id={ele1}]')[num].click()
            return len(self.driver.find_elements(By.XPATH, f'//*[@id={ele2}]')) > 0

    def goto_address(self):
        """
            # 点击通讯录
            :return:通讯录
            """
        self.driver.find_element(By.XPATH, '//*[@id="menu_contacts"]').click()
        return AddressMainPage(self.driver)

    def application_management(self):
        """
            # 点击应用管理
            :return: 应用管理
            """
        self.driver.find_element(By.XPATH, '//*[@id="menu_apps"]').click()

    # todo
    def customer_contact(self):
        pass
