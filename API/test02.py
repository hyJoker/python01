# 遍历单个域名
from urllib import request
from bs4 import BeautifulSoup
import re
import datetime
import random

random.seed(datetime.datetime.now())


def getLinks(articleUrl):
    html = request.urlopen("https://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html, "lxml")
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))


# firstUrl = "/wiki/Kevin_Bacon"
# links = getLinks(firstUrl)
# while len(links) > 0:
#     newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]
#     print(newArticle)
#     links = getLinks(newArticle)

pages = set()
index = 1


def getLinks2(pageUrl):
    global pages
    global index
    print("--------" + str(index))
    index += 1
    html = request.urlopen("https://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html, "lxml")
    for link in bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
        if link.attrs["href"] not in pages:
            newPage = link.attrs["href"]
            print(newPage)
            pages.add(newPage)
            getLinks2(newPage)


getLinks2("")
