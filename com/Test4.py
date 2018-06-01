# 输入某年某月某日，判断这一天是这一年的第几天？
# 以2018年为例
# 方法一：
import datetime

year = int(input('请输入年份：'))
month = int(input('请输入月份：'))
day = int(input('请输入是哪一天：'))

months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
if 0 < month <= 12:
    sum = months[month - 1]
else:
    print('data error')
sum += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1

if (leap == 1) and (month > 2):
    sum += 1
print('it is the %dth day.' % sum)

# 方法二：
# 获取年份
year = int(input('请输入年份：'))
# 获取月份
month = int(input('请输入月份：'))
# 获取日
day = int(input('请输入是哪一天：'))
# 将输入的日期格式化成标准的日期
targetDay = datetime.date(year, month, day)
# 减去上一年最后一天
dayCount = targetDay - datetime.date(targetDay.year - 1, 12, 31)
print('%s是%s年的第%s天' % (targetDay, year, dayCount.days))
