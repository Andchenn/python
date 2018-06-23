# 打印出杨辉三角形(要求打印出10行)

if __name__ == '__main__':
    a = []
    for i in range(10):
        a.append([])
        for j in range(10):
            a[i].append(0)
    for i in range(10):
        # 最左端都为1
        a[i][0] = 1
        # 最右端都为1
        a[i][i] = 1
    for i in range(2, 10):
        for j in range(1, i):
            a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
    from sys import stdout

    for i in range(10):
        for j in range(i + 1):
            stdout.write(str(a[i][j]))
            stdout.write(' ')
        print()