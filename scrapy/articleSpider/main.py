__author__ = 'lxzy'

from scrapy.cmdline import execute
import sys, os

# sys.path.append("D:\pyc\scrapy\articleSpider")
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "jobbole_cp"])
