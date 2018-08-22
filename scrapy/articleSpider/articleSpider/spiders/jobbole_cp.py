# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
from urllib import parse
import datetime
from articleSpider.items import ArticleItem
from articleSpider.utils.common import get_md5


class JobboleCpSpider(scrapy.Spider):
    name = 'jobbole_cp'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        post_nodes = response.css("#archive .floated-thumb .post-thumb a")
        if post_nodes:
            for post_node in post_nodes:
                image_url = post_node.css("img::attr(src)").extract_first("")
                post_url = post_node.css("::attr(href)").extract_first("")
                print("==================")
                print("post_url: " + post_url)
                yield Request(url=parse.urljoin(response.url, post_url),
                              meta={"front_image_url":image_url},
                              callback=self.cparse_detail)

        # next_url = response.css(".next.page-numbers::attr(href)").extract_first("")
        # if next_url:
        #     yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    def cparse_detail(self, response):
        # title=标题, create_date=创建时间, praise_nums=点赞数
        # fav_nums=收藏数, comment_nums=评论数, tags=标签
        # front_image_url=封面图
        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract()[0]
        create_date = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0].replace('·', '').strip()
        praise_nums = response.xpath("//span[contains(@class, 'vote-post-up')]/h10/text()").extract()[0]
        if praise_nums:
            praise_nums = int(praise_nums)
        else:
            praise_nums = 0
        fav_temp = response.xpath("//span[contains(@class, 'bookmark-btn')]/text()").extract()[0]
        if fav_temp:
            fav_nums = re.match('.*(\d+).*', fav_temp)
            if fav_nums:
                fav_nums = int(fav_nums.group(1))
            else:
                fav_nums = 0
        comment_temp = response.xpath('//a[@href="#article-comment"]/span/text()').extract()[0]
        if comment_temp:
            comment_nums = re.match('.*(\d+).*', comment_temp)
            if comment_nums:
                comment_nums = int(comment_nums.group(1))
            else:
                comment_nums = 0
        content = response.xpath('//div[@class="entry"]').extract()[0]
        tag_list = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a/text()').extract()
        if tag_list:
            tag_list = [element for element in tag_list if not element .strip().endswith("评论")]
            tags = ','.join(tag_list)
        front_image_url = response.meta.get("front_image_url", "")
        try:
            create_date = datetime.datetime.striptime(create_date, "%Y-%m-%d").date()
        except Exception:
            create_date = datetime.datetime.now().date()

        article_item = ArticleItem()

        article_item["title"] = title
        article_item["create_date"] = create_date
        article_item["praise_nums"] = praise_nums
        article_item["fav_nums"] = fav_nums
        article_item["comment_nums"] = comment_nums
        article_item["content"] = content
        article_item["tags"] = tags
        article_item["url"] = response.url
        article_item["front_image_url"] = [front_image_url]
        article_item["url_object_id"] = get_md5(response.url)

        yield article_item