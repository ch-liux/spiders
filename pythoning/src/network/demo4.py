'''
Created on 2018年8月20日

@author: Administrator
'''

"""UDP编程
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 8089))
s.listen(5)

print('Bind  udp on 8089...')
while True:
    data, addr = s.recv(1024)
    print("data from %s:%" % addr)
    s.sendto(b'ok, %s' % data, addr)





