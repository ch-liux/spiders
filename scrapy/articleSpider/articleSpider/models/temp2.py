#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import redis

redis_cli = redis.StrictRedis(host='47.98.106.61',port=6379, db=1)
redis_cli.sadd("xx","yy")


