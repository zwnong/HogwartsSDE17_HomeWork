#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: market_page.py
@time: 2021/3/11 23:29
"""
from appium.webdriver.common.mobileby import MobileBy

from ui_framework.base.base_page import BasePage
from ui_framework.xueqiu_app.page.search_page import SearchPage


class MarketPage(BasePage):
    def click_search(self):
        """
        点击搜索按钮
        :return:
        """
        self.find_and_click(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/action_search"]')
        return SearchPage(self.driver)
