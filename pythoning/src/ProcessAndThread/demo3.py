'''
Created on 2018年8月15日

@author: Administrator
'''

"""ThreadLocal"""
class Student(object):
    def __init__(self, name):
        self.name = name
# 每个方法都需要传入std变量      
# def process_student(name):
#     std = Student(name)
#     do_task1(std)
#     do_task2(std)
# def do_task1(std):
#     do_subtask1(std)
#     do_subtask2(std)
# def do_task2(std):
#     do_subtask1(std)
#     do_subtask2(std)
# def do_subtask1(std):
#     print(std)
# def do_subtask2(std):
#     print(std)
# import threading
# global_dict = {}
# # 共享/全局
# def std_thread(name):
#     std = Student(name)
#     global_dict[threading.current_thread()] = std
#     do_task1()
#     do_task2()
# def do_task1():
#     std = global_dict[threading.current_thread()]
# def do_task2():
#     std = global_dict[threading.current_thread()]

import threading
# 创建全局ThreadLocal对象:
local_school = threading.local()
def process_student():
    # 获取当前线程关联的student:
    std = local_school.name
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))
def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.name = name
    process_student()
t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()




