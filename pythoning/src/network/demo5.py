'''
Created on 2018年8月20日

@author: Administrator
'''

"""udp客服端
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for data in [b'marry', b'jack']:
    s.send(data, ("127.0.0.1", 8089))
    print(s.recv(1024).decode('utf-8'))
s.close()

