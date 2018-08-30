'''
Created on 2018年8月15日

@author: Administrator
'''

from datetime import datetime,timedelta

now = datetime.now()
print(now)
setd = datetime(1994, 7, 20, 19, 20, 21, 6)
print(setd)
print(setd.time())
print(setd.date())
print(setd.timestamp())
temp = setd.timestamp()
print(datetime.fromtimestamp(temp))
print(datetime.utcfromtimestamp(temp))
strd = '1994-07-20 19:20:16'
print(datetime.strptime(strd, '%Y-%m-%d %H:%M:%S'))
print(setd.strftime('%Y-%m-%d %H:%M:%S'))
print(setd.strftime('%a, %b %d %H:%M'))
at = now + timedelta(days=1, hours=10)
print(at)


