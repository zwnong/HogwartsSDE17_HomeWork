#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: swipe_screen.py
@time: 2021/3/5 23:16
"""


class SwipeScreen:
    def __init__(self, driver):
        self.driver = driver

    # 获取屏幕的宽高
    def get_size(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    # 向左边滑动
    def swipe_left(self):
        # [100,200]
        x1 = self.get_size()[0] / 10 * 9
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10
        self.driver.swipe(x1, y1, x, y1, 2000)

    # 向右边滑动
    def swipe_right(self):
        # [100,200]
        x1 = self.get_size()[0] / 10
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10 * 9
        self.driver.swipe(x1, y1, x, y1, 2000)

    # 向上滑动
    def swipe_up(self):
        # [100,200]direction
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10 * 9
        y = self.get_size()[1] / 10
        self.driver.swipe(x1, y1, x1, y, 1000)

    # 向下滑动
    def swipe_down(self):
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10
        y = self.get_size()[1] / 10 * 9
        self.driver.swipe(x1, y1, x1, y)

    def swipe_on(self, direction=None):
        if direction == 'up':
            self.swipe_up()
        elif direction == 'down':
            self.swipe_down()
        elif direction == 'left':
            self.swipe_left()
        else:
            self.swipe_right()
