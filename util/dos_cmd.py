# coding utf-8

import os


class DosCmd:

    # 获取设备信息
    def excute_cmd_result(self, command):
        result = os.popen(command).readlines()
        result_list = []
        for i in result:
            if i == '\n':
                continue
            result_list.append(i.strip('\n'))
        return result_list

    # 仅运行命令不获取结果
    def excute_cmd(self, command):
        os.system(command)


if __name__ == '__main__':
    re = DosCmd()
    print(re.excute_cmd('appium -p 4723 -bp 4726 -U 127.0.0.1:4723 --no-reset --session-override'))
