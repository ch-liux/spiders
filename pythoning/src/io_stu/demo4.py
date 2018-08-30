'''
Created on 2018年8月10日

@author: Administrator
'''

"""
获取当前目录下所有文件
"""

import os

path = os.path.abspath('.')
print(path)
lists = os.listdir()
farr = list()
darr = list()

def parse(lists):
    for l in lists:
        temp = os.path.isdir(l)
        if temp:
            farr.append(l)
            ls = os.listdir(l)
            parse(ls)
        else:
            darr.append(l)

parse(lists)
print(farr)
print(darr)

