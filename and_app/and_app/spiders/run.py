from scrapy import cmdline
name = 'apple_spider'
# name = 'news_huazhong'
cmd = 'scrapy crawl {0} -o res.csv'.format(name)
# cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())