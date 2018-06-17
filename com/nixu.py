# 将一个数逆序输出。

if __name__ == '__main__':
    a = [9, 6, 5, 4, 1]
    print('输出a列表的数：')
    for u in range(len(a)):
        print(a[u])
    print('逆序得到的数：')
    for i in reversed(a):
        print(i)
