def paven(n):
    i = 0
    s = 0.0
    for i in range(2, n + 1, 2):
        # python里，整数除整数，只能得出整数，所以需要使用浮点数1.0
        s += 1.0 / i
    return s


def podd(n):
    s = 0.0
    for i in range(1, n + 1, 2):
        # python里，整数除整数，只能得出整数，所以需要使用浮点数1.0
        s += 1.0 / i
    return s


def dcall(fp, n):
    s = fp(n)
    return s


if __name__ == '__main__':
    n = int(input('input a number:\n'))
    if n % 2 == 0:
        sum = dcall(paven, n)
    else:
        sum = dcall(podd, n)
    print(sum)
