'''
Created on 2018年8月14日

@author: Administrator
'''

"""多线程"""

# import time, threading
# def loop():
#     print("thread %s is running..." % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#         print('thread %s ended.' % threading.current_thread().name)
# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThraed')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)
        
"""LOCK"""
# import time, threading
# balance = 0
# def change_it(n):
#     global balance
#     balance = balance + n
#     balance = balance - n
# def run_thread(n):
#     for i in range(100000):
#         change_it(n)
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)#0 8
# 
# balance = 0
# lock = threading.Lock()
# 
# def run_thread2(n):
#     for i in range(100000):
#         lock.acquire()
#         try:
#             change_it(n)
#         finally:
#             lock.release()
# t1 = threading.Thread(target=run_thread2, args=(5,))
# t2 = threading.Thread(target=run_thread2, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)#0

"""多核CPU"""
import threading, multiprocessing
# 死循环
def loop():
    x = 0
    while True:
        x =  x^1
for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()























