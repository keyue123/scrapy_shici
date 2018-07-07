# -*- coding: utf-8 -*-
import scrapy
from ShiCi.items import ShiciItem

import re   

class TextSpider(scrapy.Spider):
	name = 'gushiwen'
	allowed_domains = ['gushiwen.org']
	start_urls = ['https://www.gushiwen.org']

	def parse(self, response):
		re_br = re.compile('<br\s*?/?>')	# 将<br>转为换行
		re_p  = re.compile('<p\s*?/?>')		# 去掉<p>
		re_h = re.compile('</?\w+[^>]*>')	# 去掉html标签
		
		informations = response.xpath("//div[@class='left']/div[@class='sons']")
		for information in informations:
			item = ShiciItem()
		
			item['name'] = information.xpath('./div[@class="cont"]/p/a/b/text()').extract_first()
			item['author'] = information.xpath('div[@class="cont"]/p[@class="source"] | a//text()').extract_first()
			item['content'] = information.xpath('./div[@class="cont"]/div[@class="contson"] | p//text()').extract_first()
		
			item['author'] = re_h.sub('', item['author'])

			item['content'] = re_br.sub('\n', item['content'])
			item['content'] = re_p.sub('', item['content'])
			item['content'] = re_h.sub('', item['content'])

			print item['name']
			print item['author']
			print item['content']

			yield item

			page_url = response.xpath('//div[@class="left"]/form[@id="FromPage"]/div[@class="pagesright"]/a[@class="amore"]/@href').get()
			if page_url:
				print "https://www.gushiwen.org" + page_url
				yield scrapy.Request("https://www.gushiwen.org" + page_url, callback = self.parse)
