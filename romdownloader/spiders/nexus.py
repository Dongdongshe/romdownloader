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
#         "http://www.clockworkmod.com/rommanager/",   
#        "http://www.clockworkmod.com/rommanager/device/a700/developer/google?manifest=http%3A%2F%2Fgh-pages.clockworkmod.com%2FROMManagerManifest%2Fgapps.js&name=Google%20Apps&deviceName=Acer%20A700",
        ]
    
#    rules = (
#        Rule(LinkExtractor(restrict_xpaths=('//tbody', )), callback='parse_url'),
#        )
        
#    def parse_start_url(response):
#        response.xpath('//')    
    def parse(self, response):
        urls = response.xpath('//table/tr')
        items = []
        for url in urls:
            item = FileItem()
            item['name'] = url.xpath('@id').extract()
            item['url'] = url.xpath('td/a/@href').extract()
            items.append(item)
        return items
#    def parse_url(self, response):
#        urls = response.url
#        items = []
#        for url in urls:
#            item = FileItem()
#            item['file_url'] = url
#            items.append(item)


#        files = response.xpath('//tbody/tr')
#        items = []
#
#        for file in files:
#            item = FileItem()
#            item['name'] = file.xpath('td/h4/text()').extract()
#            item['file_url'] = file.xpath('td/a/@href').extract()
#            items.append(item)
#        return items

