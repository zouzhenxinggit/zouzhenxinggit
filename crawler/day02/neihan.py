#!/usr/bin/python
#coding=utf-8

import urllib
import urllib2
import re



url = "https://www.neihan8.com/article/list_5_"

class Spider(object):
	"""
		内涵段子爬虫类
	"""
	def __init__(self):
		self.page = 1
		self.switch = True

	def loadPage(self):
		"""
			读取页面内容
			page:需要请求的第几页
			return html页面
		"""
		fullurl = url + str(self.page) + ".html"
		header = {
			"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36"
		}

		request = urllib2.Request(fullurl, headers = header)
		response = urllib2.urlopen(request)
		html = response.read()
		# print fullurl, html
		return html

	def cleanData(self, html):
		"""
			处理页面,清洗数据
			html: html页面
			return 处理得到的段子列表
		"""
		
		gbk_html = html.decode('gbk').encode('utf-8')
		# print html
		# print gbk_html

		pattern = re.compile(r'<div class="f18 mb20">(.*?)</div>', re.S)
		m = pattern.findall(gbk_html)

		item_list = []
		for tmp in m:
			item_list.append(tmp)
		return item_list

	def writeToFile(self, filename, content_list):
		"""
			写入本地文件
			filename: 本地文件名
			content: 写入内容
		"""
		for tmp in content_list:
			# print tmp
			with open(filename, 'a') as f:
				f.write(tmp)

	def startWork(self):
		"""
			内涵段子爬虫类
		"""
		
		while self.switch:
			command = raw_input("是否爬取第" + str(self.page) +"页(Enter:继续, quit:退出)")
			if command == 'quit':
				self.switch = False
			
			html = self.loadPage()
			content_list = self.cleanData(html)
			self.writeToFile("./duanzi.txt", content_list)

			print "******* 第 %d 页 爬取完毕...*******" %self.page
			self.page += 1


if __name__ == '__main__':
	daunziSpider = Spider()
	daunziSpider.startWork()