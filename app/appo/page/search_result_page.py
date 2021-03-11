#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: search_result_page.py
@time: 2021/3/10 18:26
"""
from appium.webdriver.common.mobileby import MobileBy

from ui_framework.base.base_page import BasePage
from app.appo.page.contact_detail_briefInfo_profile_page import ContactDetailBriefInfoProfilePage


class SearchResultPage(BasePage):

    def click_first_name(self, name):
        """
        点击第一个出现的名字
        :param name:
        :return:
        """
        len_value = self.finds(MobileBy.XPATH, f'//*[@text="{name}"]')
        len_value[1].click()
        return ContactDetailBriefInfoProfilePage(self.driver)
