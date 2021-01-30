## 项目介绍
hogwarts学习笔记

- [个人python笔记](https://github.com/zwnong/Python.git)

- [hogwarts作业地址](https://github.com/zwnong/HogwartsSDE17_zwnong.git)

- ### Git：[配置和常用命令](https://ceshiren.com/t/topic/7405)
        
- ### GitHub
    是一个托管平台
    
### pycharm配置git
    提交代码步骤： 代码-本地git仓库-提交到远程的仓库（github）
    - 环境搭建 官网下载 傻瓜式安装
    - 创建本地git仓库：在项目根目录输入git init 初始化一个git仓库
        ->在本地创建了一个.git目录（隐藏目录）
        ->执行git后该文件夹就被git管理的仓库
    - 点击右上角Git：✔展示Commit Changslist选择add to ,gitignore忽略掉.env（因为不需要上传项目环境）
    - 添加信息  点击commit上传到本地git仓库
    - 本地git与GitHub关联： VCS -> Git ->Git Remotes 输入github地址
    - VCS -> Git -> push...
### pytest安装配置
    - pip install -u pytest
    - settings-> Default test renner:选择pytest 如果有一个黄色的！ 点击fix安装
### 通过命令行运行pytest
    - 查看pytest命令：pytest --help
    - pytest test_xxx.py
    - 显示详细信息：pytest test_xxx.py -vs
    - 只收集用例而不去执行：pytest --collect-only 用处：在设计框架设计封装哪些用例需要执行哪些需要过滤
    - 匹配用例包含xxx的用例：pytest -k "xxx"
    - 标签用法：
        在用例中加上标签之后:@pytest.mark.xxx  xxx表示可以用自带的标签也可以用自己定义的标签 比如login 表示登录的标签
             配置可以识别的自定以的标签  定义pytest.ini
                [pytest]
                markers = login
                        search
        就可以使用以下命令运行某一些特定的测试用例
            pytest -m "login"
    
### 警告捕获
    -从3.1版开始，pytest现在会在测试执行期间自动捕捉警告，并在会话结束时显示它们
    - -W标志可以用来控制哪些警告将被显示，甚至将它们转换为错误
       在pytest.ini配置
            [pytest]
            addopts = -p no:warnings
       捕获完全禁用警告 或者在命令行中传递-p no:warnings
       pytest -q test_show_warnings.py -W error::UserWarning
    - @pytest.mark.filterwarnings
        -使用@pytest.mark。filterwarnings将警告过滤器添加到特定的测试项，控制哪些警告应该在测试、类甚至模块级别捕获

