# -*- coding: utf-8 -*-

# Scrapy settings for apple_app project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'apple_app'

SPIDER_MODULES = ['apple_app.spiders']
NEWSPIDER_MODULE = 'apple_app.spiders'

#激活管道类
ITEM_PIPELINES = {
    'apple_app.pipelines.AppleAppPipeline': 800,
}
#遵守爬虫协议
ROBOTSTXT_OBEY = True
