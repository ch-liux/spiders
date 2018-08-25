
# 豆瓣读书

import re
import requests

response = requests.get('https://book.douban.com/').text
# bookpa = '<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?author">(.*?).*?publisher">(.*?)</span>.*?</li>'
# pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>', re.S)
# pattern = re.compile(bookpa, re.S)
# pattern = re.compile('<title>(.*?)</title>', re.S)
# pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?</li>', re.S)
# print(response)
# result = re.findall(pattern, response)
# print(result)
bookpa = '<div class="author">(.*?)</span>'
result = re.compile(bookpa, re.S).findall(response)
urllistpa = '<li.*?title.*?href="(.*?)".*?title="(.*?)".*?</li>'
urllist = re.compile(urllistpa, re.S).findall(response)
print(urllist)