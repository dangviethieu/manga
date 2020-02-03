# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

from .constant import *
from .items import *


class MangaPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            MONGODB_SERVER,
            MONGODB_PORT
        )
        self.client = connection[MONGO_DATABASE]

    def process_item(self, item, spider):
        if isinstance(item, MangaItem):
            self.client[MONGODB_COLLECTION_MANGAS].find_one_and_update(
                {'uid': item['uid']},
                {'$set': dict(item)},
                upsert=True
            )
        elif isinstance(item, KindItem):
            self.client[MONGODB_COLLECTION_KINDS].find_one_and_update(
                {'title': item['title']},
                {'$set': dict(item)},
                upsert=True
            )
        elif isinstance(item, KindOfMangaItem):
            self.client[MONGODB_COLLECTION_KIND_MANGAS].find_one_and_update(
                {'title': item['title'], 'source': item['source']},
                {'$set': dict(item)},
                upsert=True
            )
        elif isinstance(item, AuthorItem):
            self.client[MONGODB_COLLECTION_AUTHORS].find_one_and_update(
                {'title': item['title']},
                {'$set': dict(item)},
                upsert=True
            )
        elif isinstance(item, ChapterItem):
            self.client[MONGODB_COLLECTION_CHAPTERS].find_one_and_update(
                {'uid': item['uid']},
                {'$set': dict(item)},
                upsert=True
            )
        return item

