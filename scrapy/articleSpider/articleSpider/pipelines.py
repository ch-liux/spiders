# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy.exporters import JsonItemExporter
import codecs, json, pymysql
from twisted.enterprise import adbapi



# 跟数据存储相关
class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item


# mysql插入,采用同步的机制
class MysqlPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',
                                    password='123456', db='python', charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = """
            insert into 
            jobbole_article(title, create_date, url, url_object_id, front_image_url,
            front_image_path, comment_nums, fav_nums, praise_nums, tags, content)  
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (item["title"], item["create_date"], item["url"], item["url_object_id"], item["front_image_url"][0], item["front_image_path"], item["comment_nums"], item["fav_nums"], item["praise_nums"], item["tags"], item["content"])
        try:
            self.cursor.execute(insert_sql, params)
            self.conn.commit()
        except Exception:
            # content可能保存失败ascii
            params = params[0:(len(params)-1)]
            params = params + ("",)
            self.cursor.execute(insert_sql, params)
            self.conn.commit()



# mysql连接池
class MysqlTwisterPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparams = dict(
            host=settings["MYSQL_HOST"],
            db=settings["MYSQL_DBNAME"],
            user=settings["MYSQL_USER"],
            password=settings["MYSQL_PASSWORD"],
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True
        )
        dbpool = adbapi.ConnectionPool("pymysql", **dbparams)
        return cls(dbpool)

    def process_item(self, item, spider):
        # 使用twsisted将mysql插入变成异步执行
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error, item, spider)   #处理异常

    def handle_error(self, failure, item, spider):
        # 处理异步插入异常
        print(failure)

    def do_insert(self, cursor, item):
        insert_sql = """
                    insert into 
                    jobbole_article(title, create_date, url, url_object_id, front_image_url,
                    front_image_path, comment_nums, fav_nums, praise_nums, tags, content)  
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
        params = (item["title"], item["create_date"], item["url"], item["url_object_id"], item["front_image_url"][0],
                  item["front_image_path"], item["comment_nums"], item["fav_nums"], item["praise_nums"], item["tags"],
                  item["content"])
        try:
            cursor.execute(insert_sql, params)
        except Exception:
            params = params[0:(len(params) - 1)]
            params = params + ("",)
            cursor.execute(insert_sql, params)


# 自定义导出json文件
class JsonWithEncodingPipeline(object):
    def __init__(self):
        self.file = codecs.open('article.json', 'w', encoding="utf-8")

    def process_item(self, item, spider):
        # ensure_ascii:中文编码
        lines = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(lines)
        return item

    def spider_closed(self, spider):
        self.file.close()


# 调用scrapy提供的导出json expoter
class JsonExporterPipeline(JsonItemExporter):
    def __init__(self):
        self.file = open('articleexporter.json', 'wb')
        self.expoter = JsonItemExporter(self.file, encoding="utf-8", ensure_ascii=False)
        self.expoter.start_exporting()

    def close_spider(self, spider):
        self.expoter.finish_exporting()
        self.file.close()

    def process_item(self, item):
        self.expoter.expote_item(item)
        return item


# 图片处理
class ArticleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        if "front_image_url" in item:
            for ok, value in results:
                image_file_path = value["path"]
            item["front_image_path"] = image_file_path

        return item