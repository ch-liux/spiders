
# 淘宝手机
import re
import urllib.request
import ssl
import random

ssl._create_default_https_context = ssl._create_unverified_context

keyname = "手机"
key = urllib.request.quote(keyname)
headers = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)"
]

def browser(header):
    thisb = random.choice(header)
    print("browser header is :", thisb)
    header = ("User-Agent", thisb)
    opener = urllib.request.build_opener()
    opener.addheaders = [header]
    # 全局
    urllib.request.install_opener(opener)

for i in range(1, 2):
    print("-----第"+str(i)+"页商品------")
    url = "https://s.taobao.com/search?q="+key+ "&=" + str((i-1)*44)
    print("url : ", url)
    browser(headers)
    data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
    # print(data)
    taginfopa = '"tag_info":(.*?),"cmt_count"'
    taginfolist = re.compile(taginfopa).findall(data)
    titlepa = '"title":"(.*?)"'
    titlelist = re.compile(titlepa).findall(data)
    catpa = '"cat":"(.*?)"'
    catlist = re.compile(catpa).findall(data)
    urlpa = '"url":"(.*?)"'
    urllist = re.compile(urlpa).findall(data)
    print(taginfolist)
    print(titlelist)
    print(catlist)
    print(urllist)

