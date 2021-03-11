#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: quick_entry_page.py
@time: 2021/3/9 20:04
"""
from appium.webdriver.common.mobileby import MobileBy

from ui_framework.base.base_page import BasePage


class QuickEditPage(BasePage):

    def edit_name(self, name):
        self.find(MobileBy.XPATH, '//*[contains(@text, "姓名")]//..//*[@text="必填"]').send_keys(name)

    def edit_phones(self, phone):
        self.find(MobileBy.XPATH, '//*[contains(@text, "手机")]/..//*[@text="必填"]').send_keys(phone)

    def click_save(self):
        self.find(MobileBy.XPATH, '//*[@text="保存"]').click()

    def click_save_and_continue_adding(self):
        self.find(MobileBy.XPATH, '//*[@text="保存并继续添加"]').click()


