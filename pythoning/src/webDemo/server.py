'''
Created on 2018年8月21日

@author: Administrator
'''

from wsgiref.simple_server import make_server
from webDemo.hello import application

httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000')
httpd.serve_forever()