# 利用递归方法求5！
# 方法一
def fact(j):
    sum = 0
    if j == 0:
        sum = 1
    else:
        sum = j * fact(j - 1)
    return sum


print(fact(5))

# 方法二
def Factorial(n):
    if n == 1:
        fn = 1
    else:
        fn = n * Factorial(n - 1)
    return fn


print(Factorial(5))
