# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

# 专门用来保存数据的
# 想要调用，现在 setting 中激活
# 使用json格式保存
# class QiushiSpiderPipeline(object):
#     def open_spider(self,spider):
#         print('爬虫开始了')
#         self.fp = open('duanzi.json', 'w', encoding='utf-8')
#
#     # 有 item 传过来的时候就会被调用
#     def process_item(self, item, spider):
#         item_json = json.dumps(dict(item),ensure_ascii=False)
#         self.fp.write(item_json+'\n')
#         return item
#
#     def close_spider(self,spider):
#         print('爬虫结束了')
#         self.fp.close()

from scrapy.exporters import JsonItemExporter,JsonLinesItemExporter

# 使用自带 exporter 存储
# JsonItemExporter 只能整体写好再存储
# 保存为列表中的字典
# 比较耗内存，适合较小的数据量
# class QiushiSpiderPipeline(object):
#     def open_spider(self,spider):
#         print('爬虫开始了')
#         # wb 以二进制形式打开
#         self.fp = open('duanzi.json', 'wb')
#         self.exporter = JsonItemExporter(self.fp, ensure_ascii=False,encoding='utf-8')
#         self.exporter.start_exporting()
#
#     # 有 item 传过来的时候就会被调用
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item
#
#     def close_spider(self,spider):
#         self.exporter.finish_exporting()
#         self.fp.close()
#         print('爬虫结束了')

# 使用 JsonLinesItemExporter 存储
# 以行方式存储
# 数据量比较多的时候使用
class QiushiSpiderPipeline(object):
    def open_spider(self,spider):
        print('爬虫开始了')
        # wb 以二进制形式打开
        self.fp = open('duanzi.json', 'wb')
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False,encoding='utf-8')
        self.exporter.start_exporting()

    # 有 item 传过来的时候就会被调用
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self,spider):
        self.exporter.finish_exporting()
        self.fp.close()
        print('爬虫结束了')

