#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: handle_black_list.py
@time: 2021/3/16 18:06
"""
from appium.webdriver.common.mobileby import MobileBy


def handle_black(fun):
    def run(*args, **kwargs):
        """
        # fun-->需要装饰的函数名
        # *arg fun()函数的参数  **kwargs 字典型参数
        :param args:
        :param kwargs:
        :return:
        """
        black_list = ['//android.widget.TextView[@resource-id="com.xueqiu.android:id/tv_agree" and @text="同意"]',
                      '//android.widget.TextView[@resource-id="com.xueqiu.android:id/tv_left" and @text="取消"]']
        # 相当于self
        instance = args[0]
        try:
            return fun(*args, **kwargs)
        except Exception:
            for i in black_list:
                ele_path = instance.finds(MobileBy.XPATH, i)
                if len(ele_path) > 0:
                    ele_path[0].click()
            return fun(*args, **kwargs)

    return run
