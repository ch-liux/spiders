# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy, datetime, re
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


def remove_comment_tags(value):
    # 去掉tag中的评论
    if "评论" in value:
        return ""
    else:
        return value


def add_jobbole(value):
    return value+'-baby'


def date_convert(value):
    try:
        create_date = datetime.datetime.striptime(value, "%Y-%m-%d").date()
    except Exception as e:
        create_date = datetime.datetime.now().date()
    return create_date


def return_value(value):
    return value


def get_nums(value):
    nums = re.match('.*(\d+).*', value)
    if nums:
        nums = int(nums.group(1))
    else:
        nums = 0
    return nums


class ArticleItemLoader(ItemLoader):
    # 自定义itemLoader
    default_output_processor = TakeFirst()


class ArticleItem(scrapy.Item):
    title = scrapy.Field()
    create_date = scrapy.Field(input_processor=MapCompose(date_convert),)
    praise_nums = scrapy.Field(input_processor=MapCompose(get_nums),)
    fav_nums = scrapy.Field(input_processor=MapCompose(get_nums),)
    comment_nums = scrapy.Field(input_processor=MapCompose(get_nums),)
    content = scrapy.Field()
    tags = scrapy.Field(input_processor=MapCompose(remove_comment_tags),output_processor=Join(','))
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    front_image_url = scrapy.Field(input_processor=MapCompose(return_value),)
    front_image_path = scrapy.Field()