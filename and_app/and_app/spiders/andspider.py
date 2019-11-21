# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy.spider import Spider
from and_app.items import AndAppItem

class apple_spider(Spider):
    name = 'apple_spider'
    headers = {
        "User-Agent": 'Mozilla / 5.0(WindowsNT10.0;Win64;x64;rv:55.0) Gecko / 20100101Firefox / 55.0'
    }
    start_urls = ['http://sj.qq.com/myapp/category.htm?orgame=1&categoryId=109']

    def parse(self, res):
        headers = {
            "User-Agent": 'Mozilla / 5.0(WindowsNT10.0;Win64;x64;rv:55.0) Gecko / 20100101Firefox / 55.0'
        }
        pages = res.xpath('//html/body/div[3]/div[2]/ul/li')
        # print(pages)

        for a in pages:
            item = AndAppItem()
            item['num'] = 'open_end'
            # print(item['num'])/html/body/div[3]/div[2]/ul/li[1]/div/div/a[1]
            url = 'http://sj.qq.com/myapp/' + (a.xpath('.//div/div/a[1]/@href').extract()[0])
            # print(url)
            req = Request(url, callback=self.parseTwo, headers=self.headers)
            req.meta['item'] = item
            yield req

    def parseTwo(self, res):
        # print('ok')
        item = res.meta['item']
        # // *[ @ id = "J_DetDataContainer"] / div / div[1] / div[2] / div[1] / div[1]
        item['name'] = res.xpath('//*[@id="J_DetDataContainer"]/div/div[1]/div[2]/div[1]/div[1]/text()').extract()[0]
        # print(item['name'])
        item['grade'] = res.xpath('//*[@id="J_DetDataContainer"]/div/div[1]/div[2]/div[2]/div[2]/text()').extract()[0]
        item['download_num'] =res.xpath('//*[@id="J_DetDataContainer"]/div/div[1]/div[2]/div[3]/div[1]/text()').extract()[0]
        item['comment_num'] = 0
        item['size'] = res.xpath('//*[@id="J_DetDataContainer"]/div/div[1]/div[2]/div[3]/div[3]/text()').extract()[0]
        item['add'] = res.xpath('//*[@id="J_AdvBox"]').extract()[0]
        item['version'] = res.xpath('//*[@id="J_DetDataContainer"]/div/div[3]/div[2]/text()').extract()[0]
        item['update_time'] = res.xpath('//*[@id="J_ApkPublishTime"]').extract()[0]
        item['dev'] = res.xpath('//*[@id="J_DetDataContainer"]/div/div[3]/div[6]/text()').extract()[0]
        item['info'] = res.xpath('////*[@id="J_DetAppDataInfo"]/div[1]/text()').extract()[0]
        yield item
