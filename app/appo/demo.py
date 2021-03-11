#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: demo.py
@time: 2021/3/9 20:17
"""
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from utils.swipe_screen import SwipeScreen

capabilities = {
    'platformName': 'Android',
    "automationName": "UiAutomator2",
    'deviceName': '127.0.0.1:21503',
    'appPackage': 'com.tencent.wework',
    'appActivity': 'com.tencent.wework.launch.WwMainActivity',
    # 'appPackage': self.package,
    # 'appActivity': self.activity,
    # 跳过安装uiautomator2 服务
    'skipServerInstallation': True,
    # 跳过初始化
    'skipDeviceInstallation': True,
    'noReset': True
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
driver.implicitly_wait(5)

driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@resource-id="com.tencent.wework:id/en5" '
                                    'and @text="通讯录"]').click()
SwipeScreen(driver).swipe_find('//*[@text="添加成员"]').click()
sleep(2)
# # 点击手动输入添加
driver.find_element(MobileBy.XPATH, '//android.widget.RelativeLayout[@resource-id="com.tencent.wework:id/cth"]').click()
# # 输入名字
# WebDriverWait(driver, 10, 0.5).until(lambda x: x.find_element(MobileBy.XPATH,
#                                                               '//android.widget.LinearLayout['
#                                                               '1]/android.widget.RelativeLayout['
#                                                               '1]//*[@text="必填"]').send_keys(123))
#
# driver.find_element(MobileBy.XPATH,
#                     '//android.widget.LinearLayout[1]/android.widget.RelativeLayout[5]//*[@text="手机号"]').send_keys(
#     '18541254785')
#
# # 输入邮箱
# driver.find_element(MobileBy.XPATH,
#                     '//android.widget.LinearLayout[1]/android.widget.RelativeLayout[7]//*[@text="选填"]').\
#                     send_keys('18541254785@163.com')

# driver.find_element(MobileBy.XPATH, '//android.widget.EditText[@resource-id="com.tencent.wework:id/b7m" and @text="必填"]').send_keys('s')
# driver.find_element(MobileBy.XPATH, '//android.widget.EditText[@resource-id="com.tencent.wework:id/fwi" and @text="必填"]').send_keys('13522226584')
driver.find_element(MobileBy.XPATH, '//android.widget.EditText[@resource-id="com.tencent.wework:id/b7m" and @text="必填"]').send_keys('3')
driver.find_element(MobileBy.XPATH, "//android.widget.EditText[@resource-id='com.tencent.wework:id/fwi' and @text='手机号']").send_keys('18546524785')
sleep(5)
driver.quit()