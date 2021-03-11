#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: test_register.py
@time: 2021/3/1 22:46
"""
from time import sleep

from web.login_page import MainPage


class TestRegister:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        self.main.driver_quite()

    def test_register_from_login(self):
        self.main.goto_login().goto_register()
        sleep(6)

    def test_register(self):
        self.main.goto_register().send_company_name_keys()
        self.main.goto_register().register()
        sleep(6)
