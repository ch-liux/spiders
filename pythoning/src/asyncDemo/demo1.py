'''
Created on 2018年8月21日

@author: Administrator
'''

"""
asyncio
"""
import asyncio
import threading

@asyncio.coroutine
def hello(index):
    print("Hello, world %s:(%s)" % (index,threading.currentThread()))
    # 异步调用asyncio.sleep(1)
    yield from asyncio.sleep(1)
    print("Hello, end %s:(%s) " % (index,threading.currentThread()))

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(asyncio.wait([hello(1),hello(2)]))
# loop.run_until_complete(hello(2))
loop.close()

