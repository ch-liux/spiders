'''
Created on 2018年8月16日

@author: Administrator
'''

"""
itertools
Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
"""
import itertools
# 无限月读，数字
# na = itertools.count(1)
# for n in na:
#     print(n)

# 无限月读，ABC
# na = itertools.cycle('ABC')
# for n in na:
#     print(n)

#
# na = itertools.repeat('A', 3)
# for n in na:
#     print(n)

# ns = itertools.count(1)
# na = itertools.takewhile(lambda x:x<10, ns)
# print(list(na))

"""
chain()
chain()可以把一组迭代对象串联起来，形成一个更大的迭代器"""
for c in itertools.chain('abc', 'dfg'):
    print(c)

"""
groupby()
groupby()把迭代器中相邻的重复元素挑出来放在一起"""
for key,group in itertools.groupby('aabbbccccca'):
    print(key, list(group))

for key,group in itertools.groupby('AaBbbbbbdccC', lambda x:x.upper()):
    print(key, list(group))




