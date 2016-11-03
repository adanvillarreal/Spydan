# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpydanItem(scrapy.Item):
    ip = scrapy.Field()
    port = scrapy.Field()
    protocol = scrapy.Field()
    state = scrapy.Field()
    h3 = scrapy.Field()
    pre = scrapy.Field()
    hostname = scrapy.Field()
    pass
