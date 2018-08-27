#!/usr/bin/env python
# 老版的知乎，请参考orther知乎
# -*- coding:utf-8 -*-

import requests
import re

try:
    #py2
    import cookielib
except:
    #py3
    import http.cookiejar as cookielib

session = requests.session()
# cookies保存到本地文件名
session.cookies = cookielib.LWPCookieJar(filename="cookies.text")
try:
    session.cookies.load(ignore_discard=True)
except:
    print("cookie未能加载")


agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
header = {
    "HOST":"www.zhihu.com",
    "Referrer":"https://www.zhihu.com",
    "User-Agent":agent
}


def is_login():
    inbox_url = "https://www.zhihu.com/inbox"
    # allow_redirects 是否跳转url
    response = session.get(inbox_url, headers=header, allow_redirects=False)
    if response.status_code != 200:
        return False
    else:
        return True


def get_index():
    response = session.get("https://www.zhihu.com", headers=header)
    with open("index_page.html", 'wb') as f:
        f.write(response.text.encode('utf-8'))
    print("ok")


def get_captcha():
    import time
    t = str(int(time.time()*1000))
    captcha_url = "https://www.zhihu.com/captcha.gif?r={0}&type=login".format(t)
    t = session.get(captcha_url, header=header) #成功
    # t = requests.get(captcha_url, header=header) #失败
    with open("captcha.jpg", "wb") as f:
        f.write(t.content)
        f.close()
    from PIL import Image
    try:
        im = Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        pass
    captcha = input("输入验证码\n>")
    return captcha


def get_xsrf():
    response = session.get("https://www.zhihu.com", headers=header)
    print(response.text)
    text = '<input type="hidden" name="_xsrf" value="xxx" />'
    match_obj = re.match('.*name="_xsrf" value="(.*?)"')
    if match_obj:
        return match_obj.group(1)
    return ""


# 知乎登录
def zhihu_login(account, password):
    if re.match("^1\d{10}", account):
        print("手机号码登录...")
        post_url = "https://www.zhihu.com/login/phone_num"
        post_data = {
            "_xsrf":get_xsrf(),
            "phone_num":account,
            "password":password,
            "captcha":get_captcha()    #验证码
        }
    else:
        if "@" in account:
            print("邮箱方式登录...")
            post_url = "https://www.zhihu.com/login/eamil"
            post_data = {
                "_xsrf": get_xsrf(),
                "eamil": account,
                "password": password,
                "captcha":get_captcha()
            }
    response_text = session.post(post_url, data=post_data, headers=header)
    session.cookies.save()


if is_login():
    print("login")
else:
    zhihu_login("xxx", "yyy")