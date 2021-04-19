#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: search_page.py
@time: 2021/3/11 23:33
"""

from ui_framework.base.base_page import BasePage


class SearchPage(BasePage):

    def edit_search_box(self):
        """
        编辑输入框
        :return:
        """
        self.parse(r'../../keywords/search_page.yaml', 'edit_search_box')
