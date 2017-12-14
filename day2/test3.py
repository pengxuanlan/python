# Author:pjf
# github=https://github.com/pengxuanlan/python
# time:2017-12-14 10:44

exit_set = False    # 状态标识
file = open("user", "r+", encoding="utf-8")   # 读取user文件
f=str(file.read())
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
        else:
            print("密码错误，请重新输入密码")
            password = input("请输入输入密码:")
            continue
    else:
        password_salay = {}
        salay_str = input("首次登录，请输入您的工资：")   # 首次登录，输入工资
        salay = int(salay_str)  # 输入的工资转化成数字格式
        password_salay[password] = salay  # 把工资写入字典
        data[name] = password_salay  # 把名称写入字典
        file.seek(0)  # 移动文件首
        file.write(str(data))  # 追加写入
        file.tell()
        print("注册成功，当前余额为：",password_salay)
        break






