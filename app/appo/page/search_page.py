#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: search_page.py
@time: 2021/3/10 18:21
"""
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from ui_framework.base.base_page import BasePage
from app.appo.page.search_result_page import SearchResultPage


class SearchPage(BasePage):
    def edit_search(self, name):
        """
        搜索框 输入
        :param name:
        :return:
        """
        self.find(MobileBy.XPATH, '//*[@text="搜索"]').send_keys(name)
        sleep(3)
        return SearchResultPage(self.driver)
