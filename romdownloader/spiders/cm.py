# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from romdownloader.items import FileItem


class CmSpider(CrawlSpider):
    name = 'miui'
    allowed_domains = ['www.romzj.com']
    start_urls = [
        'http://www.romzj.com/rom/31752.htm',
        'http://www.romzj.com/rom/17941.htm',
        'http://www.romzj.com/rom/8076.htm',
        'http://www.romzj.com/rom/16432.htm',
        'http://www.romzj.com/rom/9744.htm',
        'http://www.romzj.com/rom/8787.htm',
        'http://www.romzj.com/rom/12031.htm',
        'http://www.romzj.com/rom/16801.htm',
        'http://www.romzj.com/rom/19260.htm',
        'http://www.romzj.com/rom/11104.htm',
        'http://www.romzj.com/rom/11975.htm',
        'http://www.romzj.com/rom/16155.htm',
        'http://www.romzj.com/rom/29854.htm',
        'http://www.romzj.com/rom/28324.htm',
        'http://www.romzj.com/rom/30634.htm',
        'http://www.romzj.com/rom/30380.htm',
        'http://www.romzj.com/rom/26800.htm',
        'http://www.romzj.com/rom/28172.htm',
        'http://www.romzj.com/rom/27992.htm',
        'http://www.romzj.com/rom/27174.htm',
        'http://www.romzj.com/rom/9511.htm',
        'http://www.romzj.com/rom/4232.htm',
        'http://www.romzj.com/rom/5060.htm',
        'http://www.romzj.com/rom/3964.htm',
        'http://www.romzj.com/rom/5274.htm',
        'http://www.romzj.com/rom/2531.htm',
        'http://www.romzj.com/rom/1007.htm',
        'http://www.romzj.com/rom/1014.htm',
        'http://www.romzj.com/rom/3925.htm',
        'http://www.romzj.com/rom/4130.htm',
        'http://www.romzj.com/rom/4150.htm',
        'http://www.romzj.com/rom/2378.htm',
        'http://www.romzj.com/rom/10336.htm',
        'http://www.romzj.com/rom/11688.htm',
        'http://www.romzj.com/rom/20101.htm',
        'http://www.romzj.com/rom/11974.htm',
        'http://www.romzj.com/rom/9719.htm',
        'http://www.romzj.com/rom/14186.htm',
        'http://www.romzj.com/rom/21733.htm',
        'http://www.romzj.com/rom/9897.htm',
        'http://www.romzj.com/rom/17939.htm',
        'http://www.romzj.com/rom/9758.htm',
        'http://www.romzj.com/rom/8839.htm',
        'http://www.romzj.com/rom/9050.htm',
        'http://www.romzj.com/rom/7827.htm',
        'http://www.romzj.com/rom/4719.htm',
        'http://www.romzj.com/rom/4722.htm',
        'http://www.romzj.com/rom/4810.htm',
        'http://www.romzj.com/rom/26035.htm',
        'http://www.romzj.com/rom/26550.htm',
        'http://www.romzj.com/rom/25679.htm',
        'http://www.romzj.com/rom/4718.htm',
        'http://www.romzj.com/rom/4721.htm',
        'http://www.romzj.com/rom/4808.htm',
        'http://www.romzj.com/rom/16413.htm',
        'http://www.romzj.com/rom/15877.htm',
        'http://www.romzj.com/rom/21729.htm',
        'http://www.romzj.com/rom/14526.htm',
        'http://www.romzj.com/rom/7944.htm',
        'http://www.romzj.com/rom/9749.htm',
        'http://www.romzj.com/rom/8828.htm',
        'http://www.romzj.com/rom/4861.htm',
        'http://www.romzj.com/rom/4720.htm',
        'http://www.romzj.com/rom/7657.htm',
        'http://www.romzj.com/rom/26434.htm',
        'http://www.romzj.com/rom/24347.htm',
        'http://www.romzj.com/rom/17940.htm',
        'http://www.romzj.com/rom/25123.htm',
        'http://www.romzj.com/rom/23415.htm',
        'http://www.romzj.com/rom/16320.htm',
        'http://www.romzj.com/rom/24062.htm',
        'http://www.romzj.com/rom/12946.htm',
        'http://www.romzj.com/rom/23579.htm',
        'http://www.romzj.com/rom/30527.htm',
        'http://www.romzj.com/rom/31187.htm',
        'http://www.romzj.com/rom/31664.htm',
        'http://www.romzj.com/rom/15674.htm',
        'http://www.romzj.com/rom/16502.htm',
        'http://www.romzj.com/rom/23180.htm',
        'http://www.romzj.com/rom/15204.htm',
        'http://www.romzj.com/rom/17090.htm',
        'http://www.romzj.com/rom/15910.htm',
        'http://www.romzj.com/rom/16189.htm',
        'http://www.romzj.com/rom/15714.htm',
        'http://www.romzj.com/rom/20212.htm',
        'http://www.romzj.com/rom/16213.htm',
        'http://www.romzj.com/rom/18447.htm',
        'http://www.romzj.com/rom/20561.htm',
        'http://www.romzj.com/rom/17743.htm',
        'http://www.romzj.com/rom/4781.htm',
        'http://www.romzj.com/rom/6296.htm',
        'http://www.romzj.com/rom/6480.htm',
        'http://www.romzj.com/rom/4445.htm',
        'http://www.romzj.com/rom/19223.htm',
        'http://www.romzj.com/rom/8129.htm',
        'http://www.romzj.com/rom/4700.htm',
        'http://www.romzj.com/rom/19531.htm',
        'http://www.romzj.com/rom/4840.htm',
        'http://www.romzj.com/rom/6270.htm',
        'http://www.romzj.com/rom/502.htm',
        'http://www.romzj.com/rom/21363.htm',
        'http://www.romzj.com/rom/21730.htm',
        'http://www.romzj.com/rom/17036.htm',
        'http://www.romzj.com/rom/16847.htm',
        'http://www.romzj.com/rom/13606.htm',
        'http://www.romzj.com/rom/21734.htm',
        'http://www.romzj.com/rom/11373.htm',
        'http://www.romzj.com/rom/9868.htm',
        'http://www.romzj.com/rom/8741.htm',
        'http://www.romzj.com/rom/21290.htm',
        'http://www.romzj.com/rom/6056.htm',
        'http://www.romzj.com/rom/1130.htm',
        'http://www.romzj.com/rom/11432.htm',
        'http://www.romzj.com/rom/6271.htm',
        'http://www.romzj.com/rom/2318.htm',
        'http://www.romzj.com/rom/8303.htm',
        'http://www.romzj.com/rom/9742.htm',
        'http://www.romzj.com/rom/8784.htm',
        'http://www.romzj.com/rom/26460.htm',
        'http://www.romzj.com/rom/27988.htm',
        'http://www.romzj.com/rom/29754.htm',
        'http://www.romzj.com/rom/29299.htm',
        'http://www.romzj.com/rom/28196.htm',
        'http://www.romzj.com/rom/3924.htm',
        'http://www.romzj.com/rom/993.htm',
        'http://www.romzj.com/rom/30382.htm',
        'http://www.romzj.com/rom/31855.htm',
        'http://www.romzj.com/rom/30635.htm',
        'http://www.romzj.com/rom/29855.htm',
        'http://www.romzj.com/rom/27993.htm',
        'http://www.romzj.com/rom/29228.htm',
        'http://www.romzj.com/rom/28326.htm',
        'http://www.romzj.com/rom/28171.htm',
        'http://www.romzj.com/rom/27256.htm',
        'http://www.romzj.com/rom/21575.htm',
        'http://www.romzj.com/rom/21055.htm',
        'http://www.romzj.com/rom/27295.htm',
        'http://www.romzj.com/rom/9547.htm',
        'http://www.romzj.com/rom/14274.htm',
        'http://www.romzj.com/rom/21406.htm',
        'http://www.romzj.com/rom/11689.htm',
        'http://www.romzj.com/rom/20118.htm',
        'http://www.romzj.com/rom/21243.htm',
        'http://www.romzj.com/rom/14197.htm',
        'http://www.romzj.com/rom/22515.htm',
        'http://www.romzj.com/rom/20943.htm',
        'http://www.romzj.com/rom/20542.htm',
        'http://www.romzj.com/rom/9360.htm',
        'http://www.romzj.com/rom/16640.htm',
        'http://www.romzj.com/rom/14470.htm',
        'http://www.romzj.com/rom/8786.htm',
        'http://www.romzj.com/rom/6882.htm',
        'http://www.romzj.com/rom/16715.htm',
        'http://www.romzj.com/rom/7473.htm',
        'http://www.romzj.com/rom/9743.htm',
        'http://www.romzj.com/rom/12620.htm',
        'http://www.romzj.com/rom/24971.htm',
        'http://www.romzj.com/rom/31521.htm',
        'http://www.romzj.com/rom/29805.htm',
        'http://www.romzj.com/rom/29638.htm',
        'http://www.romzj.com/rom/27543.htm',
        'http://www.romzj.com/rom/29177.htm',
        'http://www.romzj.com/rom/28669.htm',
        'http://www.romzj.com/rom/28319.htm',
        'http://www.romzj.com/rom/27255.htm',
        'http://www.romzj.com/rom/27796.htm',
        'http://www.romzj.com/rom/23046.htm',
        'http://www.romzj.com/rom/22458.htm',
        'http://www.romzj.com/rom/10638.htm',
        'http://www.romzj.com/rom/21731.htm',
        'http://www.romzj.com/rom/3972.htm',
        'http://www.romzj.com/rom/8075.htm',
        'http://www.romzj.com/rom/16156.htm',
        'http://www.romzj.com/rom/5162.htm',
        'http://www.romzj.com/rom/6678.htm',
        'http://www.romzj.com/rom/3204.htm',]
    
    def parse(self, response):
#        url1s = response.xpath('//div[@class="zy_lr_le_jz"]/a/@href').extract()
        url1s = response.xpath('//a[@id="detail_ptdl"]/@href').extract()
        for url1 in url1s:
            item = FileItem()
            item['url'] = url1
            yield item
        
#        url2s = response.xpath('//a[@class="btn_5"]/@href').extract()
#        for url2 in url2s:
       #     item = FileItem()
       #     item['url'] = url2
#            yield item
        
#        i = RomdownloaderItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
       # #i['description'] = response.xpath('//div[@id="description"]').extract()
#        return i
