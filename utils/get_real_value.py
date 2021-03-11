# coding = utf-8
"""
@File     :  get_real_value.py
@project  :  
@Author   :  zwnong
@Time     :  2021/1/31  0:17
"""
from utils.get_file import GetFile


class GetRealValue:
    def __init__(self):
        self.get_real = GetFile()

    def get_add_real_value(self):
        return self.get_real.get_value('add')['datas']

    def get_ids_real_value(self):
        return self.get_real.get_value('add')['ids']

    def get_div_real_value(self):
        return self.get_real.get_value('div')['datas']

    # 测试是否获取操yaml数据
    def get_test(self):
        return self.get_real.get_value('test')['int']['datas']


if __name__ == '__main__':
    run = GetRealValue()
    print(run.get_test())
