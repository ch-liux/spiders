#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from django.shortcuts import render, redirect
from django.views.generic.base import View
from search.models import ArticleType
from django.http import HttpResponse
import json
from elasticsearch import Elasticsearch
from datetime import datetime
import redis

client = Elasticsearch(hosts="127.0.0.1")
redis_cli = redis.StrictRedis(host='localhost',port=6379, db=1)


def home(request):
    topn_search = redis_cli.zrevrangebyscore("search_keywords_set", "+inf", "-inf", start=0, num=5)
    topn_search = [topn.decode('utf-8') for topn in topn_search]
    return render(request, 'index.html', {"topn_search":topn_search})


def suggest(request):
    key_words = request.GET.get('s', '')
    re_datas = []
    if key_words:
        s = ArticleType.search()
        s = s.suggest('my_suggest', key_words, completion={
            "field": "suggest",
            "fuzzy": {
                "fuzziness": 2
            },
            "size": 10
        })
        suggestions = s.execute_suggest()
        for match in suggestions.my_suggest[0].options:
            source = match._source
            re_datas.append(source["title"])
    return HttpResponse(json.dumps(re_datas), content_type="application/json")


def search(request):
    key_words = request.GET.get('q', '')
    page = request.GET.get('p', 1)
    s_type = request.GET.get('s_type', 'article')

    redis_cli.zincrby("search_keywords_set", key_words)
    topn_search = redis_cli.zrevrangebyscore("search_keywords_set", "+inf", "-inf",start=0, num=5)
    topn_search = [topn.decode('utf-8') for topn in topn_search]

    try:
        page = int(page)
    except:
        page = 1

    jobbole_count = redis_cli.get("jobbole_count")
    try:
        jobbole_count = int(jobbole_count)
    except:
        jobbole_count = 0
    start_time = datetime.now()
    response = client.search(
        index="jobbole",
        body={
            "query": {
                "multi_match": {
                    "query": key_words,
                    "fields": ["tags", "title", "content"]
                }
            },
            "from": (page-1)*10,
            "size": 10,
            "highlight": {
                "pre_tags": ['<span class="keyWord">'],
                "post_tags": ['</span>'],
                "fields": {
                    "title": {},
                    "content": {},
                }
            }
        }
    )
    end_time = datetime.now()
    last_seconds = (end_time - start_time).total_seconds()

    total_nums = response["hits"]["total"]
    if (page%10)>0:
        page_nums = int(total_nums/10)+1
    else:
        page_nums = int(total_nums/10)

    hit_list = []
    for hit in response["hits"]["hits"]:
        hit_dict = {}
        try:
            if "title" in hit["highlight"]:
                hit_dict["title"] = "".join(hit["highlight"]["title"])
        except:
            hit_dict["title"] = "".join(hit["_source"]["title"])
        try:
            if "content" in hit["highlight"]:
                hit_dict["content"] = "".join(hit["highlight"]["content"])[:500]
        except:
            hit_dict["content"] = "".join(hit["_source"]["content"])[:500]

        hit_dict["create_date"] = hit["_source"]["create_date"]
        hit_dict["url"] = hit["_source"]["url"]
        hit_dict["score"] = hit["_score"]

        hit_list.append(hit_dict)
    return render(request, "result.html", {"page":page,
                                              "total_nums":total_nums,
                                              "page_nums":page_nums,
                                              "last_seconds":last_seconds,
                                              "jobbole_count":jobbole_count,
                                              "topn_search":topn_search,
                                              "all_hits":hit_list,
                                              "key_words":key_words})