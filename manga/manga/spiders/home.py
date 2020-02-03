from scrapy import Spider, Request
from scrapy.loader import ItemLoader

from ..items import MangaItem, ChapterItem, AuthorItem, KindItem, KindOfMangaItem

import logging


class Home(Spider):
    name = 'home'
    custom_settings = {
        'FEED_EXPORT_FIELDS': ['uid', 'title', 'link', 'img', 'updated_at', 'view', 'comment', 'heart', 'source', 'status', 'description'],
        'DUPEFILTER_CLASS': 'scrapy.dupefilters.BaseDupeFilter',
    }
    allowed_domains = ['nettruyen.com']
    start_urls = [
        "https://nettruyen.com",
    ]

    def __init__(self):
        logger = logging.getLogger('scrapy.middleware')
        logger.setLevel(logging.WARNING)
        # self.html_file = open("net.html", 'w')

    def parse(self, response):
        # self.html_file.write(response.text)
        # self.html_file.close()

        for manga in response.xpath('//div[@class="row"]/div[@class="item"]'):
            uid = manga.xpath('div[@class="box_tootip"]/@id').extract_first()
            detail = manga.xpath('figure[@class="clearfix"]//span[@class="pull-left"]//text()').extract()
            item = ItemLoader(item=MangaItem(), selector=manga)
            item.add_xpath('uid', 'div[@class="box_tootip"]/@id')
            item.add_xpath('title', 'div[@class="box_tootip"]//div[@class="title"]/text()')
            item.add_xpath('link', 'div[@class="box_tootip"]//a/@href')
            item.add_xpath('img', 'div[@class="box_tootip"]//a/img/@data-original')
            item.add_value('view', [detail[-3]])
            item.add_value('comment', [detail[-2]])
            item.add_value('heart', [detail[-1]])

            # scraping detail
            temp_detail = response.urljoin(manga.xpath('div[@class="box_tootip"]//a/@href').extract_first())
            yield Request(temp_detail, self.parse_detail, meta={'item': item, 'source': uid})

        new_page = response.xpath('//a[@class="next-page"]/@href').extract()
        if new_page:
            new_page = response.urljoin(new_page[0])
            self.logger.info('Page scraped, clicking on "more"! new_page = {}'.format(new_page))
            yield Request(new_page, callback=self.parse)

    def parse_detail(self, response):
        item = ItemLoader(item=MangaItem(), response=response, parent=response.meta['item'], selector=response)
        item.add_xpath('status', '//article[@id="item-detail"]//li[@class="status row"]/p[@class="col-xs-8"]/text()')
        item.add_xpath('description', '//article[@id="item-detail"]//div[@class="detail-content"]/p')
        item.add_xpath('author', '//article[@id="item-detail"]//li[@class="author row"]/p[@class="col-xs-8"]/a/text()')
        item.add_xpath('updated_at', '//article[@id="item-detail"]//time/text()')
        yield item.load_item()

        for kind_response in response.xpath('//article[@id="item-detail"]//li[@class="kind row"]/p[@class="col-xs-8"]/a'):
            kind = KindItem(
                title=kind_response.xpath('text()').extract_first(),
                link=kind_response.xpath('@href').extract_first()
            )
            yield kind

            kind_of_manga = KindOfMangaItem(
                title=kind_response.xpath('text()').extract_first(),
                source=response.meta['source']
            )
            yield kind_of_manga

        for author_response in response.xpath('//article[@id="item-detail"]//li[@class="author row"]/p[@class="col-xs-8"]/a'):
            author = AuthorItem(
                title=author_response.xpath('text()').extract_first(),
                link=author_response.xpath('@href').extract_first()
            )
            yield author

        for chapter in response.xpath('//div[@class="list-chapter"]//li[@class="row"] | //div[@class="list-chapter"]//li[@class="row less"]'):
            item = ItemLoader(item=ChapterItem(), selector=chapter)
            item.add_xpath('uid', 'div/a/@data-id')
            item.add_xpath('title', 'div/a/text()')
            item.add_xpath('link', 'div/a/@href')
            item.add_xpath('updated_at', 'div[2]/text()')
            item.add_xpath('view', 'div[3]/text()')
            item.add_value('source', response.meta['source'])
            # scraping detail
            temp_detail = response.urljoin(chapter.xpath('div/a/@href').extract_first())
            yield Request(temp_detail, self.parse_chapter, meta={'item': item})


    def parse_chapter(self, response):
        item = ItemLoader(item=ChapterItem(), response=response, parent=response.meta['item'], selector=response)
        item.add_xpath('img', '//div[@class="reading-detail box_doc"]/div[@class="page-chapter"]/img/@src')
        item.add_xpath('img_v2', '//div[@class="reading-detail box_doc"]/div[@class="page-chapter"]/img/@data-original')
        item.add_xpath('img_v3', '//div[@class="reading-detail box_doc"]/div[@class="page-chapter"]/img/@data-cdn')
        yield item.load_item()



