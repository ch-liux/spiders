# -*- coding: utf-8 -*-
# 老版的知乎，请参考orther知乎
import scrapy
import re
import json
from urllib import parse
from scrapy.loader import ItemLoader
from articleSpider.items import ZhihuQuestionItem,ZhihuAnswerItem
import datetime


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']
    start_answer_url = "https://www.zhihu.com/answers/{0}/concerned_upvoters?limit={1}&offset={2}"

    agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    headers = {
        "HOST": "www.zhihu.com",
        "Referrer": "https://www.zhihu.com",
        "User-Agent": agent
    }

    def parse(self, response):
        all_urls = response.css("a::attr(href)").extract()
        all_urls = [parse.urljoin(response.url ,url) for url in all_urls]
        all_urls = filter(lambda x:True if x.startwith("https") else False, all_urls)
        for url in all_urls:
            match_object = re.match("(.*zhihu.com/question/(\d+))(/|$).*", url)
            if match_object:
                request_url = match_object.group(1)
                yield scrapy.Request(request_url, headers=self.headers, callback=self.parse_question)
            else:
                yield scrapy.Request(url, headers=self.headers, callback=self.parse)

    def parse_question(self, response):
        if 'QuestionHeader-title' in response.text:
            # 处理新版本
            match_object = re.match("(.*zhihu.com/question/(\d+))(/|$).*", response.url)
            if match_object:
                question_id = int(match_object.group(2))
            item_loader = ItemLoader(item=ZhihuQuestionItem(), response=response)
            item_loader.add_css("title", "h1.QuestionHeader-title::text")
            item_loader.add_css("content", ".QuestionHeader-detail")
            item_loader.add_value("url", response.url)
            item_loader.add_css("zhihu_id", question_id)
            item_loader.add_css("answer_num", ".List-headerText span::text")
            item_loader.add_css("comments_num", ".QuestionHeader-actions button::text")
            item_loader.add_css("watch_user_num", ".NumberBoard-value::text")
            item_loader.add_css("topics", ".QuestionHeader-topics > .Popover div::text")

            question_item = item_loader.load_item()
        else:
            # 处理旧版本
            match_object = re.match("(.*zhihu.com/question/(\d+))(/|$).*", response.url)
            if match_object:
                question_id = int(match_object.group(2))
            item_loader = ItemLoader(item=ZhihuQuestionItem(), response=response)
            # item_loader.add_css("title", ".zh-question-title h2 a::text")
            item_loader.add_xpath("title", "//*[id='zh-question-title']/h2/a/text()|//*[id='zh-question-title']/h2/span/text()")
            item_loader.add_css("content", "#zh-question-detail")
            item_loader.add_value("url", response.url)
            item_loader.add_css("zhihu_id", question_id)
            item_loader.add_css("answer_num", "#zh-question-answer-num::text")
            item_loader.add_css("comments_num", "#zh-question-meta-wrap a[name='addcomment']::text")
            # item_loader.add_css("watch_user_num", "zh-question-side-header-wrap::text")
            item_loader.add_xpath("watch_user_num", "*//[id='zh-question-side-header-wrap']/text()|*//[id='zh-question-side-header-wrap']/div/a/strong/text()")
            item_loader.add_css("topics", ".zm-tag-editor-labels a::text")

            question_item = item_loader.load_item()
        yield scrapy.Request(self.start_answer_url.format(question_id, 20, 0), headers=self.headers, callback=self.parse_answer)
        yield question_item

    def parse_answer(self, response):
        # 处理question中的answer
        answer_json = json.loads(response.text)
        is_end = answer_json["paging"]["is_end"]
        totals_answer = answer_json["paging"]["totals"]
        next_url = answer_json["paging"]["next"]
        # 提取answer
        for answer in answer_json["data"]:
            answer_item = ZhihuAnswerItem()
            answer_item["zhihu_id"] = answer["id"]
            answer_item["url"] = answer["url"]
            answer_item["question_id"] = answer["question"]["id"]
            answer_item["author_id"] = answer["author"]["id"] if "id" in answer["author"] else None
            answer_item["content"] = answer["content"] if "content" in answer else None
            answer_item["parise_num"] = answer["voteup_count"]
            answer_item["comments_num"] = answer["comment_count"]
            answer_item["create_time"] = answer["created_time"]
            answer_item["update_time"] = answer["updated_time"]
            answer_item["crawl_time"] = datetime.datetime.now()
            yield answer_item
        if not is_end:
            yield scrapy.Request(next_url, headers=self.headers, callback=self.parse_answer)

    def start_requests(self):
        # 异步
        return [scrapy.Reuqest('https://www.zhihu.com/#signin', callback=self.login)]

    def login(self, response):
        response_text = response.text
        match_obj = re.match('.*name="_xsrf" value="(.*?)"', response_text, re.DOTALL)
        xsrf = ''
        if match_obj:
            xsrf =  match_obj.group(1)
        if xsrf:
            post_data = {
                    "_xsrf": xsrf,
                    "phone_num": "xxx",
                    "password": "yyy",
                    "captcha":""
            }
            import time
            t = str(int(time.time() * 1000))
            captcha_url = "https://www.zhihu.com/captcha.gif?r={0}&type=login".format(t)
            yield scrapy.Request(captcha_url, headers=self.headers, meta={"post_data": post_data}, callback=self.login_after_captcha)

    def login_after_captcha(self, response):
        with open("captcha.jpg", "wb") as f:
            f.write(response.body)
            f.close()
        from PIL import Image
        try:
            im = Image.open('captcha.jpg')
            im.show()
            im.close()
        except:
            pass
        captcha = input("输入验证码\n>")

        url = "https://www.zhihu.com/login/phone_num"
        post_data = response.meta.get("post_data")
        post_data["captcha"] = captcha
        return [scrapy.FormRequest(
            url=url,
            formdata=post_data,
            headers=self.headers,
            callback=self.check_login
        )]

    def check_login(self, response):
        text_json = json.loads(response.text)
        if "msg" in text_json and text_json["msg"] == '登录成功':
            for url in self.start_urls:
                yield scrapy.Request(url, dont_filter=True, headers=self.headers, callback=self.parse)