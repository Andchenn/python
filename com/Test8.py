# 两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：

x = [
    [12, 7, 3],
    [4, 5, 6],
    [7, 8, 9],
]
y = [
    [5, 8, 1],
    [6, 7, 3],
    [4, 7, 3],
]
result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

# 迭代输入行
for i in range(len(x[0])):
    # 迭代输入列
    for j in range(len(x[0])):
        result[i][j] = x[i][j] + y[i][j]
for r in result:
    print(r)
