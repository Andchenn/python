# 输入三个整数x,y,z,请把这三个数由小到大输出
# 方法一：
l = []
for i in range(3):
    x = int(input('输入数字：'))
    # 把数字x添加到l中
    # append 在列表末尾添加新的对象
    l.append(x)
# 排序
l.sort()
print('这三个数从小到大输出为：', l)


# 方法二
x = int(input('x:'))
y = int(input('y:'))
z = int(input('z:'))
if x > y: x, y = y, x
if x > z: x, z = z, x
if y > z: y, z = z, y
print('这三个数从小到大输出为：', x, y, z)
