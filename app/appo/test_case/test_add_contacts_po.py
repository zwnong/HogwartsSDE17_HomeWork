#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: test_add_contacts_po.py
@time: 2021/3/9 21:03
"""
from time import sleep

import pytest
from app.appo.page.app import App
from utils.get_file import GetFile


class TestAddContactsPo:
    info = GetFile(file_path=r'E:\HogwartsSDE17_HomeWork\config\info.yaml')

    def setup_class(self):
        self.driver = App().start_android_driver()
        self.add = self.driver.goto_main_page().click_address_list().click_add_members().goto_full_edit_page()

    def teardown_class(self):
        self.driver.stop_android_driver()

    @pytest.mark.parametrize(["name", "phone_numb", "e_mail"], info.get_value("addcontcts"))
    def test_add_contacts(self, name, phone_numb, e_mail):
        self.add.edit_name(name)
        self.add.edit_phone(phone_numb)
        self.add.edit_email(e_mail)
        self.add.click_save_and_continue_adding()
        sleep(2)
        self.add.verify_add_member_ok('添加成功')
        # TypeError: argument of type 'method' is not iterableTypeError:
        # 类型'method'的参数是不可迭代的，因为添加了多个成员所有会多次获取page_source,待解决
        sleep(3)
