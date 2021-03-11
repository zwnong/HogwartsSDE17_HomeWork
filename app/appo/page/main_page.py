#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: main_page.py
@time: 2021/3/9 19:35
"""
from appium.webdriver.common.mobileby import MobileBy
from ui_framework.base.base_page import BasePage
from app.appo.page.address_list_page import AddressListPage


# 主页
class MainPage(BasePage):
    addresslist_element = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="com.tencent.wework:id/en5" and '
                                           '@text="通讯录"]')

    def click_address_list(self):
        """
        # 点击通讯录
        :return:
        """
        # *解元组
        self.find(*self.addresslist_element).click()
        return AddressListPage(self.driver)


