# -*- coding: utf-8 -*-

# Scrapy settings for romdowanloader project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'romdownloader'

SPIDER_MODULES = ['romdownloader.spiders']
NEWSPIDER_MODULE = 'romdownloader.spiders'
ITEM_PIPELINES = [
    'romdownloader.files.FilesPipeline',
    ]
FILES_STORE = '/home/sherman/Project/romdownloader/roms'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'romdowanloader (+http://www.yourdomain.com)'
