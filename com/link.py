# 创建一个链表

if __name__ == '__main__':
    par = []
    for i in range(5):
        num = int(input('please input a number:\n'))
        par.append(num)
    print(par)
    par.reverse()
    print(par)
