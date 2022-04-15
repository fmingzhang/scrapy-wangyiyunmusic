# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MusicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    createTime=scrapy.Field()
    tag=scrapy.Field()
    introduce=scrapy.Field()
    cover=scrapy.Field()

    pass
