#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: base_page.py
@time: 2021/3/9 21:52
"""
import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from ui_framework.decorator.handle_black_list import handle_black
from utils.logger import log


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    @handle_black
    def find(self, locator, element):
        """
        重构查找元素
        :param locator: 定位方式
        :param element: 元素信息
        :return:
        """
        log.debug('find' + element)
        return self.driver.find_element(locator, element)
        # black_list = ['//android.widget.TextView[@resource-id="com.xueqiu.android:id/tv_agree" and @text="同意"]',
        #               '//android.widget.TextView[@resource-id="com.xueqiu.android:id/tv_left" and @text="取消"]']
        # try:
        #     return self.driver.find_element(locator, element)
        # except Exception:
        #         for i in black_list:
        #             ele_path = self.finds(locator, i)
        #             if len(ele_path) > 0:
        #                 ele_path[0].click()
        #         return self.find(locator, element)
        # black_list = ['//android.widget.TextView[@resource-id="com.xueqiu.android:id/tv_agree" and @text="同意"]',
        #               '//android.widget.TextView[@resource-id="com.xueqiu.android:id/tv_left" and @text="取消"]']
        # try:
        #     return self.driver.find_element(locator, element)
        # except Exception:
        #     for i in black_list:
        #         ele_path = self.finds(locator, i)
        #         if len(ele_path) > 0:
        #             ele_path[0].click()
        #             return self.find(locator, element)

    def find_and_click(self, locator, element):
        """
        重构查找元素并点击
        :param locator: 定位方式
        :param element: 元素信息
        :return:
        """
        self.find(locator, element).click()

    def find_and_sendkeys(self, locator, element, value):
        return self.find(locator, element).send_keys(value)

    def finds(self, locator, value):
        return self.driver.find_elements(locator, value)

    def web_driver_wait(self, locator, value):
        return WebDriverWait(self.driver, 10, 0.1).until(lambda x: x.find_element(locator, value))

    def verify_add_member_ok(self):
        assert '添加成功' in self.driver.page_source()

    def verify_del_member_ok(self):
        assert '' in self.driver.page_source()

    # def get_yaml_data(self, file_path=None, value=None):
    #     if file_path is None:
    #         self.file_path = r'../config\data.yaml'
    #     else:
    #         self.file_path = file_path
    #     data = yaml.safe_load(open(str(self.file_path), 'r', encoding='utf-8'))
    #     try:
    #         value = data.get()
    #     except EOFError:
    #         value = None
    #     return value

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
        self.driver.swipe(x1, y1, x1, y, 1000)

    def swipe_on(self, direction=None):
        if direction == 'up':
            self.swipe_up()
        elif direction == 'down':
            self.swipe_down()
        elif direction == 'left':
            self.swipe_left()
        else:
            self.swipe_right()

    def swipe_find(self, expression, num=3):
        """
        # 上下滑动查找元素
        :param expression: 滑动页数，默认为3页
        :param num:
        :return:
        """
        for i in range(num):
            if i == num - 1:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f'滑动{num}次，没找到元素')

            self.driver.implicitly_wait(1)
            try:
                element = self.driver.find_element(MobileBy.XPATH, expression)
                self.driver.implicitly_wait(5)
                return element
            except Exception:
                self.swipe_up()

    def parse(self, yaml_path, fun_name):
        """
        # 解析关键字 解析yaml文件并调用相应的方法 实现相应功能
        :param yaml_path: yaml文件路径
        :param fun_name: yaml文件定义的方法名
        :return:
        """
        with open(yaml_path, 'r', encoding='utf-8') as f:
            functance = yaml.load(f)
        steps = functance.get(fun_name)
        for step in steps:
            if step.get('action') == 'find_and_click':
                self.find_and_click(step.get('locator'), step.get('element'))
            elif step.get('action') == 'find_and_sendkeys':
                self.find_and_sendkeys(step.get('locator'), step.get('element'), step.get('contents'))

    def screenshot(self):
        return self.driver.get_screenshot_as_png()
