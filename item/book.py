import requests
from bs4 import BeautifulSoup


# 请求获得HTML源码的函数
def get_html(url):
    # 伪装成浏览器访问服务器
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/58.0.3029.110 Safari/537.36'}
    r = requests.get(url, headers=headers).text
    return r


# 解析页面，获得数据信息
def html_parse():
    # 调用函数，for循环迭代出所有页面
    for url in all_page():
        # BeautifulSoup的解析
        soup = BeautifulSoup(get_html(url), 'lxml')
        # 书名
        alldiv = soup.find_all('div', class_='pl2')
        names = [a.find('a')['title'] for a in alldiv]
        # 作者
        allp = soup.find_all('p', class_='pl')
        authors = [p.get_text() for p in allp]
        # 评分
        starspan = soup.find_all('span', class_='rating_nums')
        scores = [s.get_text() for s in starspan]
        # 简介
        sum_div = soup.select('tr.item > td:nth-of-type(2)')
        sums = []
        for d in sum_div:
            sumspan = d.find('span', class_='inq')
            summary = sumspan.get_text() if sumspan else '无'
            sums.append(summary)

        for name, author, score, sum in zip(names, authors, scores, sums):
            name = '书名' + str(name) + '\n'
            author = '作者' + str(author) + '\n'
            score = '评分' + str(score) + '\n'
            sum = '简介' + str(sum) + '\n'
            data = name + author + score + sum
            # 保存数据
            f.writelines(data + '=====================' + '\n')


# 获取所有页面的函数
def all_page():
    base_url = 'https://book.douban.com/top250?start='
    urllist = []
    # 从0到255,间隔25的数组
    for page in range(0, 250, 25):
        allurl = base_url + str(page)
        urllist.append(allurl)
    return urllist


# 文件名
filename = '豆瓣图书Top250.txt'
# 保存文件操作
f = open(filename, 'w', encoding='utf-8')
# 调用函数
html_parse()
f.close()
print('保存成功')
