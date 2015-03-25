# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
from romdownloader.items import FileItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class RomSpider(CrawlSpider):
    name = "nexus"
    allowed_domains = ["developer.google.com"]
    start_urls = [
         "https://developers.google.com/android/nexus/images"   
        ]
    
    def parse(self, response):
        urls = response.xpath('//table/tr')
        items = []
        for url in urls:
            item = FileItem()
            item['name'] = url.xpath('@id').extract()
            item['url'] = url.xpath('td/a/@href').extract()
            items.append(item)
        return items
