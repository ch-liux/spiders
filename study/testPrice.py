
import re
import urllib.request
import ssl
import random
from lxml import etree

ssl._create_default_https_context = ssl._create_unverified_context

uapools = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
]

def ua(uapools):
    thisua = random.choice(uapools)
    print(thisua)
    headers = ("User-Agent", thisua)
    opener = urllib.request.build_opener();
    opener.addheaders = [headers]
    # 安装为全局
    urllib.request.install_opener(opener)
ua(uapools)
url = 'http://www.hefei.gov.cn/xxgk/19270/'
data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
# print(data)
# datapa = '<div class="news_con">.*?<li>(.*?)</li>.*?<div>'
# lists = re.compile(datapa,re.S).findall(data)
doc = etree.HTML(data)
# print(doc)
lisDate = doc.xpath('//div[@class="news_con"]/ul/li/text()')
# print(lisDate)
lisTitle = doc.xpath('//div[@class="news_con"]/ul[@class="con_list"]/li/a/@title')
print(lisTitle)
lisHref = doc.xpath('//div[@class="news_con"]/ul[@class="con_list"]/li/a/@href')
# print(lisHref)
