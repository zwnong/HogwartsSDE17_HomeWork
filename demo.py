#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: demo.py
@time: 2021/3/25 0:32
"""

# t1 = (1, 2, [30, 40])
# t1[2].append(20)
# t1[2].insert(2, 50)
# t1[2].extend([60, 70])
# t1[2].sort()
# print(t1)
import time
from time import asctime

import yaml

# data = yaml.safe_load(open(r'E:\HogwartsSDE17_HomeWork\member_info_tb.yaml', 'r', encoding='utf-8'))
# value = data.get('addcontcts')
# print(value)

print(time.strftime("%Y%m%d_%H%M%S", time.localtime()))