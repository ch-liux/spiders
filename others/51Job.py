
# 51job
import requests
import re
from lxml import etree
import pymysql

keyword = 'java'
hd = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
# 薪资范围
price = {'01':'2k-','02':'2-3k','03':'3-4.5k','04':'4.5-6k','05':'6-8k','06':'8-10k','07':'1-1.5w',
    '08':'1.5-2w','09':'2-3w','03':'3-4w'}
# 学历要求
degreefrom = {'01':'初中-','02':'高中/中专','03':'大专','04':'本科','05':'硕士','06':'博士'}
# 工作年限
workyear = {'01':'无','02':'1-3','03':'3-5','04':'5-10','05':'10+'}
# param
params = {
    "fromJs":"1",
    "jobarea":"040000",
    'keyword':keyword,
    "keywordtype":"2",
    "curr_page":"1"
}

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db="python", port=3306, charset='utf8')
cur = conn.cursor()
url = "http://search.51job.com/jobsearch/search_result.php"
response = requests.get(url, params=params, headers=hd)
data = bytes(response.text, response.encoding).decode('gbk','ignore')
pagepa = '共(.*?)条职位'
page = re.compile(pagepa, re.S).findall(data)[0]
for i in range(0, int(page)):
    thisparams = {
        "fromJs":"1",
        "jobarea":"040000",
        'keyword':keyword,
        "keywordtype":"2",
        "curr_page":str(i+1)
    }
    thisresponse = requests.get(url, params=thisparams, headers=hd)
    thisdata = bytes(thisresponse.text,thisresponse.encoding).decode("gbk","ignore")
    dataUrlPa = '<span>.*?<a target="_blank" title=".*?href="(.*?)" onmousedown="">'
    dataUrl = re.compile(dataUrlPa, re.S).findall(thisdata)
    companyResponse = requests.get(dataUrl[0])
    company = bytes(companyResponse.text, companyResponse.encoding).decode("gbk","ignore")
    html = etree.HTML(company)
    companyName = html.xpath('//p/a/@title')[0]
    companyJob = html.xpath('//h1/@title')[0]
    companyJobArea = html.xpath('//div/span[@class="lname"]/text()')[0]
    companyTypeMsg = html.xpath('//p[@class="msg ltype"]/text()')[0]
    companyTypeMsg = str.strip(companyTypeMsg)
    companySkey = html.xpath('//span[@class="sp4"]/text()')
    companySkey = "&&".join(companySkey)
    companyWelfare = html.xpath('//p[@class="t2"]/span/text()')
    companyWelfare = "&&".join(companySkey)
    companyJobMsg = html.xpath('//div[@class="bmsg job_msg inbox"]/p/text()')
    companyJobMsg = "&&".join(companyJobMsg)
    companyJsonPirce = html.xpath('//div[@class="cn"]/strong/text()')[0]
    print(companyName)
    print(companyJob)
    print(companyJobArea)
    print(companyTypeMsg)
    print(companySkey)
    print(companyWelfare)
    print(companyJobMsg)
    print(companyJsonPirce)
    sql = """
    insert into 51_job(job,company_name,company_job,company_job_area,company_type_msg,company_skey,company_welfare,company_job_msg,company_job_price)
     values(%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    cur.execute(sql, (keyword,companyName,companyJob,companyJobArea,companyTypeMsg,companySkey,companyWelfare,companyJobMsg,companyJsonPirce))
    conn.commit()
conn.close()


