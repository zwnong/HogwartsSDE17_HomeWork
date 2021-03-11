#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: server.py
@time: 2021/2/27 21:48
"""
from utils.dos_cmd import DosCmd


class Server:
    def __init__(self):
        self.dos = DosCmd()

    def kill_node_server(self):
        """
        查找：tasklist | find "node.exe"
        杀进程：taskkill -F -PID node.exe
        :return:
        """
        # 查找结果列表
        server_list = self.dos.excute_cmd_result('tasklist | find "node.exe"')
        if len(server_list) > 0:
            self.dos.excute_cmd('taskkill -F -PID node.exe')

    def kill_chrome_server(self):
        """
        查找：tasklist | find "chrome.exe"
        杀进程：taskkill -F -PID chrome.exe
        :return:
        """
        # 查找结果列表
        server_list = self.dos.excute_cmd_result('tasklist | find "chrome.exe"')
        if len(server_list) > 0:
            self.dos.excute_cmd('taskkill -F -PID chrome.exe')


if __name__ == '__main__':
    run = Server()
    run.kill_chrome_server()
