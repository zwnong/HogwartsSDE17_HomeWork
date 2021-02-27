#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: file_operations.py
@time: 2021/2/28 0:32
"""
import json
from time import sleep
from selenium import webdriver


class FileOperation:
    def __init__(self):
        pass
        # self.chrome_arg = webdriver.ChromeOptions()
        # self.chrome_arg.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(r'D:\Google\Chrome\Application\chromedriver.exe', options=self.chrome_arg)
        # self.driver.implicitly_wait(5)

    def save_cookies_from_selenium_way(self, url):
        """
        # 传入需要获取cookies的url并保存到文件
        :param url:
        :return:
        """
        self.driver = webdriver.Chrome(r"D:\Google\Chrome\Application/chromedriver.exe", url)
        cookies = self.driver.get_cookies()
        with open('cookies.txt', 'w', encoding='utf-8') as f:
            f.write(json.dumps(cookies))
            # 也可以使用json序列化存储
            # json.dump(cookies, f)
            sleep(10)
        self.driver.quit()

    # def read_cookies(self):
    #     with open('cookies.txt', 'r', encoding='utf-8') as fr:
    #         cookies = json.load(fr)
    #     print(cookies)


# if __name__ == '__main__':
#     run = FileOperation()
#     # run.save_cookies_from_selenium_way('https://work.weixin.qq.com/')
#     run.save_cookies_from_selenium_way('https://work.weixin.qq.com/wework_admin/frame')
#     run.read_cookies()
