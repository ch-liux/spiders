'''
Created on 2018年8月2日

@author: Administrator
'''
import requests
import random
import re
from pyquery import PyQuery as pq

base_url = "https://s.taobao.com/search"
keyword = "手机"
headers = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)"
]
params = {
    "q":keyword
}

def get_header(headers):
    thish = random.choice(headers)
    return {"User-Agent":thish}

def get_html():
    header = get_header(headers)
    response = requests.get(base_url, headers=header, params=params)
    if response.status_code == 200:
        return response.text
    return None

def get_total(html):
    totalpa = '"totalPage":(\d+)'
    total = re.compile(totalpa).findall(html)
    if total:
        return int(total[0])
    return 0

def get_pageSize(html):
    pagepa = '"pageSize":(\d+)'
    page = re.compile(pagepa).findall(html)
    if page:
        return int(page[0])
    return 0

def get_detail(html):
    item_img = html(".J_ItemPic").attr("src")
    print(item_img)
    
def main():
    html = get_html()
    total = get_total(html)
    demopa = '"title":"(.*?)","pic_url":"(.*?)","price":"(.*?)".*?\[.*?\].*?"month_sales":"(.*?)".*?"seller":{.*?},"url":"(.*?)"'
    data = re.compile(demopa).findall(html)
#     print(data)
    uu = data[0][4]
    print(uu)
    print(uu.replace('003', '='))

if __name__ == '__main__':
#     main()
    url = "https://s.taobao.com/search?q=手机&s=0"
    res = requests.get(url, headers=headers)
    res = res.text
    lis = re.compile('"nid":"(.*?)"').findall(res)
    print(lis)
    