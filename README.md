## 项目介绍
hogwarts学习笔记

- [个人python笔记](https://github.com/zwnong/Python.git)

- [hogwarts作业地址](https://github.com/zwnong/HogwartsSDE17_zwnong.git)

- ## git：[配置和常用命令](https://ceshiren.com/t/topic/7405)
        
- ## GitHub
    是一个托管平台
    
## pycharm配置git
    提交代码步骤： 代码-本地git仓库-提交到远程的仓库（github）
    - 环境搭建 官网下载 傻瓜式安装
    - 创建本地git仓库：在项目根目录输入git init 初始化一个git仓库
        ->在本地创建了一个.git目录（隐藏目录）
        ->执行git后该文件夹就被git管理的仓库
    - 点击右上角Git：✔展示Commit Changslist选择add to ,gitignore忽略掉.env（因为不需要上传项目环境）
    - 添加信息  点击commit上传到本地git仓库
    - 本地git与GitHub关联： VCS -> Git ->Git Remotes 输入github地址
    - VCS -> Git -> push...
## pytest安装配置
    - pip install -u pytest
    - settings-> Default test renner:选择pytest 如果有一个黄色的！ 点击fix安装
## 通过命令行运行pytest
