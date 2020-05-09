# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class TutorialPipeline(object):
    collection_name = "corona"

    def open_spider(self, spider):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["BD"]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        print(item["Country"])
        print("--------------------------------------------------------------->>>>>>>>>>>>>>>>")
        if item["Country"] is not None:
            self.db[self.collection_name].insert(item)
        return item
