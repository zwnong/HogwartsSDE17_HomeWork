#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: test_search.py
@time: 2021/3/11 23:40
"""
from time import sleep

import allure

from ui_framework.xueqiu_app.page.app import App


@allure.feature("行情页面")
class TestSearch:
    def setup(self):
        self.app = App().start_android_driver()

    def teardown(self):
        self.app.stop_android_driver()

    @allure.story('搜索Alibaba')
    def test_search_a(self):
        self.app.goto_main_page().goto_market().click_search().edit_search_box()
        assert 1 == 1
        sleep(5)

    @allure.story('进入到行情页面')
    def test_agree(self):
        self.app.goto_main_page().goto_market()
        assert 1 != 2
        sleep(3)
