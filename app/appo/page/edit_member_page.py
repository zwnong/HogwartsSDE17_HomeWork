#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: edit_member_page.py
@time: 2021/3/10 21:41
"""
from appium.webdriver.common.mobileby import MobileBy

from ui_framework.base.base_page import BasePage


class EditMemberPage(BasePage):
    def click_del_member(self):
        """
        删除成员
        :return:
        """
        self.find(MobileBy.XPATH, '//*[@text="删除成员"]').click()

    def click_sure(self):
        """
        点击确定
        :return:
        """
        self.find(MobileBy.XPATH, '//*[@text="确定"]').click()

    def click_call_off(self):
        """
        点击取消
        :return:
        """
        self.find(MobileBy.XPATH, '//*[@text="取消"]').click()
