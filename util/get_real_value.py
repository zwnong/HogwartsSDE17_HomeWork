# coding = utf-8
"""
@File     :  get_real_value.py
@project  :  
@Author   :  zwnong
@Time     :  2021/1/31  0:17
"""
from util.get_file import GetFile


class GetRealValue:
    def __init__(self):
        self.get_real = GetFile()

    def get_add_real_value(self):
        return self.get_real.get_value('add')['datas']

    def get_div_real_value(self):
        return self.get_real.get_value('div')['datas']

    def get_ids_real_value(self):
        return self.get_real.get_value('add')['ids']


if __name__ == '__main__':
    run = GetRealValue()
    print(run.get_div_real_value())
