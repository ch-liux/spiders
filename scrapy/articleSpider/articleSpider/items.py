# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy, datetime, re
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from articleSpider.utils.common import extract_num
from w3lib.html import remove_tags



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
    front_image_url = scrapy.Field(input_processor=MapCompose(return_value),output_processor=Join(','))
    front_image_path = scrapy.Field()

    def get_sql(self):
        insert_sql = """
            insert into 
            jobbole_article(title, create_date, url, url_object_id, front_image_url,
            front_image_path, comment_nums, fav_nums, praise_nums, tags, content)  
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (self["title"], self["create_date"], self["url"], self["url_object_id"], self["front_image_url"][0],
                  self["front_image_path"], self["comment_nums"], self["fav_nums"], self["praise_nums"], self["tags"],
                  self["content"])
        return insert_sql, params


class ZhihuQuestionItem(scrapy.Item):
    zhihu_id = scrapy.Field()
    topics = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    answer_num = scrapy.Field()
    comments_num = scrapy.Field()
    watch_user_num = scrapy.Field()
    click_num = scrapy.Field()
    crawl_time = scrapy.Field()

    def get_sql(self):
        insert_sql = """
            insert into 
            zhihu_question(zhihu_id, topics, url, title, content, create_time, update_time, 
            answer_num, comments_num, watch_user_num, click_num, crawl_time, crawl_update_time)    
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)  
            ON DUPLICATE KEY UPDATE content=VALUES(content),answer_num=VALUES(answer_num),
            comments_num=VALUES(comments_num),click_num=VALUES(click_num),watch_user_num=VALUES(watch_user_num)
        """
        zhihu_id = self["zhihu_id"][0]
        topics = ",".join(self["topics"])
        url = self["url"][0]
        title = "".join(self["title"])
        content = "".join(self["content"])
        answer_num = extract_num("".join(self["answer_num"]))
        comments_num = extract_num("".join(self["comments_num"]))
        click_num = extract_num("".join(self["click_num"]))
        watch_user_num = extract_num("".join(self["watch_user_num"]))
        crawl_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        create_time = datetime.datetime.now(self["create_time"]).strftime("%Y-%m-%d %H:%M:%S")
        update_time = datetime.datetime.now(self["update_time"]).strftime("%Y-%m-%d %H:%M:%S")
        crawl_update_time = datetime.datetime.now(self["crawl_update_time"]).strftime("%Y-%m-%d %H:%M:%S")
        params = (zhihu_id, topics, url, title,
                  content, create_time, update_time,
                  answer_num, comments_num, watch_user_num,
                  click_num, crawl_time, crawl_update_time)
        return insert_sql, params


class ZhihuAnswerItem(scrapy.Item):
    zhihu_id = scrapy.Field()
    url = scrapy.Field()
    question_id = scrapy.Field()
    author_id = scrapy.Field()
    content = scrapy.Field()
    parise_num = scrapy.Field()
    comments_num = scrapy.Field()
    create_time = scrapy.Field()
    update_time = scrapy.Field()
    crawl_time = scrapy.Field()

    def get_sql(self):
        insert_sql = """
            insert into 
            zhihu_answer(zhihu_id, url, question_id, author_id, content,
            praise_num, commnets_num, create_time, update_time, crawl_time, crawl_update_time)   
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)  
            ON DUPLICATE KEY UPDATE content=VALUES(content), comments_num=VALUES(comments_num),
            praise_num=VALUES(praise_num), update_time=VALUES(update_time)
        """
        create_time = datetime.datetime.fromtimestamp(self["create_time"]).strftime("%Y-%m-%d %H:%M:%S")
        update_time = datetime.datetime.fromtimestamp(self["update_time"]).strftime("%Y-%m-%d %H:%M:%S")
        params = (self["zhihu_id"], self["url"], self["question_id"], self["author_id"],
                  self["content"], self["praise_num"], self["commnets_num"], create_time,
                  update_time, self["crawl_time"].strftime("%Y-%m-%d %H:%M:%S"), self["crawl_update_time"].strftime("%Y-%m-%d %H:%M:%S"))
        return insert_sql, params


def remove_splash(value):
    return value.replace("/", "")


def handle_jobaddr(value):
    addr_list = value.split("\n")
    addr_list = [item.strip() for item in addr_list if item.strip() != '查看地图']
    return "".join(addr_list)


class LagouJobItem(scrapy.Item):
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    title = scrapy.Field()
    salary = scrapy.Field()
    job_city = scrapy.Field(
        input_processor=MapCompose(remove_splash),
    )
    work_years = scrapy.Field(
        input_processor=MapCompose(remove_splash),
    )
    degree_need = scrapy.Field(
        input_processor=MapCompose(remove_splash),
    )
    job_type = scrapy.Field()
    pulish_time = scrapy.Field()
    tags = scrapy.Field()
    job_advantage = scrapy.Field()
    job_desc = scrapy.Field()
    job_addr = scrapy.Field(
        input_processor=MapCompose(remove_tags, handle_jobaddr),
    )
    company_url = scrapy.Field()
    company_name = scrapy.Field()
    crawl_time = scrapy.Field()
    crawl_update_time = scrapy.Field()


class LagouJobItemLoader(ItemLoader):
    # 自定义itemLoader
    default_output_processor = TakeFirst()