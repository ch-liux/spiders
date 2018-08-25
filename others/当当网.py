
#  http://category.dangdang.com/cid4002644.html

import re
import urllib.request
import ssl
import json
import time
import random

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

url = 'http://category.dangdang.com/cid4002644.html'

for page in range(0, 1):
    ua()
    data = urllib.request.urlopen(url).read().decode('utf-8', 'ignore')
    # datapa = 'skudata = {(.*?)}'
    # datapa = "this.pids\[\d\].*?'(.*?)'"
    dataPa = '<li ddt-pit="\d+".*?<a.*?href="(.*?)".*?</a>.*?</li>'
    lists = re.compile(dataPa, re.S).findall(data)
    listData = urllib.request.urlopen(lists[0]).read().decode('gbk', 'ignore')
    titlepa = '<title>(.*?)</title>'
    title = re.compile(titlepa, re.S).findall(listData)
    # print(title)
    pricePa = '<p id="dd-price">.*?</span>(.*?)</p>'
    price = re.compile(pricePa, re.S).findall(listData)
    # print(price)
    for commentPage in range(0, 100):
        commentUrl = 'http://product.dangdang.com/index.php?r=comment%2Flist&productId=60633951&categoryPath=58.88.03.01.01.00&mainProductId=60633951&mediumId=12&pageIndex='+str(commentPage+1)+'&sortType=1&filterType=1&isSystem=1&tagId=0&tagFilterCount=0&template=mall&long_or_short=short'
        commentData = urllib.request.urlopen(commentUrl).read().decode('utf-8')
        commentJ = json.loads(commentData, encoding='utf8')
        # 去掉BOM头
        # if commentJ.startswith(u'\ufeff'):
        #     commentJ = commentJ.encode('utf8')[3:].decode('utf8')
        htmlJ = commentJ['data']['list']['html']
        # print(htmlJ)
        htmlJPa = '<div class="describe_detail">.*?<span>(.*?)</span>.*?</div>'
        htmlDatas = re.compile(htmlJPa, re.S).findall(htmlJ)
        # print(htmlDatas)
        f = open("/当当网数据/当当网第"+str(page+1)+"页数据"+str(time.time())+".txt", 'w', encoding="utf-8")
        f.write("标题："+title[0]+"\n")
        f.write("价格："+price[0]+"\n")
        f.write("第("+str(commentPage+1)+")页评论----------"+"\n")
        index = 1
        for comment in htmlDatas:
            f.write("第("+str(index)+")条："+comment+"\n")
            index += 1
        f.close()
        # 延迟3秒
        # time.sleep(2)