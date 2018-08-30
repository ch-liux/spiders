'''
Created on 2018年8月15日

@author: Administrator
'''


"""分布式进程"""
import random, queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

# 发送队列任务
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()

# 从baseManager继承QueueManager
class QueueManager(BaseManager):
    pass

def return_task_queue():
    global task_queue
    return task_queue
def return_result_queue():
    global result_queue
    return result_queue

def run_test():
    # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
    # win 不支持
#     QueueManager.register("get_task_queue", callable=lambda:task_queue)
#     QueueManager.register("get_result_queue", callable=lambda:result_queue)
    QueueManager.register("get_task_queue", callable=return_task_queue)
    QueueManager.register("get_result_queue", callable=return_result_queue)
    # 绑定端口5000，并设置密码‘abc’
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    # 启动Queue
    manager.start()
    # 获得通过网络访问的queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 加入任务
    for i in range(10):
        n = random.randint(0, 10000)
        print("put task %d..." % n)
        task.put(n)
    # result队列读取结果
    print("try get result...")
    for i in range(10):
        r = result.get(timeout=10)
        print("result %s" % r)
    # 关闭
    manager.shutdown()
    print('master exit.')

if __name__ == '__main__':
    freeze_support()
    run_test()
