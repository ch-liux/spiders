'''
Created on 2018年8月8日

@author: Administrator
'''

"""
StringIO和BytesIO
"""

from io import StringIO

# f = StringIO()
# f.write('hello')
# print(f.write('hello'))
# print(f.getvalue())

# f = StringIO('Hello\nWorld\nGoodbye!')
# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s)

"""
BytesIO
"""
from io import BytesIO

f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read().decode('utf-8'))










