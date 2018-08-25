#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests
import re

try:
    #py2
    import cookielib
except:
    #py3
    import http.cookiejar as cookielib


agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
header = {
    "HOST":"www.zhihu.com",
    "Referrer":"https://www.zhihu.com",
    "User-Agent":agent
}


def get_xsrf():
    response = requests.get("https://www.zhihu.com", headers=header)
    print(response.text)
    text = ''
    return response


# 知乎登录
def zhihu_login(account, password):
    if re.match("^1\d{10}", account):
        print("手机号码登录...")
        post_url = "https://www.zhihu.com/login/phone_num"
        post_data = {
            "_xsrf":get_xsrf(),
            "phone_num":account,
            "password":password
        }
        response = requests.post(post_url, data=post_data, headers=header)


if __name__ == "__main__":
    get_xsrf()