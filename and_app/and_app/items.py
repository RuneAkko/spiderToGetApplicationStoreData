# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AndAppItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    num = scrapy.Field()
    name = scrapy.Field()
    grade = scrapy.Field()
    comment_num = scrapy.Field()
    download_num = scrapy.Field()
    size = scrapy.Field()
    add = scrapy.Field()
    version = scrapy.Field()
    update_time = scrapy.Field()
    dev = scrapy.Field()
    info = scrapy.Field()
    pass
