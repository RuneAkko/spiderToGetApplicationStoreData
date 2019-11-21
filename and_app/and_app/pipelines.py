# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from openpyxl import Workbook

class AndAppPipeline(object):

    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['序号', 'APP名称', '评分', '评论数目', '下载量', '有无广告', '版本号', '更新时间', '开发商', '应用信息'])
    def process_item(self, item, spider):
        line = [item['num'], item['name'], item['grade'], item['comment_num'], item['download_num'], item['size'],
                item['add'],
                item['version'], item['update_time'], item['dev'], item['info']]
        self.ws.append(line)
        self.wb.save('../and.xlsx')
        return item
