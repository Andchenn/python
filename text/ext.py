# Python 十进制转二进制、八进制、十六进制

dec = int(input("输入数字:"))
print("十进制为：", dec)
print("转换为二进制为：", bin(dec))
print("转换为八进制为：", oct(dec))
print("转换为十六进制：", hex(dec))
print('************************')

# Python 二进制转十进制、八进制、十六进制

print(int('10100111110', 2))
print(oct(0b1010))
print(hex(int('101010', 2)))
