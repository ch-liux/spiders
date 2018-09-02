#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from selenium import webdriver
from scrapy.selector import Selector


browser = webdriver.Chrome()
# browser = webdriver.Firefox(executable_path='C:/Users/Administrator/firefox.exe')
browser.get('https://www.zhihu.com/#signin')
# print(browser.page_source)
browser.find_element_by_css_selector(".SignContainer-switch span").click()
browser.find_element_by_css_selector(".SignFlow-accountInput input[name='username']").send_keys("18283042497")
browser.find_element_by_css_selector(".Input-wrapper input[name='password']").send_keys("liuxuan720;")
# browser.find_element_by_css_selector("button[type='submit']").submit()
# t_selector = Selector(text=browser.page_source)

# 滚动栏
browser.execute_script("window.scorllTo(0, document.body.scorllHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage")

# 不加载图片
chrome_opt = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images":2}
chrome_opt.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome(chrome_options=chrome_opt)
browser.get("xxx")

# browser.quit()