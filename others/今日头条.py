
# 今日头条
# 分析ajax

from urllib.parse import urlencode
import requests
from requests.exceptions import RequestException
import json
from json.decoder import JSONDecodeError
from bs4 import BeautifulSoup
import re
import os
from hashlib import md5
from multiprocessing import Pool
# pip install demjson
# import demjson
from config import *
# pip install pymongo
import pymongo

client = pymongo.MongoClient(MONGO_URL, connect=False)  #由于启动多进程，会出现connect未生成；connect=False会生成一个连接
db = client[MONGO_DB]

def get_page_index(offest, keyword):
    data = {
        'offest': offest,
        'format':'json',
        'keyword': keyword,
        'autoload':'true',
        'count':'20',
        'cur_tab':3
    }
    url = 'http://www.toutiao.com/search_content/?' + urlencode(data)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求索引页出错', url)
        return None

def parse_page_index(html):
    try:
        data = json.loads(html)
        if data and 'data' in data.keys():
            for item in data.get('data'):
                yield item.get('article_url')
    except JSONDecodeError:
        pass


def get_page_detail(url):
    try:
        # url_reg = re.compile('\d+').findall(url)
        # newUrl = 'a'+url_reg[0]
        # url = re.sub('\d+', newUrl, url)
        urls = url.split('/')
        urls = [x for x in urls if x != '']
        newUrl = urls[0] + "//www." + urls[1] + '/a' + urls[3]
        response = requests.get(newUrl)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求详情页出错', url)
        return None

def parse_page_detail(html, url):
    # print(html)
    # with open('/t.txt','w', encoding='utf-8') as f:
    #     f.write(html)
    #     f.close()
    soup = BeautifulSoup(html, 'lxml')
    title = soup.select('title')[0].get_text()
    # print(title)
    images_pattern = re.compile('gallery: JSON.parse\("(.*?)"\)', re.S)
    result = re.search(images_pattern, html)
    if result:
        resultTemp = result.group(1).replace("\\",'')
        data = json.loads(resultTemp)
        if data and 'sub_images' in data.keys():
            sub_images = data.get('sub_images')
            images = [item.get('url') for item in sub_images]
            for image in images:
                download_image(image)
            return {
                'title': title,
                'images': images,
                'url': url
            }

def save_to_mongo(result):
    if db[MONGO_TABLE].insert(result):
        print("save to mongoDB success", result)
        return True
    return False

def download_image(url):
    print('正在下载',url)
    try:
        # urls = url.split('/')
        # urls = [x for x in urls if x != '']
        # newUrl = urls[0] + "//www." + urls[1] + '/a' + urls[3]
        response = requests.get(url)
        if response.status_code == 200:
            save_image(response.content)
        return None
    except RequestException:
        print('请求图片出错', url)
        return None

def save_image(content):
    file_path = '{0}/{1}.{2}'.format(os.getcwd(), md5(content).hexdigest(), 'jpg')
    print('保存地址',file_path)
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(content)
            f.close()

def main(offest):
    html = get_page_index(offest, KEYWORD)
    for url in parse_page_index(html):
        html = get_page_detail(url)
        if html:
            result = parse_page_detail(html, url)
            if result:
                save_to_mongo(result)

if __name__ == '__main__':
    # main()
    groups = [x*20 for x in range(GROUP_START, GROUP_END+1)]
    pool = Pool()
    pool.map(main, groups)



