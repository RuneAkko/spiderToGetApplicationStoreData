# -*- coding: utf-8 -*-

# Define your item pipelines here
#

'''
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

'''


from openpyxl import Workbook

#设置item字段顺序和存储方式
class AppleAppPipeline(object):

    def __init__(self):

        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['APP名称','大小','评分','评论数目','版本号','开发商','应用信息','排名'])

    def process_item(self, item, spider):
        line = [item['name'], item['size'], item['grade'], item['comment_num'],
                item['version'], item['dev'], item['info'], item['rank']]
        self.ws.append(line)
        self.wb.save('../result1.xlsx')
        return item

