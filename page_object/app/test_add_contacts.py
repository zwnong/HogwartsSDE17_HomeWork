#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: test_add_contacts.py
@time: 2021/3/5 19:55
"""
from time import sleep
import pytest
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from page_object.app.startappium import StartAppium
from util.get_yaml import GetFile


class TestAddContacts:
    info = GetFile(file_path=r'E:\HogwartsSDE17_HomeWork\config\info.yaml')

    def setup_class(self):
        self.driver = StartAppium().android_driver()
        self.driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@resource-id="com.tencent.wework:id/en5" '
                                                 'and @text="通讯录"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]').click()

        # def wait_name(driver):
        #     """
        #     :param driver:
        #     :return:
        #     """
        #     self.driver.find_element(MobileBy.XPATH, '//android.widget.RelativeLayout[@resource-id="com.tencent.wework:id/cth"]').click()
        #     return len(self.driver.find_elements(MobileBy.XPATH, '//android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]//*[@text="必填"]')) > 0
        # WebDriverWait(self.driver, 10).until(wait_name)

        sleep(2)
        self.driver.find_element(MobileBy.XPATH,
                                 '//android.widget.RelativeLayout[@resource-id="com.tencent.wework:id/cth"]').click()

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize(["name", "phone_numb", "e_mail"], info.get_value("addcontcts"))
    def test_add_contacts(self, name, phone_numb, e_mail, gender=None):
        """
        # 添加成员
        :return:
        """

        try:
            self.driver.find_element(MobileBy.XPATH,
                                     '//@resource-id="com.tencent.wework:id/ig8" and @text="完整输入"').click()
            self.driver.find_element(MobileBy.XPATH,
                                     '//android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]//*[@text="必填"]').send_keys(
                name)
        except Exception:
            # 输入名字
            self.driver.find_element(MobileBy.XPATH,
                                     '//android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]//*[@text="必填"]').send_keys(
                name)

            # 选择男女
            # self.driver.find_element(By.XPATH, '//@resource-id="com.tencent.wework:id/b7m"').click()

            # 输入手机号
            self.driver.find_element(MobileBy.XPATH,
                                     '//android.widget.LinearLayout[1]/android.widget.RelativeLayout[5]//*[@text="手机号"]').send_keys(
                phone_numb)

            # 输入邮箱
            self.driver.find_element(MobileBy.XPATH,
                                     '//android.widget.LinearLayout[1]/android.widget.RelativeLayout[7]//*[@text="选填"]').send_keys(
                e_mail)

            #
            self.driver.find_element(MobileBy.XPATH, '//*[@text="保存并继续添加"]').click()

        sleep(3)
