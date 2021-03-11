#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: full_edit_page.py
@time: 2021/3/9 20:11
"""
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from ui_framework.base.base_page import BasePage


# 完整输入页
class FullEditPage(BasePage):
    # edit_name_elament = (MobileBy.XPATH, 'resource-id="com.tencent.wework:id/b7m" and text="必填"')
    # edit_phone_element = (MobileBy.XPATH, 'android.widget.RelativeLayout[5][@text="手机号"]')
    edit_email_element = (MobileBy.XPATH, '//android.widget.LinearLayout[1]/android.widget.RelativeLayout[7]//*['
                                          '@text="选填"]')
    save_element = (MobileBy.XPATH, '//*[@text="保存"]')
    save_and_continue_adding_element = (MobileBy.XPATH, '//*[@text="保存并继续添加"]')

    def edit_name(self, name):
        """
        输入姓名
        :param name:
        :return:
        """
        sleep(3)
        WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element(MobileBy.XPATH, '//*[contains(@text, '
                                                                                           '"姓名")]//..//*['
                                                                                           '@text="必填"]')).send_keys(
            name)

    def edit_phone(self, phone_numb):
        """
        输入手机号
        :param phone_numb:
        :return:
        """

        self.find(MobileBy.XPATH, '//*[contains(@text, "手机")]/..//*[@text="手机号"]').send_keys(phone_numb)

    def edit_email(self, e_mail):
        """
        输入e_mail
        :param e_mail:
        :return:
        """
        self.find(*self.edit_email_element).send_keys(e_mail)

    def click_save(self):
        """
        点击保存
        :return:
        """
        self.find(*self.save_element).click()

    def click_save_and_continue_adding(self):
        """
        点击  保存并继续添加
        :return:
        """
        self.find(*self.save_and_continue_adding_element).click()
