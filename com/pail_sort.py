# 桶排序
def pail_sort(my_list):
    max_num = max(my_list)
    min_mun = min(my_list)

    Y_list = []
    for i in range(min_mun, max_num + 1):
        f_list = [i, 0]
        Y_list.append(f_list)

    for m in my_list:
        for Y in Y_list:
            if Y[0] == m:
                Y[1] += 1

    result = []

    for n in Y_list:
        for t in range(0, n[1]):
            result.append(n[0])

    return result

    pass


def main():
    Y_list = [100, 20, 45, 54, 63, 12, 22, 93, 17, 10, 77, 31, 44, 55, 26]
    print("简单桶排序之前的序列：", Y_list)
    print("简单桶排序之后的序列：", pail_sort(Y_list))


if __name__ == '__main__':
    main()


