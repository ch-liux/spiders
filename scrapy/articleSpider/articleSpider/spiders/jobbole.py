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
        article_item = ArticleItem()
        # title=标题, create_date=创建时间, praise_nums=点赞数
        # fav_nums=收藏数, comment_nums=评论数, tags=标签
        # front_image_url=封面图
        # title:xpath选择器
        # title = response.xpath('//div[@class="entry-header"]/h1/text()').extract()[0]
        # # ctitle:css选择器
        # # ctitle = response.css('.entry-header h1::text').extract()[0]
        # create_date = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0].replace('·', '').strip()
        # praise_nums = response.xpath("//span[contains(@class, 'vote-post-up')]/h10/text()").extract()[0]
        # if praise_nums == None:
        #     praise_nums = 0
        # else:
        #     praise_nums = int(praise_nums)
        # fav_temp = response.xpath("//span[contains(@class, 'bookmark-btn')]/text()").extract()[0]
        # if fav_temp:
        #     fav_nums = re.match('.*(\d+).*', fav_temp)
        #     if fav_nums:
        #         fav_nums = int(fav_nums.group(1))
        #     else:
        #         fav_nums = 0
        # comment_temp = response.xpath('//a[@href="#article-comment"]/span/text()').extract()[0]
        # if comment_temp:
        #     comment_nums = re.match('.*(\d+).*', comment_temp)
        #     if comment_nums:
        #         comment_nums = int(comment_nums.group(1))
        #     else:
        #         comment_nums = 0
        # content = response.xpath('//div[@class="entry"]').extract()[0]
        # tag_list = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a/text()').extract()
        # if tag_list:
        #     tag_list = [element for element in tag_list if not element .strip().endswith("评论")]
        #     tags = ','.join(tag_list)
        # # image_url = response.meta["front_image_url"]
        # front_image_url = response.meta.get("front_image_url", "")
        # article_item["title"] = title
        # try:
        #     create_date = datetime.datetime.striptime(create_date, "%Y-%m-%d").date()
        # except Exception:
        #     create_date = datetime.datetime.now().date()
        # article_item["create_date"] = create_date
        # article_item["praise_nums"] = praise_nums
        # article_item["fav_nums"] = fav_nums
        # article_item["comment_nums"] = comment_nums
        # article_item["content"] = content
        # article_item["tags"] = tags
        # article_item["url"] = response.url
        # article_item["front_image_url"] = [front_image_url]
        # article_item["url_object_id"] = get_md5(response.url)
        # print(title, create_date, praise_nums, fav_nums, comment_nums, content, tags)

        # 通过itemLoader加载item
        item_loader = ArticleItemLoader(item=ArticleItem(), response=response)
        item_loader.add_css("title", ".entry-header h1::text")
        # item_loader.add_xpath()
        front_image_url = response.meta.get("front_image_url", "")
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