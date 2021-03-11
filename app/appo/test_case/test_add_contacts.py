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
from app.appo.page.app import App
from utils.get_file import GetFile
from utils.swipe_screen import SwipeScreen


class TestAddContacts:
    info = GetFile(file_path=r'E:\HogwartsSDE17_HomeWork\config\info.yaml')

    def setup_class(self):
        self.driver = App().start_android_driver()
        self.swipe_find = SwipeScreen(self.driver)
        self.driver.find(MobileBy.XPATH, '//android.widget.TextView[@resource-id="com.tencent.wework:id/en5" '
                                         'and @text="通讯录"]').click()
        self.driver.swipe_find('//*[@text="添加成员"]').click()
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]').click()

        # -->未知问题 使用WebDriverWait会报timeout sleep就能成功 是WebDriverWait没用对？
        # WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_element(MobileBy.XPATH,
        #                                                                  '//android.widget.RelativeLayout['
        #                                                                  '@resource-id="com.tencent.wework:id/cth"]').click())
        sleep(2)
        # 点击手动输入添加
        self.driver.find(MobileBy.XPATH,
                         '//android.widget.RelativeLayout[@resource-id="com.tencent.wework:id/cth"]').click()

    def teardown_class(self):
        self.driver.stop_android_driver()

    @pytest.mark.parametrize(["name", "phone_numb", "e_mail"], info.get_value("addcontcts"))
    def test_add_contacts(self, name, phone_numb, e_mail, gender=None):
        """
        # 添加成员
        :return
        """

        try:
            WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find(MobileBy.XPATH,
                                                                       '//*[@text="完整输入"]').click())
            # self.driver.find_element(MobileBy.XPATH,
            #                          '///[@text="完整输入"]').click()
            WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find(MobileBy.XPATH,
                                                                       '//android.widget.LinearLayout['
                                                                       '1]/android.widget.RelativeLayout['
                                                                       '1]//*[@text="必填"]').send_keys(name))
            # self.driver.find_element(MobileBy.XPATH,
            #                          '//android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]//*[@text="必填"]').send_keys(
            #     name)
        except Exception:
            # 输入名字
            WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find(MobileBy.XPATH, '//*[contains(@text, ''"姓名")]//..//*[''@text="必填"]').send_keys(name))
            # self.driver.find_element(MobileBy.XPATH,
            #                          '//android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]//*[@text="必填"]').send_keys(
            #     name)

            # 选择男女
            # self.driver.find_element(By.XPATH, '//@resource-id="com.tencent.wework:id/b7m"').click()

            # 输入手机号
            self.driver.find(MobileBy.XPATH, '//*[contains(@text, "手机")]/..//*[@text="手机号"]').send_keys(phone_numb)

            # 输入邮箱
            self.driver.find(MobileBy.XPATH,
                             '//android.widget.LinearLayout[1]/android.widget.RelativeLayout[7]//*[@text="选填"]').send_keys(
                e_mail)

            #
            self.driver.find(MobileBy.XPATH, '//*[@text="保存并继续添加"]').click()
            sleep(2)
            assert '添加成功' in self.driver.page_source()

        sleep(3)
