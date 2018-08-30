'''
Created on 2018年8月14日

@author: Administrator
'''

"""
多进程
"""

# import os
# from multiprocessing import Process
# 
# print(os.getpid())
"""multiprocessing"""
# # pid = os.fork()  # linux/unix/mac
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')
"""Pool"""
# from multiprocessing import Pool
# import os, time, random
# def long_time_task(name):
#     print(name, os.getpid())
#     start = time.time()
#     time.sleep(random.random() *3)
#     end = time.time()
#     print(name, (end-start))
# if __name__ == '__main__':
#     print(os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('.....')
#     # 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
#     p.close()
#     p.join()
#     print(";;;;;;")

"""子进程"""
# import subprocess
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code:', r)
# 
# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output)
# # print(output.decode('utf-8'))
# print('Exit code:', p.returncode)

"""进程间通信"""
from multiprocessing import Process, Queue
import os, time, random
# 写数据进程执行代码
def write(q):
    print(os.getpid())
    for value in ['a', 'b', 'c']:
        print('set value is %s' % value)
        q.put(value)
        time.sleep(random.random())
# 读取进程执行代码
def read(q):
    print(os.getpid())
    while True:
        value = q.get(True)
        print('get value is %s' % value)
if __name__ == "__main__":
    # 父进程创建queue，传给子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动pw
    pw.start()
#     time.sleep(10)
    # 启动pr
    pr.start()
    # 等待pw结束
    pw.join()
    # 终止死循环
    pr.terminate()






