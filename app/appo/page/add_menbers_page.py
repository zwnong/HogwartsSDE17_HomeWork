#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: add_menbers_page.py
@time: 2021/3/9 19:52
"""
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from ui_framework.base.base_page import BasePage
from app.appo.page.full_edit_page import FullEditPage
from app.appo.page.quick_entry_page import QuickEditPage


# 添加成员page
class AddMembersPage(BasePage):
    def goto_manuall_edit_page(self):
        """
        点击 手动添加成员到快速输入page
        :return:
        """

        self.find(MobileBy.XPATH,
                  '//android.widget.RelativeLayout[@resource-id="com.tencent.wework:id/cth"]').click()
        sleep(2)
        if '快速输入' in self.driver.page_source:
            self.find(MobileBy.XPATH, '//*[@text="快速输入"]').click()
        else:
            print('当前处于快速输入页')
        return QuickEditPage(self.driver)

    def goto_full_edit_page(self):
        """
        点击手动添加成员到完整输入page
        :return:

        """
        self.find(MobileBy.XPATH,
                  '//android.widget.RelativeLayout[@resource-id="com.tencent.wework:id/cth"]').click()
        try:
            WebDriverWait(self.driver, 10, 0.1).until(lambda x: x.find(MobileBy.XPATH, '//*[@text="完整输入"]').click())
            return FullEditPage(self.driver)
        except:
            return FullEditPage(self.driver)

