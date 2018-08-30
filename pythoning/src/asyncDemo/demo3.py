'''
Created on 2018年8月21日

@author: Administrator
'''

"""async/await"""

import asyncio

@asyncio.coroutine
def hello():
    print('Hello,world')
    yield from asyncio.sleep(1)
    print("Hello end")
 
loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
# loop.run_until_complete(asyncio.wait(["a",'b']))
# loop.close()

async def hello2():
    print("begin...")
    await asyncio.sleep(1)
    print('end')
loop = asyncio.get_event_loop()
loop.run_until_complete(hello2())
loop.close()
