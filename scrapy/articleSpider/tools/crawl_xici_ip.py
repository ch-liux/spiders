#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'lxzy'
import requests
from scrapy.selector import Selector
import re
import pymysql


conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                       password='123456', db='python', charset='utf8')
cursor = conn.cursor()


def crawl_ips():
    # 爬取西刺免费IP代理
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    response = requests.get('http://www.xicidaili.com/nn/', headers=header)

    next_page = re.compile('<a class="next_page".*?href="/nn/(\d+)">').findall(response.text)
    if next_page:
        next_page = next_page[0]
    selector = Selector(text=response.text)
    all_trs = selector.css("#ip_list tr")

    ip_list = []
    for tr in all_trs[1:]:
        speed_str = tr.css('.bar::attr(title)').extract()[0]
        if speed_str:
            speed = float(speed_str.split("秒")[0])
        all_texts = tr.css("td::text").extract()
        ip = all_texts[0]
        port = all_texts[1]
        proxy_type = all_texts[5]
        if proxy_type is None:
            proxy_type = "HTTP"
        ip_list.append((ip, port, proxy_type, speed))
        ips = (ip, port, proxy_type, speed)
        cursor.execute("insert into xici_ips(ip, port, proxy_type, speed) values(%s, %s, %s, %s)", ips)
        conn.commit()


class GetIP(object):
    def check_ip(self, ip, port):
        http_url = "http://www.baidu.com"
        proxy_url = "http://{0}:{1}".format(ip, port)
        try:
            proxy_dict = {
                "http":proxy_url
            }
            response = requests.get(http_url, proxies=proxy_dict)
            return True
        except Exception as e:
            print("ip is error >>>"+ip)
            self.delete_ip(ip)
            return False
        else:
            code = response.status_code
            if code <= 200 and code < 300:
                print("ip is ok >>>"+ip)
                return True
            else:
                print("invalid ip and port >>>"+ip)
                self.delete_ip(ip)
                return False

    def delete_ip(self, ip):
        d_sql = "delete from xici_ips where ip = '{0}'".format(ip)
        cursor.execute(d_sql)
        conn.commit()
        return True

    def get_random_ip(self):
        cursor.execute("select ip, port from xici_ips order by rand() limit 1")
        row = cursor.fetchone()
        result_ip = self.check_ip(row[0],row[1])
        if result_ip:
            return "http://{0}:{1}".format(row[0], row[1])
        else:
            return self.get_random_ip()


if __name__ == "__main__":
    # crawl_ips()
    ip = GetIP()
    print(ip.get_random_ip())