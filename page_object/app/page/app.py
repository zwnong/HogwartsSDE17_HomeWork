#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: app.py
@time: 2021/3/4 0:49
"""
from appium import webdriver

from page_object.app.base.base_page import BasePage
from page_object.app.page.main_page import MainPage


class App(BasePage):
    # 复用driver 判断driver是否为None
    def start_android_driver(self):
        if self.driver is None:
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
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
            self.driver.implicitly_wait(10)
        else:
            self.driver.launch_app()
        return self

    def restart_android_driver(self):
        """
        # 重启
        :return:
        """
        self.driver.close()
        self.driver.launch_app()

    def stop_android_driver(self):
        self.driver.quit()

    def start_ios_driver(self):
        pass

    def goto_main_page(self):
        return MainPage(self.driver)

    def page_source(self):
        return self.driver.page_source

    def implicitly_wait(self, time):
        return self.driver.implicitly_wait(time)
