# Author:pjf
# github=https://github.com/pengxuanlan/python
# time:2017-12-15 9:00
# file = open("info.txt","r+",encoding="utf-8")

exit_set = False
msg = '''   # 定义菜单项
1. 查询员工工资
2. 修改员工工资
3. 增加新员工记录
4. 退出
'''
file_r = open("info.txt", "r", encoding="utf-8")  # 读取文件
lines = file_r.readlines()
while not exit_set:
    print(msg)
    choose = input("请输入需要使用的功能：")
    if choose == '1':    # 查询工资

        username = input("请输入查询姓名：")
        for i in lines:
            (user,salay) = i.strip('\n').split()
            if username == user:
                print("%s的工资为:\033[34;1m%s\33[0m" % (username,salay))
                pass
    elif choose == '2':    # 修改员工工资
        user_old = input("请输入员工姓名：").strip()
        for i in lines:
            file = i.strip().split()
            if user_old in file:
                salay_old = file[1]   # 把旧工资取出来
                user_new, salay_new = input("请输入新的员工姓名和工资，用空格分离:").strip().split()
                file_user = open("info.txt", "w", encoding="utf-8")
                for line in lines:
                    if user_old in line:
                        line = line.replace(user_old, user_new)  # 先改名称

                    file_user.write(line)
                file_user.close()
                file_r.close()
                file_r = open("info.txt", "r", encoding="utf-8")  # 重新读取文件
                lines = file_r.readlines()
                file_salay = open("info.txt", "w", encoding="utf-8")   #重新读取文件
                for line in lines:
                    if user_new in line:
                        line = line.replace(salay_old, salay_new)  # 修改工资
                    file_salay.write(line)   # 写入文件
                file_salay.close()  #关闭文件
                file_r.close()
                print("修改成功")
    elif choose == '3':
        file_r = open("info.txt", "r+", encoding="utf-8")  # 追加方式打开方便写入
        lines = file_r.readlines()
        file_list=[]
        for i in lines:
            file = i.strip().split()
            file_list.append(file[0])
        user_new_info = input("请输入新员工的名称和工资，以空格分开：")
        user_x, salay_x=user_new_info.strip().split()
        if user_x in file_list:
            print("用户名已经存在，无法添加")
        else:
            file_r.write(user_new_info+"\n") # 添加换行符
            print("恭喜你，用户 %s 添加成功" % user_x)
            file_r.close()
    elif choose == '4':
        print("再见！")
        exit_set =True
    else:
        print("无效输入，请重新输入")





















