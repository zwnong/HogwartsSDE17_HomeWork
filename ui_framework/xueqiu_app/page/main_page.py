#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: main_page.py
@time: 2021/3/11 23:13
"""
import yaml

from ui_framework.base.base_page import BasePage
from ui_framework.utils.get_file import GetFile
from ui_framework.xueqiu_app.page.market_page import MarketPage
import sys
sys.path.append('..')


class MainPage(BasePage):
    def goto_market(self):
        """
        点击行情
        :return:
        """
        with open(r'../../keywords/main_page.yaml', 'r', encoding='utf-8') as f:
            functance = yaml.load(f)
        steps = functance.get('main_page')
        for step in steps:
            if step['action'] == 'find_and_click':
                self.find_and_click(step['locator'], step['element'])
        # locator = data_mp('locator')
        # element = data_mp('element')
        # function = GetFile(r'../../keywords/main_page.yaml')
        # locator = function.get_yaml_data('main_page')[]
        # element = function('element')
        # self.find_and_click(locator, element)
        # self.find_and_click('xpath', '//*[@resource-id="com.xueqiu.android:id/tab_name" and @text="行情"]')
        return MarketPage(self.driver)


