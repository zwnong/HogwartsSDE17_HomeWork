#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: base.py
@time: 2021/3/31 22:40
"""
import sys

sys.path.append('..')
import requests
import yaml


class Base:
    def __init__(self):
        # 声明session
        # self.s替换掉requests.方法
        self.s = requests.Session()
        self.token = self.get_token()
        self.s.params = {"access_token": self.token}

    def get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        # 企业id: corpid
        # 应用的凭证密钥：corpsecret 权限说明 接口使用范围，比如，同步通讯录的接口必须要用通讯录同步助手的access_token
        params = {"corpid": "wwb636abb767a13836",
                  "corpsecret": "dKM7tQH5rCf_PgLMZlMEoz3Zv-v2I4RNeDpWB71XM3c"
                  }
        r = self.s.get(url, params=params)
        return r.json()['access_token']

    def yaml_data(self):
        data = yaml.safe_load(open(r'../test_case/member_info_tb.yaml', 'r', encoding='utf-8'))
        return data

    def get_yaml_userid(self):
        lists = self.yaml_data()["member_info"]
        userid_list = []
        with open('../test_case/user.yaml', 'w', encoding='utf-8') as f:
            for j in lists:
                f.write(str(f'{j[1]},'))
        print(userid_list)

    def send(self, *args, **kwargs):
        """
        request是get() post()等 的底层
        比如 get（）底层代码:
             def get(self, url, **kwargs):
                kwargs.setdefault('allow_redirects', True)
                return self.request('GET', url, **kwargs)

        # 所以 使用request的时候 如果是get请求 request('GET', url, **kwargs) 即第一个参数填写上GET
        # post请求同理 更多参数看底层代码
        # 这样
        :param args:
        :param kwargs:
        :return:
        """
        return self.s.request(*args, **kwargs)


if __name__ == '__main__':
    run = Base()
    print(type(run.get_yaml_userid()))

