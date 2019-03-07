#!/usr/bin/python
#coding=utf-8

import scrapy
from mySpider.items import MyspiderItem

# 一个爬虫类
class ItcastSpider(scrapy.Spider):
	# 爬虫名
	name = "itcast"
	# 允许
	allowd_domains  = ["http://www.itcast.cn/"]
	# 爬虫真是的url
	start_urls = [
		"http://www.itcast.cn/channel/teacher.shtml#aandroid",
        "http://www.itcast.cn/channel/teacher.shtml#ac",
        "http://www.itcast.cn/channel/teacher.shtml#acloud",
        "http://www.itcast.cn/channel/teacher.shtml#aios",
        "http://www.itcast.cn/channel/teacher.shtml#ajavaee",
        "http://www.itcast.cn/channel/teacher.shtml#anetmarket",
        "http://www.itcast.cn/channel/teacher.shtml#aphp",
        "http://www.itcast.cn/channel/teacher.shtml#apython",
        "http://www.itcast.cn/channel/teacher.shtml#astack",
        "http://www.itcast.cn/channel/teacher.shtml#aui",
        "http://www.itcast.cn/channel/teacher.shtml#aweb"
	]

	def parse(self, response):
		# with open('teacher.html', "w") as f:
		# 	f.write(response.body)
		# 通过scrapy自带的xpath匹配出所有老师根节点列表集合
		teacher_list = response.xpath('//div[@class="li_txt"]')

		# teacherItem = []

		# 遍历根节点
		for each in teacher_list:
			item = MyspiderItem()

			# extract() 将匹配出来的结果转换为Unicode字符串 不加extract() 结果为xpath匹配对象
			name = each.xpath('./h3/text()').extract()
			title = each.xpath('./h4/text()').extract()
			info = each.xpath('./p/text()').extract()

			item['name'] = name[0]
			item['title'] = title[0]
			item['info'] = info[0]

			# teacherItem.append(item)
		

		# return teacherItem
			yield item


