from urllib import request
from bs4 import BeautifulSoup
import re


def getTitle(url):
    try:
        html = request.urlopen(url)
    except request.HTTPError as e:
        print("url Error!!!")
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.h1
    except AttributeError as e:
        return None
    return title


def DDSurl(url):
    i = 0
    while True:
        print(i)
        i = i + 1
        html = request.urlopen(url)
        if html == None:
            print(html)
            return None


# https://v.qq.com/
# http://www.pythonscraping.com/pages/page3.html
try:
    html = request.urlopen("http://www.pythonscraping.com/pages/page3.html")
    print(1)
except request.HTTPError as e:
    print(e)
    print(2)
else:
    # 推荐使用lxml解析器
    bsObj = BeautifulSoup(html.read(), "lxml")
    print(3)
    # nameList = bsObj.findAll("span", {"class": "green"})
    # print(4)
    # for name in nameList:
    #     print(name.get_text())

    # childrens = bsObj.find("table", {"id": "giftList"}).children
    # for child in childrens:
    #     print(child)

    # childrens = bsObj.find("table", {"id": "giftList"}).tr.next_siblings
    # for child in childrens:
    #     print(child)

    # images = bsObj.findAll("img", {"src": re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
    # for image in images:
    #     print(image["src"])

    # images = bsObj.findAll("img")
    # for image in images:
    #     print(image.attrs["src"])

    tags = bsObj.findAll(lambda tag: len(tag.attrs) == 2)
    for aa in tags:
        print(aa)