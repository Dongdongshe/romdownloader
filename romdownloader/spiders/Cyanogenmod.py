# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from romdownloader.items import FileItem


class CyanogenmodSpider(CrawlSpider):
    name = 'Cyanogenmod'
    allowed_domains = ['cyanogenmod.com']
    start_urls = [
        'https://download.cyanogenmod.org/?device=&type=stable',
        'https://download.cyanogenmod.org/?type=snapshot',
        'https://download.cyanogenmod.org/?type=nightly'
        ]

    def parse(self, response):
        urls = response.xpath('//tbody/tr/td/a/@href').re(r'data.url=http://get.cm/\s*(.*)\&data.name')
        for url in urls:
            item = FileItem()
            item['url'] = url
            yield item
