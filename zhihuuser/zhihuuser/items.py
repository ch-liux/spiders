# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field


class UserItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    id = Field()
    name = Field()
    avatar_url = Field()    #头像
    answer_count = Field()  #回答数
    follower_count = Field()    #关注数
    articles_count = Field()
    avatar_url_template = Field()
    type = Field()
    url = Field()
    url_token = Field()
    user_type = Field()




