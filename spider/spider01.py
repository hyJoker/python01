from urllib import request
from bs4 import BeautifulSoup


# 构造函数,抓取第i页数据 http://mirrors.aliyun.com/pypi/simple/
def crow(i):
    pagestart = (i - 1) * 25
    while True:
        url = 'https://movie.douban.com/top250?start=' + str(pagestart)
        html = request.urlopen(url)
    # html = request.urlopen(url).read().decode('utf-8')
    # soup = BeautifulSoup(html, "html.parser")
    # datas=soup.find_all("span",class_="title")
    # for data in datas:
    #     print(data)


crow(1)

