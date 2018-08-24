# 19723756=云音乐飙升榜, 3779629=云音乐新歌榜, 2884035=网易原创歌曲榜, 3778678=云音乐热歌榜
# 评论
# https://music.163.com/weapi/v1/resource/comments/A_PL_0_19723756?csrf_token=

import re
from selenium import webdriver
import selenium.webdriver.support.ui as ui


# driver = webdriver.PhantomJS(executable_path=r'C:\liux\py_tools\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver = webdriver.PhantomJS(executable_path='phantomjs.exe')
driver.get("https://music.163.com/discover/toplist")
driver.switch_to.frame('g_iframe')
wait = ui.WebDriverWait(driver, 15)
body = driver.page_source
toplistidpa = 'href="/discover/toplist\?id=(\d+)"'
toplistids = re.compile(toplistidpa, re.S).findall(body)
# for
driver.get("https://music.163.com/discover/toplist?id=19723756")
driver.switch_to.frame('g_iframe')
wait = ui.WebDriverWait(driver, 15)
body = driver.page_source
# title = body.title
# print(title)
# print(body)
titlepa = '<h2 class="f-ff2">(.*?)</h2>'
title = re.compile(titlepa, re.S).findall(body)
print(title)
toplistpa = '<tr id="(\d+)".*?>.*?</tr>'
tolists = re.compile(toplistpa, re.S).findall(body)
print(tolists)