'''
Created on 2018年8月16日

@author: Administrator
'''

"""base64"""
import base64
# base64长度是4的倍数
b64 = base64.b64encode(b'123456b64 = base64.b64encode')
print(b64)
b64 = base64.b64decode(b64)
print(b64)
ub64 = base64.urlsafe_b64encode(b"i\xb7\x1d\xfb\xef\xff")
print(ub64)
ub64 = base64.urlsafe_b64decode(ub64)
print(ub64)

b64 = base64.b64encode(b'abcd')
print(b64)
b64 = base64.b64decode(b'YWJjZA==')
print(b64)
print(len('MTIzNDU2YjY0ID0gYmFzZTY0LmI2NGVuY29kZQ=='))


