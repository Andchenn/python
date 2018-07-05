def add_number(num):
    def adder(number):
        # adder是个闭包
        return num + number

    return adder


a1 = add_number(10)
print(a1(5))

a2 = add_number(20)
print(a2(3))
