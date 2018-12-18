from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

# 抓取网页链接

pages = set()
random.seed(datetime.datetime.now())


# 获取页面内所有内链的列表
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    # 找出所有以"/"开头的链接
    for link in bsObj.findAll("a", href=re.compile("^(/|.*" + includeUrl + ")")):
        if link.attrs["href"] is not None:
            if link.attrs["href"] not in internalLinks:
                internalLinks.append(link.attrs["href"])
    return internalLinks


# 获取页面内的外链接
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # 找出所有以"http"或"www" 开头且不包含当前url的链接
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!" + excludeUrl + ").)*$")):
        if link.attrs["href"] is not None:
            if link.attrs["href"] not in externalLinks:
                externalLinks.append(link.attrs["href"])
    return externalLinks


def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

