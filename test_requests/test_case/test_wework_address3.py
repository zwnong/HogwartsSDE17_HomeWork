#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: test_wework_address3.py
@time: 2021/3/28 20:39
在做数据处理的时候 需要先做数据前的清理（必要）
不必花大量时间在数据清理上，列举出常见的当前的影响数据处理的操作
未来如果再遇到影响，再去添加清理操作，不必把整个项目所有的点（需要清理的操作）都想明白 浪费时间
测试完成之后要恢复数据
"""
from test_requests.wework.wework_address2 import WeworkAddress2


# 原始基础case
class TestWeworkAddress:
    def setup_class(self):
        self.address = WeworkAddress2()
        self.user_id = "li1234"
        self.name = "李小龙"
        self.mobile = "15236487542"
        self.department = [1]

    def setup(self):
        # 数据处理 1、通过已有接口创造、操作数据 2、直接操作数据库（有权限）
        self.address.delete_member(self.user_id)  # 删除成员 如果成员不存在 只会返回错误码，不对需求（测试结果）参数影响

    def teardown(self):
        # 数据恢复（测试前的状态）因为已经调用创建成员的接口创建了成员 所有需要删除创建的成员
        self.address.delete_member(self.user_id)

    def test_get_info(self):
        # 测试用户信息是否存在使用返回的errcode判定 如果是判定用户信息是否正确？
        # 明确用户的角度 功能的角度 保证用户已经存在
        # 解决： 创建此用户 首先要做数据清理 比如 改用户已经存在

        self.address.add_member(self.user_id, self.name, self.mobile,
                                self.department)  # 添加用户 如果成员存在 只会返回错误码，不对需求（测试结果）参数影响
        r = self.address.get_info(self.user_id)
        assert r["name"] == self.name

    def test_add_member(self):
        # 如果创建的成员/手机号 已经存在，那么就会创建失败，所有需要做数据处理
        # 判断errmsg是否是create 但只能判定接口调用成功，并不能判定成员被创建
        r = self.address.add_member(self.user_id, self.name, self.mobile, self.department)
        assert r["errmsg"] == "created"
        # 方案1 查询数据库（这里做一个假的数据库信息）断言
        info = self.address.get_info(self.user_id)
        assert info["name"] == self.name

    def test_update_member(self):
        new_name = "李小龙_update"
        self.address.add_member(self.user_id, self.name, self.mobile, self.department)
        r = self.address.update_member(self.user_id, new_name)
        assert r["errmsg"] == "updated"
        info = self.address.get_info(self.user_id)
        assert info["name"] == new_name

    def test_del_member(self):
        self.address.add_member(self.user_id, self.name, self.mobile, self.department)
        r = self.address.delete_member(self.user_id)
        assert r["errmsg"] == "deleted"
        info = self.address.get_info(self.user_id)
        assert info["errcode"] == 60111
