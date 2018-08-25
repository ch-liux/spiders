# -*- coding: utf-8 -*-
import scrapy


class A51jobSpider(scrapy.Spider):
    name = '51job'
    allowed_domains = ['www.51job.com']
    start_urls = ['http://www.51job.com/']


    def start_requests(self):
        keyword = 'python'
        hd = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
        params = {
            "fromJs": "1",
            "jobarea": "040000",
            'keyword': keyword,
            "keywordtype": "2",
            "curr_page": "1"
        }
        url = "http://search.51job.com/jobsearch/search_result.php"
        scrapy.Request(url=url, body=params, headers=hd, callback=self.parse)


    def parse(self, response):
        print(response.text)
