#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: test_search.py
@time: 2021/3/11 23:40
"""
from time import sleep

from ui_framework.xueqiu_app.page.app import App


class TestSearch:
    def setup(self):
        self.app = App().start_android_driver()

    def teardown(self):
        self.app.stop_android_driver()

    def test_search_a(self):
        self.app.goto_main_page().goto_market().click_search().edit_search_box()
        sleep(5)

    def test_agree(self):
        self.app.goto_main_page().goto_market()
        sleep(3)
