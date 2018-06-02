# 9*9乘法口诀表(顺序)
# i表示行数
for i in range(1, 10):
    # j表示列数
    for j in range(1, i + 1):
        print(str(j) + '*' + str(i) + "=" + str(j * i), end="\t")
    print()

print("\n")

# 9*9乘法口诀表(倒序)
for i in range(9, 0, -1):
    for j in range(i, 0, -1):
        print(str(j) + "*" + str(i) + "=" + str(j * i), end="\t")
    print()
