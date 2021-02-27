# 企业微信的自动化的登录

- ##selenium
    - ###三剑客 
      selenium webdriver 编程语言驱动
      selenium IDE 插件
      selenium Grid 分布式工具
      
- ### 复用已有的浏览器
  等同于webdriver.Chrome()添加options参数，且options=chrome_arg（webdriver.ChromeOptions()）
  先打开复用功能-->把浏览器打开一个调式口子（打开一个chrome，设置远程地址chrome --remote-debugging-port=9222）
  - 1、cmd打开这个chrome --remote-debugging-port=9222命令之后，会自动打开浏览器
  - 2、只需要将需要复用的操作（登录）操作一遍
      #### 不要手动关闭该浏览器 ，如果关闭了，
    需要使用命令chrome --remote-debugging-port=9222再将浏览器打开 操作
    
            -1、先手动的登录需要复用的页面，再关闭所有的chrome（必须）
            -2、chrome -remote-debugging-port 127.0.0.1:9333
            -3、在代码中使用：
                chrome_arg = webdriver.ChromeOptions()
                chrome_arg.debuger_address = '127.0.0.1"9333'
                self.driver = webdriver.Chrome(options = chrome_arg)
  
- ### cookie登录
    cookie相当与身份信息，再请求数据的时候携带cookie
        作用：维持会话
            使用：
            
            -driver.get(url)
            -driver.delete_all_cookies()
            -for cookie in cookies:
                driver.add_cookie(cookie)
                driver.refresh()
    
        获取cookie（一定要拿到登录后的cookie信息）：
            
            -1 浏览器调试工具查找
            -2 self.driver.get_cookies() # 列表 
            -3 将获取到的cookie转化成字符串 jion.dumps(cookies)
            -4 存到本地文件
            -5 读取本地cookies.text文件
            -6 因为读取出来是列表 含有多个字典 而driver.add cookie()规则是传入一个字典 所有需要for遍历传入