# 知乎信息爬虫项目开发实战
# https://www.zhihu.com/
# 登录并爬取页面
# 自动登录并保持登录

import urllib.request
import re
import ssl
import urllib.parse
import http.cookiejar
import base64
import json
import hmac
from hashlib import sha1
import time

#为了防止ssl出现问题，你可以加上下面一行代码
ssl._create_default_https_context = ssl._create_unverified_context
print("Cookie处理中…")

#以下进行登陆操作
#建立cookie处理
cjar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener)

print("Cookie处理完成，正在进行登录")
base_url = "https://www.zhihu.com"
req = urllib.request.Request(base_url)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
req_data = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')

print("开始处理验证码")
oauth = "c3cef7c66a1843f8b3a9e6a1e3160e20"
yzm_url = "https://www.zhihu.com/api/v3/oauth/captcha?lang=en"#英文验证码
req = urllib.request.Request(yzm_url)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
req.add_header('authorization', 'oauth ' + str(oauth))
req_data = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
yzm_url = "https://www.zhihu.com/api/v3/oauth/captcha?lang=en"
req = urllib.request.Request(yzm_url, method='PUT')
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
req.add_header('authorization', 'oauth '+str(oauth))
req_data = urllib.request.urlopen(req).read().decode("utf-8","ignore")
pat_yzm = 'img_base64":"(.*?)"'
yzm_data = re.compile(pat_yzm, re.S).findall(req_data)
if(len(yzm_data)>0):
    yzm_data = yzm_data[0]
    print("解码成图片")
    yzm_img = base64.b64decode(yzm_data.replace("\\n", ""))
    fh = open("./知乎验证码.jpg", "wb")
    fh.write(yzm_img)
    fh.close()
else:
    yzm_data = ""
yzm_type = input("请输入验证码类型：（1）倒立图片 （2）直接输入")
yzm_map = {
    1:[22.796875, 22],
    2:[42.796875, 22],
    3:[63.796875, 21],
    4:[84.796875, 20],
    5:[107.796875, 20],
    6:[129.796875, 22],
    7:[150.796875, 22],
}
if(yzm_type == '1'):
    yzm_id = input("请输入倒立图片:")
    captcha = {
        'img_size': [200, 44],
        'input_points': []
    }
    yzm_id = eval(yzm_id)
    for num in yzm_id:
        captcha['input_points'].append(yzm_map[num])
    yzm_value = json.dumps(captcha)
else:
    yzm_value = input("请输入验证码:")
    print("开始验证码验证")
    yzm_post_url = "https://www.zhihu.com/api/v3/oauth/captcha?lang=en"
    yzm_post_data = urllib.parse.urlencode({
        'input_text': yzm_value,
    }).encode('utf-8')
    req1 = urllib.request.Request(yzm_post_url, yzm_post_data)
    req1.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
    req1_data = urllib.request.urlopen(req1).read().decode("utf-8", 'ignore')

# 签名处理
def get_signature(grantType, clientId, source, timestamp):
    hm = hmac.new(b'd1b964811afb40118a12068ff74a12f4', None, sha1)
    hm.update(str.encode(grantType))
    hm.update(str.encode(clientId))
    hm.update(str.encode(source))
    hm.update(str.encode(str(timestamp)))
    return str(hm.hexdigest())
# 账号密码验证
timestamp = int(time.time()*1000)
login_url = "https://www.zhihu.com/api/v3/oauth/sign_in"
login_data = urllib.parse.urlencode({
    "client_id":"c3cef7c66a1843f8b3a9e6a1e3160e20",
    "grant_type":"password",
    "timestamp":timestamp,
    "source":"com.zhihu.web",
    "signature":get_signature("password", "c3cef7c66a1843f8b3a9e6a1e3160e20","com.zhihu.web",timestamp),
    "username":"",
    "password":"",
    "captcha":yzm_value,
    "lang":"en",
    "ref_source":"other_",
    "utm_source":"",
}).encode('utf-8')
req2 = urllib.request.Request(login_url, login_data)
req2.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
req2_data = urllib.request.urlopen(req2).read().decode('utf-8', 'ignore')
print("验证通过")
# 登录成功后爬取
url = "https://www.zhihu.com/"
req = urllib.request.Request(url)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
print("开始爬取第一张页面")
req_data = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
fh = open('./知乎网页1.html', 'w', encodeing="utf-8")
fh.write(req_data)
fh.close()
print("第一张页面爬取结束")

url = "https://www.zhihu.com/question/264239372/answer/450790203"
req = urllib.request.Request(url)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
print("开始爬取第二张页面")
req_data = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
fh = open('./知乎网页2.html', 'w', encodeing='utf-8')
fh.write(req_data)
fh.close()
print("第二张页面爬取结束")

