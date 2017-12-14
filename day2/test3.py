# Author:pjf
# github=https://github.com/pengxuanlan/python
# time:2017-12-14 10:44

exit_set = False    # 状态标识
f = str(open("user", "r+", encoding="utf-8").read())   # 读取user文件
for line in f:
    file_str = str(f)    # 转换成文本
data = eval(file_str)   # 字符串转换成字典
name = input("请输入用户姓名：")
password = input("请输入用户密码：")
while True:
    if name in data:
        if password in data[name]:
            salay_yue = int(data[name][password]) # 读取用户表中的余额,转成数字格式
            print("登录成功，您的余额为：",salay_yue)
            break








