# 学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

score = int(input('请输入你的分数：\n'))
if score >= 90:
    grade = '优'
elif score >= 80:
    grade = '良'
elif score >= 70:
    grade = '中'
elif score >= 60:
    grade = '及格'
else:
    grade = '差'
print('%d 属于 %s' % (score, grade))
