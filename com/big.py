# 找到年龄最大的人，并输出。
# 方法一
if __name__ == '__main__':
    person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}
    m = 'li'
    for key in person.keys():
        if person[m] < person[key]:
            m = key
    print('%s,%d' % (m, person[m]))

person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}

# 方法二
def find_max(dict):
    max_age = 0
    for key, value in dict.items():
        if value > max_age:
            max_age = value
            name = key
    print(name,max_age)


find_max(person)
