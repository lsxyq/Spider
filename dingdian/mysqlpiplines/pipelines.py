# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from dingdian.items import DingdianItem
from .sql import Sql
class DingdianPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item,DingdianItem):
            name_id = item['name_id']
            ret = Sql.select_name(name_id)
            if ret[0] == 1:
                print('已经存在了')
                pass
            else:
                xs_author = item['author']
                category = item['category']
                xs_name = item['name']
                Sql.insert_dd_name(xs_name,xs_author,category,name_id)
                print('开始存小说标题')


