# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from romdownloader.items import FileItem


class CmSpider(CrawlSpider):
    name = 'cm'
    allowed_domains = ['www.clockworkmod.com']
    start_urls = ['http://www.www.clockworkmod.com/rommanager/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=('//tbody')), callback='parse_item'),
    )

    def parse_item(self, response):
        self.log('%s' % response.url) 
#        i = RomdownloaderItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
#        return i
