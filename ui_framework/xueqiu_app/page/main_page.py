#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: main_page.py
@time: 2021/3/11 23:13
"""
from appium.webdriver.common.mobileby import MobileBy

from ui_framework.base.base_page import BasePage
from ui_framework.xueqiu_app.page.market_page import MarketPage


class MainPage(BasePage):
    click_market_page_element = (MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/tab_name" and @text="行情"]')

    def click_market_page(self):
        """
        点击行情
        :return:
        """
        self.find_and_click(*self.click_market_page_element)
        return MarketPage(self.driver)
