import redis
import pymysql
import urllib.request
import re
rconn=redis.Redis("172.17.0.2","6379")
#url:http://www.17k.com/book/2.html
'''
url-i-"1"
'''
for i in range(0,5459058):
    isdo=rconn.hget("url",str(i))
    if(isdo!=None):
        continue
    rconn.hset("url",str(i),"1")
    try:
        data=urllib.request.urlopen("http://www.17k.com/book/"+str(i)+".html").read().decode("utf-8","ignore")
    except Exception as err:
        print(str(i)+"----"+str(err))
        continue
    pat='<a class="red" .*?>(.*?)</a>'
    rst=re.compile(pat,re.S).findall(data)
    if(len(rst)==0):
        continue
    name=rst[0]
    print(str(i)+"-----"+str("ok"))
    rconn.hset("rst",str(i),str(name))
