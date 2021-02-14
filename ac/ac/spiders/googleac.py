# -*- coding: utf-8 -*-
import scrapy,os
from scrapy.loader import ItemLoader
from ac.items import AcItem
from string import ascii_lowercase

class PaginegialleSpider(scrapy.Spider):
    name = 'ac'
    #start_urls = []
    single = False
    base = 'https://www.google.com/complete/search?hl=%s&oe=utf-8&output=toolbar&q=%s'

    def start_requests(self):
        b = os.environ['START'] #self.settings['START']
        base = self.base % ( os.environ['HL'] , b)
        for i in ascii_lowercase:
            url = ((base+' ' +i).replace(' ', '%20').encode('ascii','ignore')).decode("utf-8")
            yield scrapy.Request(url=url, meta={'origin': b, 'letter': i, 'depth': 1})

    def parse(self, response):
        found = False
        for u in response.selector.xpath('//suggestion/@data').getall():
            found = True
            l = ItemLoader(item=AcItem(), response=response)
            l.add_value('origin', response.meta['origin'])
            l.add_value('letter', response.meta['letter'])
            l.add_value('depth', response.meta['depth'])
            l.add_value('suggestion', u)
            l.add_value('url', response.url)
            yield l.load_item()

            if (response.meta['depth'] < int( os.environ['MAXDEPTH']) ):
                base = self.base % ( os.environ['HL'] , u )
                depth = response.meta['depth'] + 1
                for i in ascii_lowercase:
                    url = ((base+' ' +i).replace(' ', '%20').encode('ascii','ignore')).decode("utf-8")
                    yield scrapy.Request(url=url, meta={'origin': u, 'letter': i, 'depth': depth} )

        if not found:
            l = ItemLoader(item=AcItem(), response=response)
            l.add_value('origin', response.meta['origin'])
            l.add_value('letter', response.meta['letter'])
            l.add_value('depth', response.meta['depth'])
            l.add_value('suggestion', '@empty')
            l.add_value('url', response.url)
            yield l.load_item()
