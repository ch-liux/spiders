
# 云栖社区 - python
import re
import urllib.request
import ssl
import json
import time
import random
import requests

ssl._create_default_https_context = ssl._create_unverified_context

def ua():
    uapools = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    ]
    thisua =  random.choice(uapools)
    header = ("User-Agent",thisua)
    print(header)
    opener = urllib.request.build_opener()
    opener.addheaders = [header]
    urllib.request.install_opener(opener)

url = 'https://yq.aliyun.com/search/articles/'
key = 'Python'

data = requests.get(url, {"q":key}).text
dataNumPa = '找到(.*?)条关于'
dataNum = re.compile(dataNumPa, re.S).findall(data)
nums = None

# if len(dataNum)>0:
#     if dataNum[0] != None | dataNum[0] != '' | dataNum[0] != ' ':
#         nums = int(dataNum[0])

for page in range(0, 10):
    ua()
    key = {
        "p":str(page+1),
        "q":key
    }
    listDatas = requests.get(url, key).text
    listDatasPa = '<div class="media-body text-overflow">.*?<a href="(.*?)">'
    listUrls = re.compile(listDatasPa, re.S).findall(listDatas)
    # print(listData)
    index = 1
    for d in listUrls:
        listUrl = 'https://yq.aliyun.com' + d
        listData = requests.get(listUrl).text
        listDataTitlePa = '<title>(.*?)</title>'
        listDataTitle = re.compile(listDataTitlePa, re.S).findall(listData)
        # print("标题: "+listDataTitle[0])
        listDataContentPa = '<div class="content-detail markdown-body">(.*?)</div>'
        listDataContent = re.compile(listDataContentPa, re.S).findall(listData)
        # print("内容: "+listDataContent[0])
        f = open('/云栖社区/python_第'+str(page+1)+'页第'+str(index)+'条'+str(time.time())+'.txt', 'w', encoding='utf-8')
        f.write("标题: "+listDataTitle[0]+"\n")
        f.write("内容: "+listDataContent[0])
        f.close()
        index += 1
        time.sleep(3)
    time.sleep(2)

