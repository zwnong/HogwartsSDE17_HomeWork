#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: get_tost.py
@time: 2021/3/9 17:37
"""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class GetTosts:
    def __init__(self, driver):
        self.driver = driver

    def tost_in_dom(self, text):
        tost_element = ('xpath', f'//*[contains(@text, "{text}")]')
        # 判断元素是否加载到了dom树
        print(WebDriverWait(self.driver, 10, 0.2).until(EC.presence_of_element_located(tost_element)))

    def get_tost_text_in_dom(self):
        pagesource = self.driver.page_source
        return pagesource
