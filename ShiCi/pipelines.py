# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ShiciPipeline(object):
    def process_item(self, item, spider):
		with open('古诗词.txt', "a") as f:
			f.write(item['name'].encode("utf8") + '\n')
			f.write(item['author'].encode("utf8") + '\n')
			f.write(item['content'].encode("utf8") + '\n')
			f.write('-----------------------------------------------------------------\n')
		return item
