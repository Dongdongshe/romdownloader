# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
from romdownloader.items import FileItem

class RomSpider(scrapy.Spider):
    name = "rom"
    allowed_domains = ["www.clockworkmod.com"]
    start_urls = [
        "http://www.clockworkmod.com/rommanager/device/a700/developer/google?manifest=http%3A%2F%2Fgh-pages.clockworkmod.com%2FROMManagerManifest%2Fgapps.js&name=Google%20Apps&deviceName=Acer%20A700",
        ]

    def parse(self, response):
        files = response.xpath('//tbody/tr')
        items = []

        for file in files:
            item = FileItem()
            item['name'] = file.xpath('td/h4/text()').extract()
            item['file_urls'] = file.xpath('td/a/@href').extract()
            items.append(item)
        return items

