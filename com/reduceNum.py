# 将一个正整数分解质因数
from sys import stdout


n = int(input("请输入一个正整数： "))
for i in range(2, n + 1):
    while n != i:
        if n % i == 0:
            stdout.write(str(i))
            stdout.write("*")
            n = n // i
        else:
            break
print("%d" % n)
