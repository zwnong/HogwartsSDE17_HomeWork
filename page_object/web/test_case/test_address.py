#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: test_address.py
@time: 2021/3/3 21:02
"""
from page_object.web.home_page.home_main_page import HomeMainPage


class TestAddress:
    def setup(self):
        self.main = HomeMainPage()

    def teardown(self):
        pass

    def test_address(self):
        self.main.goto_address().click_add_members().click_save_and_continue_adding()
