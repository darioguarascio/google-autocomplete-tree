# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
#from scrapy.loader.processors import TakeFirst, MapCompose
from itemloaders.processors import TakeFirst

class AcItem(scrapy.Item):
    origin = scrapy.Field(
        output_processor=TakeFirst()
    )
    letter = scrapy.Field(
        output_processor=TakeFirst()
    )
    suggestion = scrapy.Field(
        output_processor=TakeFirst()
    )
    depth = scrapy.Field(
        output_processor=TakeFirst()
    )
    url = scrapy.Field(
        output_processor=TakeFirst()
    )
    pass
