#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: startappium.py
@time: 2021/3/4 0:49
"""
from appium import webdriver


class StartAppium:
    # def __init__(self, package=None, activity=None):
    #     if package or activity is None:
    #         self.package = 'com.tencent.wework'
    #         self.activity = 'com.tencent.wework.launch.WwMainActivity'
    #     else:
    #         self.package = package
    #         self.activity = activity

    def android_driver(self):
        capabilities = {
            'platformName': 'Android',
            "automationName": "UiAutomator2",
            'deviceName': '127.0.0.1:21503',
            'appPackage': 'com.cyanogenmod.filemanager',
            'appActivity': 'com.cyanogenmod.filemanager.activities.NavigationActivity',
            # 'appPackage': self.package,
            # 'appActivity': self.activity,
            'noReset': True
        }
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
        return driver

    def ios_driver(self):
        pass
