'''
Created on 2018年8月16日

@author: Administrator
'''


"""
hashlib
摘要算法简介
"""
import hashlib
# MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。
sha1 = hashlib.sha1()
sha1.update('how to use md5 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

def set_password_md5(password):
    md5 = hashlib.md5()
    pw = password + 'theSalt'
    md5.update(pw.encode('utf-8'))#加盐
    return md5.hexdigest()

pw = set_password_md5('123456')
print(pw)
