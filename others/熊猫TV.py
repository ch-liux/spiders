
# 熊猫TV 英雄联盟 主播
import urllib.request
import re
import ssl
#from lxml import etree

ssl._create_default_https_context = ssl._create_unverified_context

headers = ("user-agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)
# ?pageno=2&pagenum=120&order=top&classification=lol&token=
url = "https://www.panda.tv/cate/lol"
data = urllib.request.urlopen(url).read().decode("utf-8")

divpa = '<div class="list-container">(.*?)</div>'
div = re.compile(divpa, re.S).findall(data)
userpa = '<div class="video-info">(.*?)</div>'
userlist = re.compile(userpa, re.S).findall(data)
# 获取主播名字 - 观看量
for user in userlist:

    namepa = '</i>(.*?)</span>'
    name = re.compile(namepa, re.S).findall(user)
    print("主播名称: "+str(name[0]).strip())

    titlepa = '<span class="video-title".*?>(.*?)</span>' 
    title = re.compile(titlepa, re.S).findall(user)
    print("主播标题: "+str(title[0]))

    levelpa = 'data-level="(.*?)"></i>'
    level = re.compile(levelpa, re.S).findall(user)
    if len(level)==0:
        print("主播等级: "+"MAX")
    else:
        print("主播等级: "+str(level[0]))

    countpa = '<span class="video-number">(.*?)</span>' 
    count = re.compile(countpa, re.S).findall(user)
    print("观看量: "+str(count[0]))
    print("--------------------------------------------------")