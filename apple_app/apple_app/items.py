# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AppleAppItem(scrapy.Item):
    #设置容器的不同字段，用以存储对应元素
    name = scrapy.Field()
    grade = scrapy.Field()
    comment_num = scrapy.Field()
    size = scrapy.Field()
    version = scrapy.Field()
    dev = scrapy.Field()
    info = scrapy.Field()
    rank = scrapy.Field()

