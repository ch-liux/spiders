'''
Created on 2018年8月7日

@author: Administrator
'''
"""
错误处理
"""
import logging
try:
    pass
except Exception as e:
    logging.exception(e)
finally:
    pass
# n = 0
# if n==0:
#     raise ValueError("this is value:%s" % str(n))

# try:
#     10/0
# except ZeroDivisionError:
#     raise ValueError("input error")

from functools import reduce
def str2num(s):
    return int(s)
def add(n, m):
    return n+m
def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    if True:
        return reduce(add, ns)
    return reduce(lambda x,y:x+y, ns)
def main():
    r = calc('1+2+3')
    print(r)
main()





