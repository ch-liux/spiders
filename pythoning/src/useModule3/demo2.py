'''
Created on 2018年8月18日

@author: Administrator
'''

"""requests
"""

import requests
# r = requests.get('https://www.douban.com/')
# print(r.status_code)
# print(r.text)


url = 'https://www.douban.com/'
# r = requests.get(url, params={'q':'python', 'cat':'1001'})
# print(r.url)
# print(r.encoding)
# print(r.content)


# r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# print(r.json())
'''传入HTTP Header时，我们传入一个dict作为headers参数'''
# r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# print(r.text)
'''发送POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据'''
# r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
# print(r.text)
'''上传文件需要更复杂的编码格式，但是requests把它简化成files参数'''
# upload_files = {'file': open('report.xls', 'rb')}
# r = requests.post(url, files=upload_files)

# r = requests.get(url, params={'q':'python', 'cat':'1001'})
# print(r.headers)
# print(r.headers['Content-Type'])
"""请求中传入Cookie，只需准备一个dict传入cookies参数"""
# cs = {'token': '12345', 'status': 'working'}
# r = requests.get(url, cookies=cs)
"""指定超时，传入以秒为单位的timeout参数"""
r = requests.get(url, timeout=2.5) # 2.5秒后超时


