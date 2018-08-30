'''
Created on 2018年8月21日

@author: Administrator
'''

# environ：一个包含所有HTTP请求信息的dict对象；
# start_response：一个发送HTTP响应的函数。

# 注意Header只能发送一次，也就是只能调用一次start_response()函数。
# start_response()函数接收两个参数，一个是HTTP响应码，一个是一组list表示的HTTP Header，每个Header用一个包含两个str的tuple表示
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']