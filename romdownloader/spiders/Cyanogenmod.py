# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from romdownloader.items import FileItem


class CyanogenmodSpider(CrawlSpider):
    name = 'Cyanogenmod'
    allowed_domains = ['cyanogenmod.com']
    start_urls = ['https://download.cyanogenmod.org/?device=&type=stable']

    rules = (
        Rule(LinkExtractor(allow_domains=('https://download.cyanogenmod.org')), callback='parse_item', follow=True),
    )

    def parse(self, response):
        items=[]
        urls = response.xpath('//tbody')
        for url in urls:
            item = FileItem()
            item['url'] = url.xpath('tr/td/a/@href')
            items.append(item)
            return items

#        i = RomdownloaderItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
