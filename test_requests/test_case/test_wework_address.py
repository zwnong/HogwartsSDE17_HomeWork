#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: test_wework_address.py
@time: 2021/3/31 23:19
"""
import pytest
import yaml
from test_requests.wework.wework_address import WeworkAddress


class TestWeworkAddress:
    data = yaml.safe_load(open(r'./member_info_tb.yaml', 'r', encoding='utf-8'))

    def setup_class(self):
        self.address = WeworkAddress()

    def teardown_class(self):
        # 恢复数据
        self.address.delete_member2()

    @pytest.mark.parametrize(["userid", "name", "mobile", "department"], data.get('member_info'))
    def test_add_member(self, userid, name, mobile, department):
        # 参数化 批量添加成员
        # 如果创建的成员/手机号 已经存在，那么就会创建失败，所有需要做数据处理
        # 判断errmsg是否是create 但只能判定接口调用成功，并不能判定成员被创建
        self.address.delete_member(userid)  # 数据清理
        r = self.address.add_member(userid, name, mobile, department)
        assert r["errmsg"] == "created"
        # 方案1 查询数据库（这里做一个假的数据库信息）断言
        info = self.address.get_info(userid)
        assert info["name"] == name
