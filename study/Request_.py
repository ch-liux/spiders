
# Requests
# pip3 install requests

import requests
# response = requests.get("https://www.baidu.com/")
# print(type(response))
# print(response.status_code)
# print(type(response.text))
# print(response.text)
# print(response.cookies)

#
# requests.post("http://httpbin.org/post")
# requests.put("http://httpbin.org/put")
# requests.delete("http://httpbin.org/delete")
# requests.head("http://httpbin.org/get")
# requests.options("http://httpbin.org/get")

# 基本写法
# response = requests.get("http://httpbin.org/get")
# print(response.text)

# get带参数
# response = requests.get("http://httpbin.org/get?name=lxzy&age=22")
# print(response.text)

# get带参数
# data = {
#     "name":'lxzy',
#     "age":22
# }
# response = requests.get('http://httpbin.org/get', params=data)
# print(response.text)

# 解析json
import json
# response = requests.get('http://httpbin.org/get')
# print(type(response.text))
# print(response.json())
# print(json.loads(response.text))
# print(type(response.json()))

# 获取二进制数据
# response = requests.get('https://github.com/favicon.ico')
# print(type(response.text), type(response.content))
# print(response.text)
# print(response.content)

# 保存二进制文件
# response = requests.get('https://github.com/favicon.ico')
# with open('favicon.ico', 'wb') as f:
#     f.write(response.content)
#     f.close

# 添加header
# response = requests.get('https://www.zhihu.com/explore')
# print(response.text)

# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
# }
# response = requests.get('https://www.zhihu.com/explore', headers=headers)
# print(response.text)


# 基于 post请求
# data = {
#     'name':'lxzy',
#     'age':'22'
# }
# response = requests.post("http://httpbin.org/post", data=data)
# print(response.text)

# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
# }
# response = requests.post("http://httpbin.org/post", data=data, headers=headers)
# print(response.text)


# 响应
# response = requests.get('http://www.jianshu.com')
# print(type(response.status_code), response.status_code)
# print(type(response.headers), response.headers)
# print(type(response.cookies), response.cookies)
# print(type(response.url), response.url)
# print(type(response.history), response.history)

# 状态码判断
import requests
# response = requests.get('http://www.jianshu.com')
# print(requests.codes)
# exit() if not response.status_code == 200 else print('request successfully')

# response = requests.get('http://www.jianshu.com')
# print(requests.codes)
# exit() if not response.status_code == requests.codes else print('request successfully')

# 100:('continue',),
# 101:('switching_protocols',),
# 102:('processing',),
# 103:('checkpoint',),
# 122:('url_too_long','request_url_too_long'),
# 200:('ok','okay','all_ok','all_okay','all_good','\\o/','√'),
# 201:('created',),
# 202:('accepted',),
# 203:('non_authoritative_info', 'non_authoritative_information'),
# 204:('no_content',),
# 205:('reset_content','reset'),
# 206:('partial_content','partial'),
# 207:('multi_status','multiple_status','multi_stati','multiple_stati'),
# 208:('already_reported',),
# 226:('im_used',),
# # Redirection
# 300:('multiple_choices',),
# 301:('moved_permanently','moved','\\o-'),
# 302:('found',),
# 303:('see_other','other'),
# 304:('not_modified',),
# 305:('use_proxy',),
# 306:('switch_proxy',),
# 307:('temporary_redirect','temporary_moved','temporary'),
# 308:('permanent_redirect','resume_incomplete','resume',),#These 2 to be removed in 3.0
# Client Error
# 400:('bad_request', 'bad')
# 4..
# Server Error
# 500:
# 5..

# 高级操作
# 文件上传
# import requests
# files = {'file':open('favicon.ico', 'rb')}
# response = requests.post('http://httpbin.org/post', files=files)
# print(response.text)
# 获取cookie
# response = requests.get('https://www.baidu.com')
# print(response.cookies)
# for key,value in response.cookies.items():
#     print(key+'='+value)
# 会话维持
# 模拟登陆
# requests.get('http://httpbin.org/cookies/set/number/123456')
# response = requests.get('http://httpbin.org/cookies')
# print(response.text)
# ---- 一个浏览器内操作
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456')
# response = s.get('http://httpbin.org/cookies')
# print(response.text)

# 证书验证
# response = requests.get('https://www.12306.cn')
# print(response.status_code)

from requests.packages import urllib3
# 去除警告
# urllib3.disable_warings()
# response = requests.get('https://www.12306.cn', verify=False)
# print(response.status_code)
# 设置证书
# response = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))
# print(response.status_code)

# 代理设置
# 启动代理才会生效  翻墙一般有代理
# proxy = {
#     'http':'http://127.0.0.1:9743',
#     'https':'https://127.0.0.1:9743'
# }
# response = requests.get('https://www.taobao.com', proxies=proxy)
# print(response.status_code)

# proxy = {
#     'http':'http://user:password@127.0.0.1:9743',
# }
# response = requests.get('https://www.taobao.caom', proxies=proxy)
# print(response.status_code)

# pip3 install 'requests[socks]'
# import requests
# proxies = {
#     'http':'socks5://127.0.0.1:9742',
#     'https':'socks5://127.0.0.1:9742'
# }
# response = requests.get('https://www.taobao.caom', proxies=proxies)
# print(response.status_code)


# 超时设置 
# response = requests.get('https://www.taobao.com', timeout=1)
# print(response.status_code)

from requests.exceptions import ReadTimeout
# try:
#     response = requests.get('https://www.taobao.com', timeout=0.1)
#     print(response.status_code)
# except ReadTimeout:
#     print('time out')


# 认证设置
import requests 
from requests.auth import HTTPBasicAuth
# r = requests.get('http://120.27.34.24:9001', auth=HTTPBasicAuth('user', '123'))
# print(r.status_code)

# r = requests.get('http://120.27.34.24:9001', auth=('user', '123'))
# print(r.status_code)

# 异常处理
from requests.exceptions import ReadTimeout,HTTPError,RequestException
try:
    response = requests.get('http://httpbin.org/get', timeout=0.5)
    print(response.status_code)
except ReadTimeout:
    print('time out')
except HTTPError:
    print('http error')
except RequestException:
    print('request exception')