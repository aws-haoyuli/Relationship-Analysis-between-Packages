# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem
import logging

class MongoDBPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = client.get_database(settings['MONGODB_DB'])
        self.collection = db.get_collection(settings['MONGODB_COLLECTION'])

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem('Missing {0}'.format(data))
        if valid:
            self.collection.update({'url': item['url']},
                                   dict(item), upsert=True)
            logging.log(logging.INFO, 'Question added to MongoDB database!')
        return item


class StackPipeline(object):
    def process_item(self, item, spider):
        return item
