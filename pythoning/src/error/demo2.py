'''
Created on 2018年8月7日

@author: Administrator
'''
"""
调试
"""

# print()
# assert断言
# logging
# pdb调试器
import logging
import pdb
# debug，info，warning，error
logging.basicConfig(level=logging.INFO)
def fn():
    a = 1
    print(a)
    assert a == 1, 'n is not 1'
    logging.info("a is %s" % str(a))

fn()
pdb.set_trace()#p查看变量，或者用命令c继续运行
print('11')



