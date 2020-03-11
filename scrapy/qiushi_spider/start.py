# 启动爬虫
# 一般要用cmd命令输入scrapy crawl qiushi，比较麻烦
# 这里直接写一个python文件启动scrapy
from scrapy import cmdline
cmdline.execute('scrapy crawl qiushi'.split())
