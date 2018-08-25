
# selenium 
# 自动化测试 主要解决JavaScript渲染问题
# pip3 install selenium

# 基本使用
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait

# browser = webdriver.Chrome()

# try:
#     browser.get('https://www.baidu.com')
#     input = browser.find_element_by_id('kw')
#     input.send_keys('Python')
#     input.send_keys(Keys.ENTER)
#     #等待
#     wait = WebDriverWait(browser, 10)  
#     wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
#     print(browser.current_url)
#     print(browser.get_cookies())
#     print(browser.page_source)
# finally:
#     browser.close()


# 声明浏览器对象
from selenium import webdriver
browser = webdriver.Chrome()
# browser = webdriver.Firefox()
# browser = webdriver.Edge()
# browser = webdriver.PhantomJS()
# browser = webdriver.Safari()


# 访问页面
browser.get('https://www.taobao.com')
print(browser.page_source)
browser.close()

# 查找元素

# 单个元素
browser.get('https://www.taobao.com')
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_css_selector('#q')
input_thrid = browser.find_element_by_xpath('//*[@id=q]')
print(input_first, input_second, input_thrid)
browser.close()

from selenium.webdriver.common.by import By
browser.get('https://www.taobao.com')
input_first = browser.find_element(By.ID, 'q')
print(input_first)
browser.close()

# 多个元素
browser.get('https://www.taobao.com')
lis = browser.find_elements_by_css_selector('.service-bd li')
lis2 = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')

# 元素交互操作
# 对获取的元素调用交互方法
import time
input = browser.find_element_by_id('q')
input.send_keys('iPhone')
time.sleep(1)
input.clear()
input.send_keys('iPad')
button = browser.find_element_by_class_name("btn-search")
button.click()

# 交互动作
# 将动作附加到动作链中串行执行
from selenium.webdriver import ActionChains
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
# 拖拽的动作
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()

# 执行JavaScript
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
browser.execute_script('alert("to Botton")')

# 获取元素信息
# 获取属性
logo = browser.find_element_by_id('zh-top-link-logo')
print(logo)
print(logo.get_attribute('class'))
# 获取文本值
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.text)
# 获取id、位置、标签名、大小
print(input.id)
print(input.location, input.tag_name, input.size)
# frame
from selenium.common.exceptions import NoSuchElementException
browser = webdriver.Chrome()
url = 'http://'
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
print(source)
try:
    logo = browser.find_element_by_class_name('logo')
except NoSuchElementException:
    print('no logo')
browser.switch_to.parent_frame()
logo = browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)

# 等待
# 隐式等待
browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get('https://www.zhihu.com/explore')
input = browser.find_element_by_class_name('zu-top-add-question')
print(input)
# 显示等待
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
print(input, button)

# 前进后退
browser.back()
time.sleep(1)
browser.forward()

# cookies
print(browser.get_cookies())
browser.add_cookie({'name':'name','domain':'www'})
print(browser.get_cookies())
browser.delete_all_cookies()

# 选显卡管理
browser.get('www.baidu')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1])
browser.get('www.taobao')
time.sleep(1)
browser.switch_to_window(browser.window_handles[0])
browser.get('www.zhihu')

# 异常处理
from selenium.common.exceptions import TimeoutException, NoSuchElementException








