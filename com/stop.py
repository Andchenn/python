# 暂停一秒输出

import time

# 方法一
myD = {1: 'a', 2: 'b'}
for k, v in dict.items(myD):
    print(k, v)
    # 暂停1秒
    time.sleep(1)

print("\n")

# 方法二
l = [1, 2, 3, 4]
for i in range(len(l)):
    print(l[i])
    time.sleep(1)
