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
while name.strip() == '':    # 判断用户名是否为空，如果为空就要求用户输入
    print("用户名不能为空，请重新输入！")
    name = input("请输入用户姓名:")
    continue
password = input("请输入用户密码：")
while True:
    if name in data:
        if password in data[name]:
            salay = int(data[name][password]) # 读取用户表中的余额,转成数字格式
            print("登录成功，您的余额为：",salay)
            break
        else:
            print("密码错误，请重新输入密码")
            password = input("请输入输入密码:")
            continue
    else:
        password_salay = {}   # 定义空字典
        salay_str = input("首次登录，请输入您的工资：")   # 首次登录，输入工资
        salay = int(salay_str)  # 输入的工资转化成数字格式

        password_salay[password] = salay  # 把工资写入字典
        data[name] = password_salay  # 把名称写入字典
        file.seek(0)  # 移动文件首
        file.write(str(data))  # 追加写入
        file.tell()
        print("注册成功，当前余额为：",password_salay)
        break
list_spqd = [    # 商品清单
    ["iphone7", 7088],
    ["小米6", 2499],
    ["华为M10", 5088],
    ["ipad pro", 4388],
    ["一加5T", 3499],
    ["三星S8", 5288]
]
file_list = open("shopping", "r+", encoding="utf-8")  # 读取历史清单
f_file_list = str(file_list.read())   # 转化成字符串
shopping_list = eval(f_file_list)
if name not in shopping_list:
    shopping_list[name] = []   # 定义空列表
shopping_list_ls = shopping_list[name]  # 如果不是首次登录则把历史记录加载进来
shopping_list_now = []  # 清空本次记录
choose = input("是否需要打印购物清单？（Y/N）:")
if choose == 'y':
    print("--------历史清单--------")
    print(shopping_list_ls)
    print("---------结束-----------")
while not exit_set:   # 此处开始购物
    for index,item in enumerate(list_spqd,1):   # 遍历列表，并且指定索引从1开始
        print(index,item)   # 循环打印商品清单


    num = input("请输入想购买的商品编号：")

    if num == 'q':
        exit_set = True
        data[name][password] = str(salay)
        file.seek(0)
        file.write(str(data))
        file.tell()
        print("购物清单如下：")
        print(shopping_list_now)
        print("您的余额为：", salay)
        shopping_list_ls.extend(shopping_list_now)
        shopping_list[name] = shopping_list_ls
        file_list.seek(0)
        file_list.write(str(shopping_list_ls))
        file_list.tell()
    elif num.isdigit()== False:   # 判断输入是否为整数
        print("输入错误！请输入整数")   # 转换成数值
    elif int(num)>int(len(list_spqd)) or int(num) <=0:
        print("输入错误，超出商品列表范围")

    else:
        num_buy = int(num)-1
        if list_spqd[num_buy][1] < (salay):
            salay = salay-int(list_spqd[num_buy][1])
            print("商品",list_spqd[num_buy][0],"加入购物车成功！余额为:",salay)
            shopping_list_now.append(list_spqd[num_buy])
        else:
            print("余额不足")






















