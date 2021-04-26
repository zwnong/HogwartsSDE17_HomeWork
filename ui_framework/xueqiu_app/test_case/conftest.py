#!/user/bin/env
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: app_record.py
@time: 2021/4/19 21:59
实现录屏工具：scrcpy（第三方录屏方式），对Windows不太友好
下载安装：github.com/Genymobile/scrcpy
    配置环境变量
使用：直接链接手机 输入scrcpy   scrcpy --help 查看相关用法
以后要把这个录屏用到 插件机制里 pytest plugin 插件机制  加载机制
"""
# conftest.py是pytest的一个配置文件 里面配置的东西都会被pytest察觉到
import os
import subprocess
import signal
import sys

from utils.logger import log_init

sys.path.append('..')
import pytest


@pytest.fixture(scope="module", autouse=True)  # scope="module"模块级别 autouse=True主动的运行
def record():
    """
    # 期望：在测试用例执行的时候进行录屏 用例结束后停止
    :return:
    """
    # 用例运行前
    log_init()
    cmd = "scrcpy -Nr result/record/record.mp4"
    p = subprocess.Popen(cmd, shell=True)
    yield  # fixture的一个特点 分割用例运行前后
    # 用例运行后
    os.kill(p.pid, signal.CTRL_C_EVENT)  # Ctrl+c 不能直接使用 要给指定pid，不然可能会kill掉其他服务
