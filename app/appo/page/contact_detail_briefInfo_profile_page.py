#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: contact_detail_briefInfo_profile_page.py
@time: 2021/3/10 19:47
"""
from appium.webdriver.common.mobileby import MobileBy

from ui_framework.base.base_page import BasePage


# 联系人详细资料简介page
from app.appo.page.contact_detail_setting_page import ContactDetailSettingPage


class ContactDetailBriefInfoProfilePage(BasePage):
    def click_more_info_page(self):
        """
        点击更多：右上角三点
        :return:
        """
        self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/iga"]').click()
        return ContactDetailSettingPage(self.driver)
