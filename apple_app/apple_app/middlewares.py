# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class AppleAppSpiderMiddleware(object):

    @classmethod
    def from_crawler(cls, crawler):
        #定义类方法，使用scrapy创建爬虫
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        #定义爬虫进程的额外输入

        return None

    def process_spider_output(self, response, result, spider):
        #定义爬虫进程的输出
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        #爬虫错误捕获
        pass

    def process_start_requests(self, start_requests, spider):
        #获取初始url池并进行requests请求
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        #开始爬虫
        spider.logger.info('Spider opened: %s' % spider.name)
