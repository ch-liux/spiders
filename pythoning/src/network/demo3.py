'''
Created on 2018年8月20日

@author: Administrator
'''

"""客户端
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8089))
print("server:"+s.recv(1024).decode('utf-8'))
while True:
    data = input("input send msg:")
    if data == 'exit':
        break
    else:
        s.send(data.encode(encoding='utf_8'))
        print(s.recv(1024).decode('utf-8'))
# for data in [b'Tom', b'Jack', b'Mary']:
#     s.send(data)
#     print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
