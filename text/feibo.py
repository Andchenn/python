# python 斐波那契数列实现
# 获取用户输入数据
t = int(input("你需要几项？"))
# 第一和第二
n1 = 0
n2 = 1
count = 2
# 判断输入的值是否合法
if t <= 0:
    print("请输入一个正整数")
elif t == 1:
    print("斐波那契数列：")
    print(n1)
else:
    print("斐波那契数列：")
    print(n1, ",", n2, end=", ")
    while count < t:
        n = n1 + n2
        print(n, end=", ")
        # 更新值
        n1 = n2
        n2 = n
        count += 1
