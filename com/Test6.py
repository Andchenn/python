# 利用递归函数方式，将所输入的5个字符，以相反顺打印出来

def output(s, l):
    if l == 0:
        return
    print(s[l - 1])
    output(s, l - 1)


s = input('Input a string:')
l = len(s)
output(s, l)