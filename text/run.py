year = int(input("输入一个年份："))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            # 整百年能被400整除的是闰年
            print("{0}是润年".format(year))
        else:
            print("{0}不是润年".format(year))
    else:
        # 非整百年能被4整除的为闰年
        print("{0}是润年".format(year))
else:
    print("{0}不是润年".format(year))
