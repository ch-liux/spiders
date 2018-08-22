# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
from urllib import parse
import datetime
from articleSpider.items import ArticleItem, ArticleItemLoader
from articleSpider.utils.common import get_md5
from scrapy.loader import ItemLoader


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        # post_urls = response.xpath('//div[@class="post-meta"]/p/a[@class="archive-title"]/@href').extract()
        # post_imgs = response.xpath('//div[@id="archive"]/div[@class="post floated-thumb"]/div[@class="post-thumb"]/a/img/@src').extract()
        post_nodes = response.css(".floated-thumb .post-thumb a")
        if post_nodes:
            for post_node in post_nodes:
                image_url = post_node.css("img::attr(src)").extract_first("")
                post_url = post_node.css("::attr(href)").extract_first("")
                yield Request(url=parse.urljoin(response.url, post_url), meta={"front_image_url":image_url}, callback=self.parse_detail)

        next_url = response.css(".next.page-numbers::attr(href)").extract_first("")
        if next_url:
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_detail(self, response):
        # 通过itemLoader加载item
        article_item = ArticleItem()
        item_loader = ArticleItemLoader(item=ArticleItem(), response=response)

        front_image_url = response.meta.get("front_image_url", "")

        item_loader.add_css("title", ".entry-header h1::text")
        item_loader.add_value("url", response.url)
        item_loader.add_value("url_object_id", get_md5(response.url))
        item_loader.add_css("create_date", "p.entry-meta-hide-on-mobile::text")
        item_loader.add_value("front_image_url", [front_image_url])
        item_loader.add_css("praise_nums", ".vote-post-up h10::text")
        item_loader.add_css("comment_nums", "a[href='#article-comment'] span::text")
        item_loader.add_css("fav_nums", ".bookmark-btn::text")
        item_loader.add_css("tags", "p.entry-meta-hide-on-mobile a::text")
        item_loader.add_css("content", "div.entry")

        article_item = item_loader.load_item()
        yield article_item