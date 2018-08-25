
# 使用代理处理反爬虫抓取微信文章

import requests
from urllib.parse import urlencode
from requests.exceptions import ConnectionError
from pyquery import PyQuery as pq
import pymongo
from config import *
from lxml.etree import XMLSyntaxError

keyword = '风景'
base_url = "http://weixin.sogou.com/weixin?"
headers = {
    "Cookie":"CXID=49F1D9B6D5A04504028A922CF69C36CD; SUID=90D36E713765860A5AF8541B0003F938; SUV=0085436A716EB2DC5B0C1E2FD0129287; IPLOC=CN4403; ABTEST=0|1533040938|v1; SNUID=844B8BD40E0B7D44E79F896F0FFC529C; __guid=14337457.691143360254124400.1533040976826.8848; weixinIndexVisited=1; sct=1; JSESSIONID=aaancuOV41HrVeHRTLHsw; ppinf=5|1533041904|1534251504|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo1OmlzYWFjfGNydDoxMDoxNTMzMDQxOTA0fHJlZm5pY2s6NTppc2FhY3x1c2VyaWQ6NDQ6bzl0Mmx1QWtYVHdON0ZBZnNZWjBwRXRsTndOY0B3ZWl4aW4uc29odS5jb218; pprdig=FhnXjZLr6uJA4com9_kIMb-gaFgxa46l4VP1zynPCVMtKWsOWMFlFZ4aeA8yUax8u5CvUdL9Xli1-9lfLBCXxjJ2Nln7TSR_IM6tOhZPhzyYr1LAdcBqmvhkSP4wKBMMlAahaIcA_seoxNY8PIqaeZonxnvJBtELoTQ9OelXKmQ; sgid=05-34248497-AVtgXPBwCO9uVMyhYTVJu6Y; ppmdig=15330419040000001eebb6cdbb68cdb1d58625413e4e34b8; monitor_count=6",
    "Host":"weixin.sogou.com",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
}
proxy_pool_url = 'http://127.0.0.1:5000/get'
proxy = None

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

max_count = 5
def get_proxy():
    try:
        response = requests.get(proxy_pool_url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None

def get_html(url, count=1):
    global proxy
    if count >= max_count:
        print("try too  many maxcount")
        return None
    try:
        if proxy:
            proxies = {
                'http': 'http://' + proxy
            }
            response = requests.get(url, allow_redirects=False, headers=headers, proxies=proxies)
        else:
            response = requests.get(url, allow_redirects=False, headers=headers)
        if response.status_code == 200:
            return response.text
        if response.status_code == 302:
            print("302")
            proxy = get_proxy()
            if proxy:
                print("using proxy", proxy)
                return get_html(url)
            else:
                print("get proxy failed")
                return None
    except ConnectionError as e:
        print("ConnectionError", e.args)
        proxy = get_proxy()
        count += 1 
        return get_html(url, count)

def get_index(keyword, page):
    data = {
        'query': keyword,
        'type': 2,
        'page': page
    }
    queries = urlencode(data)
    url = base_url + queries
    html = get_html(url)
    return html

def parse_html(html):
    doc = pq(html)
    items = doc('.news-box .news-list li .txt-box h3 a').items()
    for item in items:
        yield item.attr('href')

def get_detail(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None

def parse_detail(html):
    try:
        doc = pq(html)
        title = doc('.rich_media_title').text()
        content = doc('.rich_media_content').text()
        date = doc('#post-date').text()
        nickName = doc('.profile_nickname').text()
        wechat = doc('#js_profile_qrcode > div > p:nth-child(3) > span').text()
        return {
            'title':title,
            'content':content,
            'date':date,
            'nickName':nickName,
            'wechat':wechat
        }
    except XMLSyntaxError:
        return None

def sace_to_mongo(result):
    if db['articles'].update({'title':result['title']}, {'$set':result}, True):
        print("save to mongo")
    else:
        print("fail")

def main():
    for page in range(1, 2):
        html = get_index(keyword, page)
        if html:
            article_urls = parse_html(html)
            for article_url in article_urls:
                if article_url:
                    article_data = parse_detail(article_url)
                    if article_data:
                        sace_to_mongo(article_data)
if __name__ == '__main__':
    main()