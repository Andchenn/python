import json

str = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''

print(type(str))
# loads()方法将JSON文本字符串转为JSON对象

data = json.loads(str)
print(data[0]['name'])
print(data[0].get('age'))
print(data[0].get('age', 25))
print(type(data))

data = [{
    'name': 'Bob',
    'gender': 'male',
    'birthday': '1992-10-18'
}]
with open('data.json', 'w')as file:
    # indent 缩进
    # 可以通过dumps()方法将JSON对象转为文本字符串
    file.write(json.dumps(data, indent=2))
print(data)

data = [{
    'name': '王伟',
    'gender': '男',
    'birthday': '1992-10-18'
}]
# encoding='utf-8' ensure_ascii=False 不定义的话就会乱码
with open('data.json', 'w', encoding='utf-8')as file:
    file.write(json.dumps(data, indent=2, ensure_ascii=False))
print(data)
