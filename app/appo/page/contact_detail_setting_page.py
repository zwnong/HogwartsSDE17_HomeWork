#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: contact_detail_setting_page.py
@time: 2021/3/10 20:00
"""
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from ui_framework.base.base_page import BasePage


# 联系人详情设置page
from app.appo.page.edit_member_page import EditMemberPage


class ContactDetailSettingPage(BasePage):
    def click_edit_member(self):
        """
        点击编辑成员
        :return:
        """
        sleep(3)
        self.web_driver_wait(MobileBy.XPATH, '//*[@text="编辑成员"]').click()

        return EditMemberPage(self.driver)
