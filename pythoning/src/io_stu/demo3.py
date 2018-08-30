'''
Created on 2018年8月10日

@author: Administrator
'''
"""
操作文件和目录
"""

import os

print(os.name)
# windows不提供
# print(os.uname())

# 环境变量
print(os.environ)
print(os.environ.get('PATH'))
print(os.environ.get('x', 'default'))

# 目录/文件
print(os.path.abspath('.')) #当前文件的路径
p = os.path.abspath('.')
os.path.join(p, 'testdir')  #表示新建目录路径
os.makedirs(p+'\\testdir')  #新建目录 
os.rmdir(p+'\\testdir')     #移除目录
# liunx=/ win=\
print(os.path.split(p))     #拆分路径
# os.renames('t.txt', 'test.txt') #文件重命名
# os.remove('test.py')        #移除文件
# 是目录
print([x for x in os.listdir('.') if os.path.isdir(x)])
# 列出当前目录下后缀名为.PY
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])







