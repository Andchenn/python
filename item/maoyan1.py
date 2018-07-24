import requests
from bs4 import BeautifulSoup


def get_html(url):
    # 伪装成浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/65.0.3325.162 Safari/537.36 '
    }
    r = requests.get(url, headers=headers).text

    return r


def html_parse():
    for url in all_page():
        soup = BeautifulSoup(get_html(url), 'lxml')
        # 电影名
        alldiv = soup.find_all('div', class_='movie-item-info')
        names = [a.find('a')['title'] for a in alldiv]

        # 作者
        allp = soup.find_all('p', class_='star')
        authors = [p.get_text() for p in allp]

        # 评分
        starsi = soup.find_all('p', class_='score')
        scores = [s.get_text() for s in starsi]

        # 上映
        sump = soup.find_all('p', class_='releasetime')
        releases = [r.get_text() for r in sump]

        for name, author, score, released in zip(names, authors, scores, releases):
            name = '电影名:' + str(name)+'\t'
            author = '作者:' + str(author)
            score = '评分:' + str(score)
            released = '上映:' + str(released)
            data = name + author + score + released

            # 保存数据
            f.writelines(data+' '+'\n')


def all_page():
    base_url = 'http://maoyan.com/board/4?offset='
    urllist = []
    # 从0到100，间隔10的数组
    for page in range(0, 100, 10):
        allurl = base_url + str(page)
        urllist.append(allurl)

    return urllist


# 文件名
filename = '猫眼电影Top100.txt'
# 保存文件操作
f = open(filename, 'w', encoding='utf-8')
# 调用函数
html_parse()
f.close()
print('保存成功')
