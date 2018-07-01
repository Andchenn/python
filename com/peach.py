# 海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为5份，多出了一个，这只猴子把多的
# 一个扔入大海中，拿走了一份。第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的扔
# 入海中，拿走了一份，第三第四第五只猴子都这样做的，问海滩上原来最少有多少个桃子？

if __name__ == '__main__':
    i = 0
    j = 1
    x = 0
    while i < 5:
        x = 4 * j
        for i in range(0, 5):
            if x % 4 != 0:
                break
            else:
                i += 1
            x = (x / 4) * 5 + 1
        j += 1
    print(x)

# 方法二
num = int(input("输入猴子的数目："))


def fn(n):
    if n == num:
        # 最后剩的桃子的数目
        return 4 * x
    else:
        return fn(n + 1) * 5 / 4 + 1


x = 1
while 1:
    count = 0
    for i in range(1, num):
        if fn(i) % 4 == 0:
            count = count + 1
    if count == num - 1:
        print("海滩上原来最少有%d个桃子" % int(fn(0)))
        break
    else:
        x += 1

# 方法三
start, end, m1 = 0, 100, 0
while m1 == 0:
    end = end * 2
    for i in range(start, end):
        m5 = 5 * i + 1
        if m5 % 4 == 0:
            m4 = (m5 / 4) * 5 + 1
            if m4 % 4 == 0:
                m3 = (m4 / 4) * 5 + 1
                if m3 % 4 == 0:
                    m2 = (m3 / 4) * 5 + 1
                    if m2 % 4 == 0:
                        m1 = (m2 / 4) * 5 + 1
                        break
    start = i
print("最少为：%d个桃子" % m1)
