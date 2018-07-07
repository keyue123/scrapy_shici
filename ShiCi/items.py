# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShiciItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	name    = scrapy.Field()	# 文章名
	author  = scrapy.Field()	# 作者
	content = scrapy.Field()	# 内容 
