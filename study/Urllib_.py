
# 
import urllib.request
import urllib.parse

# data = urllib.request.urlopen("http://www.baidu.com")
# print(data.read())

# data = bytes(urllib.parse.urlencode({'word':'hello'}), encoding='utf8')
# response = urllib.request.urlopen('http://httpbin.org/post', data=data) # 公开post测试地址
# print(response.read())

# data = urllib.request.urlopen('http://httpbin.org/get', timeout=1)
# print(data.read())

import socket
import urllib.error
# try:
#     data = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print("time out")

# data = urllib.request.urlopen("https://www.python.org")
# print(type(data))
# print(data.status)
# print(data.getheaders())
# print(data.getheader('Server'))
# print(data.read().decode('utf-8'))

import urllib
# Request
#
#
# request = urllib.request.Request('https://www.python.org')
# response = urllib.request.urlopen(request)
# print(response)

from urllib import request,parse
# url = 'http://httpbin.org/post'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 QIHU 360SE',
#     'Host': 'httpbin.org'
# }
# dict = {
#     'name': 'Germey'
# }
# data = bytes(parse.urlencode(dict), encoding='utf8')
# req = request.Request(url=url, data=data, headers=headers, method='POST')
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))

# url = 'http://httpbin.org/post'
# dict = {
#     'name': 'liux'
# }
# data = bytes(parse.urlencode(dict), encoding='utf8')
# req = request.Request(url=url, data=data, method='POST')
# req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 QIHU 360SE')
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))


# Handler
# 代理
# proxy_handler = urllib.request.ProxyHandler({
#     'http':'http://127.0.0.1:8080',
#     'https':'https://127.0.0.1:8080'
# })
# opener = urllib.request.build_opener(proxy_handler)
# response = opener.open('http://www.baidu.com')
# print(response.read())

# Cookie   维持登录状态的机制
# 获取cookie
# import http.cookiejar,urllib.request
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open("http://www.baidu.com")
# for item in cookie:
#     print(item.name+"="+item.value)

# 记录到本机cookie
# filename = 'cookie.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)

# 记录到本机cookie
# filename = 'cookie.txt'
# cookie = http.cookiejar.LWPCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)

# 加载对应方式存储的cookie
# cookie = http.cookiejar.LWPCookieJar()
# cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# print(response.read().decode('utf-8'))


# 异常处理
# from urllib import request,error
# try:
#     response = request.urlopen('http://cuiqingcai.com/index.htm')
# except error.URLError as e:
#     print(e.reason)

# try:
#     response = request.urlopen('http://cuiqingcai.com/index.htm')
# except error.HTTPError as e:
#     print(e.reason, e.code, e.headers, sep="\n")
# except error.URLError as e:
#     print(e.reason)
# else:
#     print("Request successfuly.")

# try:
#     response = urllib.request.urlopen('http://www.baidu.com', timeout=0.01)
# except urllib.error.URLError as e:
#     print(type(e.reason))
#     if isinstance(e.reason, socket.timeout):
#         print("time out")


# URL 解析

# urlparse(urlstring, scheme='', allow_fragments=True)
# 协议类型(http,https)  
# from urllib.parse import urlparse
# result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# print(type(result), result)

# result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
# print(result)

# result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', scheme='https')
# print(result)

# result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
# print(result)

# result = urlparse('http://www.baidu.com/index.html?#comment', allow_fragments=False)
# print(result)

# urlunparse
# from urllib.parse import urlunparse
# data = ['http','www.baidu.com','index.html','user','a=6','comment']
# print(urlunparse(data))

# urljoin
# 后者参数覆盖
# from urllib.parse import urljoin
# print(urljoin('http://www.baidu.com','FAQ.html'))
# print(urljoin('http://www.baidu.com','https://cuiqingcai.com/FAQ.html'))


# urlencode
# from urllib.parse import urlencode
# params = {
#     'name':'liux',
#     'age':22
# }
# url = 'http://www.baidu.com?'
# url = url + urlencode(params)
# print(url)

# 检查 是否可以访问
import urllib.robotparser
rp = urllib.robotparser.RobotFileParser()
rp.set_url('http://www.musi-cal.com/robots.txt')
rp.read()
rrate = rp.request_rate('*')
print(rrate.requests)