import datetime

if __name__ == '__main__':
    # 输入今天日期，格式为yy/dd/mm.更多可以查看 strftime()方法
    print(datetime.date.today().strftime('%Y/%m/%d'))

    # 创建日期对象
    miyazakiBirthDate = datetime.date(2018, 1, 5)
    print(miyazakiBirthDate.strftime('%Y/%m/%d'))

    # 日期算术运算
    miyazakiBirthNextDay = miyazakiBirthDate + datetime.timedelta(days=1)
    print(miyazakiBirthNextDay.strftime('%Y/%m/%d'))

    # 日期替换
    miyazakiFirstBirthDay = miyazakiBirthDate.replace(year=miyazakiBirthDate.year + 1)
    print(miyazakiFirstBirthDay.strftime('%Y/%m/%d'))
