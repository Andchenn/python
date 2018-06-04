# 输入一行字符，分别统计出其中英文字母,空格,数字和其它字符的个数.
# 程序分析：利用while或for语句，条件为输入的字符不为'\n'

# 方法一
s = input('请输入一个字符串：\n')
letters = 0
space = 0
digit = 0
others = 0
i = 0
while i < len(s):
    c = s[i]
    i += 1
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print('char = %d,space = %d,digit = %d,other = %d' % (letters, space, digit, others))


# 方法二
s = input('请输入一个字符串：\n')
letters = 0
space = 0
digit = 0
others = 0
i = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print('char = %d,space = %d,digit = %d,other = %d' % (letters, space, digit, others))
