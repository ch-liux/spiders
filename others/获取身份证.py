    
import re
import urllib.request

url ='http://sfz.ckd.cc/'
for i in range(0,10):
    data = urllib.request.urlopen(url).read().decode('utf-8', 'ignore')
    datapa = '<tr><td>(.*?)</td>.*?<tr>'
    sfz = re.compile(datapa, re.S).findall(data)
    print(sfz)
    with open('sfz.txt', 'a', encoding='utf-8') as f:
        temp = sfz[0] + '\n' + sfz[1] + '\n' + sfz[2] + '\n' + sfz[3] + '\n' + sfz[4] + '\n' + sfz[5] + '\n' + sfz[6] + '\n' + sfz[7] + '\n' + sfz[8] + '\n'
        f.write(temp)
        f.close



