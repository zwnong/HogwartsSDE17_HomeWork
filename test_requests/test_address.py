#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: test_address.py
@time: 2021/3/25 21:35
"""
import requests


class TestAddress:
    def setup(self):
        # charles代理
        self.proxies = {
            "http": "http://127.0.0.1:8888",
            "https": "http://127.0.0.1:8888"
        }
        self.token = self.test_get_token()

    # 获取token
    def test_get_token(self):
        # 企业id
        corpid = "wwb636abb767a13836"
        # 应用的凭证密钥：权限说明 接口使用范围，比如，同步通讯录的接口必须要用通讯录同步助手的access_token
        corpsecret = "dKM7tQH5rCf_PgLMZlMEoz3Zv-v2I4RNeDpWB71XM3c"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(url)
        return r.json()['access_token']

    # 添加成员
    def test_add_mamber(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        data = {
            "userid": "li1314",
            "name": "Bruce Lee",
            "mobile": "+86 13800000000",
            "department": [1]
        }
        r = requests.post(url, json=data, proxies=self.proxies, verify=False)
        print(r.json())

    # 批量添加成员
    def test_batch_member(self):
        # 此方法一次只能添加9个 需要对mobile做处理
        for i in range(5):
            url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
            data = {
                "userid": f"range{i}",
                "name": f"批量{i}",
                "mobile": f"+86 1380000001{i}",
                "department": [1],
            }
            r = requests.post(url, json=data)
            print(r.json())
            i += 1

    # 读取一个成员信息
    def test_read_mamber(self):
        user_id = 'li1314'
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={user_id}"
        r = requests.get(url)

    # 更新成员信息
    def test_update_member(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}"
        data = {
            "userid": "li1314",
            "name": "李小龙",
            "mobile": "13800000000",
        }
        r = requests.post(url, json=data)
        print(r.json())

    # 删除一个部门成员
    def test_delete_member(self):
        user_id = 'li1314'
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={user_id}"
        r = requests.get(url)
        print(r.json())

    # 获取部门成员
    def test_get_department(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/simplelist?access_token={self.token}&department_id=1&fetch_child=0"
        r = requests.get(url)
        print(r.json())
