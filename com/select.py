# 选择排序

s = [5, 3, 2, 4, 1, 0]
# 循环次数
for i in range(len(s) - 1):
    # 这是下标，不是元素值
    min_index = i
    for j in range(i + 1, len(s)):
        if s[min_index] > s[j]:
            # 记录最小元素的下标
            min_index = j
    s[i], s[min_index] = s[min_index], s[i]
    print('第%s次循环' % (i + 1), s)
print('排序后： ', s)
