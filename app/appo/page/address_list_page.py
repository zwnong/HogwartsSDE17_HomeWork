#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: address_list_page.py
@time: 2021/3/9 19:44
"""
from appium.webdriver.common.mobileby import MobileBy

from ui_framework.base.base_page import BasePage
from app.appo.page.add_menbers_page import AddMembersPage


# 通讯录page
from app.appo.page.search_page import SearchPage


class AddressListPage(BasePage):
    def click_add_members(self):
        """
        # 点击添加成员
        :return:
        """
        self.swipe_find('//*[@text="添加成员"]').click()
        return AddMembersPage(self.driver)

    def click_search_member(self):
        """
        点击搜索成员
        :return:
        """
        self.find(MobileBy.XPATH, '//android.widget.TextView[@resource-id="com.tencent.wework:id/igk"]').click()
        return SearchPage(self.driver)