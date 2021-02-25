#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: get_cookie.py
@time: 2021/2/25 22:03
"""
import json
from time import sleep

from selenium import webdriver


class GetCookies:
    def __init__(self):
        self.driver = webdriver.Chrome(r"D:\Google\Chrome\Application/chromedriver.exe")
        self.driver.implicitly_wait(5)

    def get_save_cookies_to_file(self, url):
        """
        # 传入需要获取cookis并保存到文件
        :param url:
        :return:
        """
        self.driver.get(url)
        with open('cookies.txt', 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.driver.get_cookies()))
            sleep(5)
        self.driver.quit()


if __name__ == '__main__':
    run = GetCookies()
    run.get_save_cookies_to_file('https://work.weixin.qq.com/')
