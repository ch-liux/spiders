'''
Created on 2018年8月16日

@author: Administrator
'''

"""
contextlib
"""

# try:
#     f = open('demo1.py', 'r', encoding='utf-8')
#     f.read()
# finally:
#     if f:
#         f.close()

# with open('demo1.py', 'r', encoding='utf-8') as f:
#     f.read()

# class Query(object):
#     def __init__(self, name):
#         self.name = name
#     def __enter__(self):
#         print('Begin')
#         return self
#     def __exit__(self, exc_type, exc_value, traceback):
#         if exc_type:
#             print('Error')
#         else:
#             print('End')
#     def query(self):
#         print('Query info about %s...' % self.name)
# 
# with Query('Bob') as q:
#     q.query()

"""@contextmanager"""
from contextlib import contextmanager
# class Query(object):
#     def __init__(self, name):
#         self.name = name
#     def query(self):
#         print('Query info about %s...' % self.name)
# @contextmanager
# def create_query(name):
#     print('Begin')
#     q = Query(name)
#     yield q
#     print('End')
# with create_query('Bob') as q:
#     q.query()
# # @contextmanager让我们通过编写generator来简化上下文管理
# @contextmanager
# def tag(name):
#     print("<%s>" % name)
#     yield
#     print("</%s>" % name)
# with tag('h1'):
#     print('hello')
#     print('world')

"""@closing"""
from contextlib import closing
from urllib.request import urlopen
with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()















