# -*- coding: utf-8 -*-
import scrapy
from qiushi_spider.items import QiushiSpiderItem
from scrapy.http.response.html import HtmlResponse

class QiushiSpider(scrapy.Spider):
    # 爬虫名称，每个spider的名称不能相同
    name = 'qiushi'
    # 允许的域名
    allowed_domains = ['qiushibaike.com']
    # 开始url
    start_urls = ['https://www.qiushibaike.com/text/page/1/']
    
    # 第一个解析函数 
    def parse(self, response):
        # response 的 type 为 HtmlResponse
        # 可以使用 text 获取整个文本
        # 可以直接使用xpath、css、selector取得特定位置信息
        content_left = response.xpath('//div[@id="content-left"]/div')
        print(len(content_left))
        # 返回结果为selectorList类型
        # 可以使用循环遍历
        # 继续使用xpath等定位
        for duanzi in content_left:
            # duanzi为selector类型
            # get() 获取selector 中的第一个文本
            author = duanzi.xpath('.//h2/text()').get().strip()
            # getall() 获取selector 中所有文本
            # getall() 返回结果为一个字符串列表
            content = duanzi.xpath('.//div[@class="content"]/span/text()').getall()
            # 完成列表中字符串拼接，并用strip() 掐去两边空白部分
            content = ''.join(content).strip()
            # 把数据导入item中
            item = QiushiSpiderItem(author=author, content= content)
            # 使用yield 返回结果
            # 爬虫不会停止
            yield item
        # 获取下一页网址
        next_url = response.xpath('//ul[@class="pagination"]/li[last()]/a/@href').get()
        # 如果没有下一页网址，爬虫结束
        if not next_url:
            # 使用return，爬虫结束
            return
        else:
            # 用新的网址请求
            # callback 定义新网址的处理函数，这里继续用parse函数处理
            new_url = 'https://www.qiushibaike.com' + str(next_url)
            yield scrapy.Request(new_url, callback=self.parse)

