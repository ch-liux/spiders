'''
Created on 2018年8月21日

@author: Administrator
'''

"""协程
"""

# def A():
#     print('1')
#     print('2')
#     print('3')
# 
# def B():
#     print('x')
#     print('y')
#     print('z')
# A()
# B()

"""
yield常见用法：该关键字用于函数中会把函数包装为generator。然后可以对该generator进行迭代: for x in fun(param).
按照我的理解，可以把yield的功效理解为暂停和播放。
在一个函数中，程序执行到yield语句的时候，程序暂停，返回yield后面表达式的值，在下一次调用的时候，从yield语句暂停的地方继续执行，如此循环，直到函数执行完。
扩展：
next函数与send函数很相似，都能获得生成器的下一个yield后面表达式的值，不同的是send函数可以向生成器传参。
yield from:封装包含yield的函数，使得子函数也为一个generator.
"""
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)