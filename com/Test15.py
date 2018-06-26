# 列表排序及连接

if __name__=='__main__':
    a=[1,2,3]
    b=[3,4,5]
    # 对列表a进行排序
    a.sort()
    print(a)

    # 连接列表a和b
    print(a+b)

    # 连接列表 a与b
    a.extend(b)
    print(a)