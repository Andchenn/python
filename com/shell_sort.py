# 希尔排序

def shell_sort(a):
    n = len(a)
    # gap是长度的一半
    gap = n // 2
    while gap >= 1:
        for j in range(gap, n):
            i = j
            while (i - gap) >= 0:
                if a[i] < a[i - gap]:
                    a[i], a[i - gap] = a[i - gap], a[i]
                    i -= gap
                else:
                    break
        # gad每次减半
        gap //= 2


if __name__ == '__main__':
    a = [10, 4, 3, 1, 6, 20, 30, 1, 40, 30, 20]
    print(a)
    shell_sort(a)
    print(a)
