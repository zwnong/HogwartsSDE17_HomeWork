#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: test_scroll_through.py
@time: 2021/3/6 2:23
"""
from time import sleep
from appium.webdriver.common.mobileby import MobileBy
from page_object.app.scroll_through import ScrollThrough
from page_object.app.startappium import StartAppium
from util.swipe_screen import SwipeScreen


class TestScrollThrough:
    def setup(self):
        self.driver = StartAppium().android_driver()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_scroll_through(self):
        run = ScrollThrough()
        s = SwipeScreen(self.driver)
        s.swipe_on('up')
        # run.Scroll_through_by_xpath_click('//android.widget.TextView[@resource-id=“com.cyanogenmod.filemanager:id/navigation_view_item_name" and @text="sslCache"]')
        sleep(5)
