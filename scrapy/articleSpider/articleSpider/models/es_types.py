#!/usr/bin/env python 
# -*- coding:utf-8 -*-


from datetime import datetime
from elasticsearch_dsl import Document, Date, Nested, Boolean, \
    analyzer, InnerDoc, Completion, Keyword, Text, Integer

from elasticsearch_dsl.connections import connections
connections.create_connection(hosts=["localhost"])


class ArticleType(Document):
    # 伯乐在线
    title = Text(analyzer="ik_max_word")
    create_date = Date()
    url = Keyword()
    url_object_id = Keyword()
    front_image_url = Keyword()
    front_image_path = Keyword()
    praise_nums = Integer()
    fav_nums = Integer()
    comment_nums = Integer()
    content = Text(analyzer="ik_max_word")
    tags = Text(analyzer="ik_max_word")

    class index:
        index = "jobbole"
        doc_type = "article"


if __name__ == "__main__":
    # 直接生产mapping,有定义的item
    ArticleType.init()