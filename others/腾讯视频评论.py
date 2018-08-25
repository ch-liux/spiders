
#
import re
import urllib.request

id = '2774518927'   # 动漫ID - 观海策
id = '2369303789'   # 斗罗大陆
id = '2850613872'   # 魔道祖师
ids = ['2774518927', '2369303789', '2850613872']

def printName(temp):
    if int(temp)==0:
        print("=====================================")
        print("观海策")
        print("=====================================")
    elif int(temp)==1:
        print("=====================================")
        print("斗罗大陆")
        print("=====================================")
    elif int(temp)==2:
        print("=====================================")
        print("魔道祖师")
        print("=====================================")

index = 0
for x in ids:
    cid = '0'           # 翻页ID
    tempid = x
    printName(index)
    for i in range(0, 10):
        url = 'https://video.coral.qq.com/varticle/'+tempid+'/comment/v2?callback=_varticle'+tempid+'commentv2&orinum=10&oriorder=o&pageflag=1&cursor='+cid+'&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=9'
        data = urllib.request.urlopen(url).read().decode('utf-8', 'ignore')
        datapa = '"content":"(.*?)"'
        content = re.compile(datapa, re.S).findall(data)
        lastpa = '"last":"(.*?)"'
        cid = re.compile(lastpa, re.S).findall(data)[0]
        print("***第"+str(i+1)+"页")
        for c in content:
            # print(c)
            print("---------------")
            try:
                print(eval('u"'+c+'"'))
            except UnicodeEncodeError as e:
                print(e)
    index+=1

