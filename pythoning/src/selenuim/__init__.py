
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('http://www.baidu.com/')

inputs = browser.find_element_by_id("kw")
inputs.send_keys("张维序")
browser.find_element_by_id("su").click()
