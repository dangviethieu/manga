# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


def item_strip(data):
    return data[0].strip()


class MangaItem(scrapy.Item):
    uid = scrapy.Field(output_processor=item_strip)
    title = scrapy.Field(output_processor=item_strip)
    link = scrapy.Field(output_processor=item_strip)
    img = scrapy.Field(output_processor=item_strip)
    updated_at = scrapy.Field(output_processor=item_strip)
    view = scrapy.Field(output_processor=item_strip)
    comment = scrapy.Field(output_processor=item_strip)
    heart = scrapy.Field(output_processor=item_strip)
    description = scrapy.Field(output_processor=item_strip)
    status = scrapy.Field(output_processor=item_strip)
    author = scrapy.Field(output_processor=item_strip)


class ChapterItem(scrapy.Item):
    uid = scrapy.Field(output_processor=item_strip)
    title = scrapy.Field(output_processor=item_strip)
    link = scrapy.Field(output_processor=item_strip)
    source = scrapy.Field(output_processor=item_strip)
    updated_at = scrapy.Field(output_processor=item_strip)
    view = scrapy.Field(output_processor=item_strip)
    img = scrapy.Field()
    img_v2 = scrapy.Field()
    img_v3 = scrapy.Field()


class AuthorItem(scrapy.Item):
    title = scrapy.Field(output_processor=item_strip)
    link = scrapy.Field(output_processor=item_strip)


class KindItem(scrapy.Item):
    title = scrapy.Field(output_processor=item_strip)
    link = scrapy.Field(output_processor=item_strip)


class KindOfMangaItem(scrapy.Item):
    title = scrapy.Field(output_processor=item_strip)
    source = scrapy.Field(output_processor=item_strip)


