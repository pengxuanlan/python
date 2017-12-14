exit=False
f=open('user','r+',encoding="utf-8").read()
file=str(f)
for line in file:
    file_str=str(file)   #转成字符串
data=eval(file_str)   #转换成字典
name=input("请输入用户姓名：")
password=input("请输入密码：")
while True:
    if name in data:
        if password in data[name]:
            print("登录成功！")
            break

        else:
            print("密码错误，登录失败")
            continue
    else:
        print("您输入的用户名不存在，请重试")
        continue


