#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: main_page.py
@time: 2021/3/11 23:13
"""

from ui_framework.base.base_page import BasePage
from ui_framework.xueqiu_app.page.market_page import MarketPage
import sys

sys.path.append('..')


class MainPage(BasePage):
    def goto_market(self):
        """
        点击行情
        :return:
        """
        self.parse(r'../../keywords/main_page.yaml', 'goto_market')
        return MarketPage(self.driver)
