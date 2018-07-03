# 输入一个奇数，然后判断最少几个9除于该数的结果为整数
# 程序分析：999999/13=76923

if __name__ == '__main__':
    ji = int(input('输入一个数字：\n'))
    n1 = 1
    c9 = 1
    m9 = 9
    sum = 9
    while n1 != 0:
        if sum % ji == 0:
            n1 = 0
        else:
            m9 *= 10
            sum += m9
            c9 += 1
    print('%d个9可以被%d整除：%d' % (c9, ji, sum))
    r = sum / ji
    print('%d/%d=%d' % (sum, ji, r))
