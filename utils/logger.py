#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: logger.py
@time: 2021/4/26 12:15
python 的logging 没有任何功能  需要添加功能（句柄）
如果需要将文件输出到文件 就需要声明输出到文件的句柄
如果要输出到终端（terminal）,那就声明输出到终端的句柄
添加不同的句柄 然后把句柄添加到logging
"""
import logging
import logging.handlers
import time


def log_init():
    # 设置格式
    log_format_str = '[%(asctime)s]  %(filename)s:%(lineno)d:%(funcName)s: %(message)s'

    format_str = logging.Formatter(log_format_str)

    # 根据 log 标识获取 log

    root = logging.getLogger("my_log")

    # 加入输出到文件的句柄
    t = time.strftime("%Y%m%d_%H%M%S", time.localtime())
    h = logging.handlers.RotatingFileHandler(f"./result/log/{t}.log", mode='a', encoding="utf-8")

    h.setFormatter(format_str)

    # 加入输出到控制台的句柄

    s = logging.StreamHandler()

    s.setFormatter(format_str)

    # 将句柄添加到loging中
    root.addHandler(h)

    root.addHandler(s)

    # 设置log等级
    root.setLevel(logging.DEBUG)


log = logging.getLogger("my_log")
