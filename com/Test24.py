# 某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如
# 下：每位数字都加5,然后用和除以10的代替该数字，再将第一位和第四位交换，第二位和
# 第三位交换
from sys import stdout

if __name__ == '__main__':
    a = int(input('输入四个数字：\n'))
    b = [a % 10, a % 100 / 10, a % 1000 / 100, a / 1000]
    for i in range(4):
        b[i] += 5
        b[i] %= 10
    for i in range(2):
        b[i], b[3 - i] = b[3 - i], b[i]
    for i in range(3, -1, -1):
        stdout.write(str(b[i]))