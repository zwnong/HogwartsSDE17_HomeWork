#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: scroll_through.py
@time: 2021/3/6 1:46
"""
from time import sleep

from page_object.app.startappium import StartAppium
from util.swipe_screen import SwipeScreen
from appium.webdriver.common.mobileby import MobileBy


class ScrollThrough:
    def __init__(self):
        self.driver = StartAppium().android_driver()
        self.swipe_screen = SwipeScreen(self.driver)

    def scroll_through_by_xpath_click(self, xpath_e):
        """
        输入xpath定位信息
        :return:
        """
        try:
            self.driver.find_element(MobileBy.XPATH, f'{xpath_e}').click()
        except Exception:
            while True:
                self.swipe_screen.swipe_on('up')
                sleep(1)
                if self.driver.find_element(MobileBy.XPATH, f'{xpath_e}').click():
                    break
                else:
                    print('没有找到元素')


if __name__ == '__main__':
    run = ScrollThrough()
    run.scroll_through_by_xpath_click('')
