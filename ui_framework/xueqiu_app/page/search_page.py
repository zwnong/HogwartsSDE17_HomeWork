#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: search_page.py
@time: 2021/3/11 23:33
"""
from appium.webdriver.common.mobileby import MobileBy

from ui_framework.base.base_page import BasePage


class SearchPage(BasePage):

    def edit_search_box(self):
        """
        编辑输入框
        :return:
        """
        self.find_and_sendkeys(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/search_input_text"]', "alibaba")
