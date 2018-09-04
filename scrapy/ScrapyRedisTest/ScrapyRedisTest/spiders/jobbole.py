#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from scrapy_redis.spiders import RedisSpider
from scrapy.http import Request
from urllib import parse

class JobboleSpider(RedisSpider):
    name = 'jobbole'
    redis_key = 'jobbole:start_urls'
    allowed_domains = ['blog.jobbole.com']
    # start_urls = ['http://blog.jobbole.com/all-posts/']

    handle_httpstatus_list = [404]

    def parse(self, response):
        if response.status == 404:
            self.fail_urls.append(response.url)
            self.crawler.stats.inc_value("failed_url")

        post_nodes = response.css("#archive .floated-thumb .post-thumb a")
        if post_nodes:
            for post_node in post_nodes:
                image_url = post_node.css("img::attr(src)").extract_first("")
                post_url = post_node.css("::attr(href)").extract_first("")
                yield Request(url=parse.urljoin(response.url, post_url), meta={"front_image_url":image_url}, callback=self.parse_detail)

            # next_url = response.css(".next.page-numbers::attr(href)").extract_first("")
            # if next_url:
            #     yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_detail(self, response):
        pass

