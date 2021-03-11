#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: test_del_contacts.py
@time: 2021/3/10 21:28
"""
from time import sleep

from app.appo.page.app import App


class TestDelContacts:
    def setup_class(self):
        name = '小明'
        self.app = App().start_android_driver()
        self.run = self.app.goto_main_page().click_address_list().click_search_member().edit_search(name)\
            .click_first_name(name).click_more_info_page().click_edit_member()

    def teardown_class(self):
        self.app.stop_android_driver()

    def test_del_member(self):
        self.run.click_del_member()
        self.run.click_sure()
        sleep(3)
