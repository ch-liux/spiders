'''
Created on 2018年8月16日

@author: Administrator
'''
"""
hmac
哈希算法
"""
import hmac
msg = b'Hello, world!'
key = b'secret'
h = hmac.new(key, msg, digestmod='MD5')
# h = hmac.new(key, msg, digestmod='SHA1')
print(h.hexdigest())





