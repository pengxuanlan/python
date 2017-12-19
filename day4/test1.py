num=0   # 定义求和的初始值
for i in range(1,101):
    if i%2 ==0:  # 使用取模运算计算单双
        num=num-i  # 如果是双数
    else:
        num=num+i   # 单数则加
print(num)