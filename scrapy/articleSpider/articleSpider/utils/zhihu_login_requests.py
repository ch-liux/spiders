import requests
import re
from http import cookiejar

header = {
    "origin":"https://www.zhihu.com",
    "referer":"https://www.zhihu.com/signup?next=%2F",
    "user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5707.400 QQBrowser/10.1.1939.400",
}

def login():
    url = 'https://www.zhihu.com/api/v3/oauth/sign_in'
    data = {

    }
    requests.post(url, data=data, headers=header)