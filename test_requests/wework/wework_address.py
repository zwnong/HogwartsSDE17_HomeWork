#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: wework_address.py
@time: 2021/3/28 20:34
"""
# 基础封装好的接口方法
import yaml

from test_requests.wework.base import Base


class WeworkAddress(Base):
    def add_member(self, userid: str, name: str, phone: str, department: list):
        """
        添加成员
        :param userid:
        :param name:
        :param phone: 手机必须是11位
        :param department:
        :return:
        """
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/create"
        params = {
            "access_token": self.token
        }
        data = {
            "userid": userid,
            "name": name,
            "mobile": f"+86 {phone}",
            "department": department
        }
        r = self.send('POST', url, json=data, params=params)
        return r.json()

    def delete_member(self, userid):
        """
        删除成员
        :return:
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?userid={userid}"
        r = self.send('GET', url)
        return r.json()

    def delete_member2(self):
        """
        删除成员
        :return:
        """
        userid_list = yaml.safe_load(open(r'../test_case/user.yaml', 'r', encoding='utf-8'))
        print(list(userid_list.split(',')))
        for userid in list(userid_list.split(',')):
            url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?userid={userid}"
            r = self.send('GET', url)
            print(r.json())

    def update_member(self, userid: str, name: str = None, mobile: str = None):
        """
        修改成员
        :return:
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update"
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
        }
        r = self.send('GET', url, json=data)
        return r.json()

    def get_info(self, userid):
        """
        查看成员
        :return:
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?userid={userid}"
        r = self.send('GET', url)
        return r.json()


if __name__ == '__main__':
    r = WeworkAddress()
    r.delete_member2()
