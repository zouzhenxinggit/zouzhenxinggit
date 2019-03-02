#!/usr/bin/python
#coding=utf-8

import urllib
import urllib2
import random
from lxml import etree 

imagenumber = 1

def loadPage(url):
    """
        作用：根据url发送请求，获取服务器响应文件
        url：需要爬取的url地址
        return 页面内容
    """
    header = {
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"
	}
    request = urllib2.Request(url)#, headers = header)
    return urllib2.urlopen(request).read()


def writeToFile(url, filename):
	"""
		得到网页中的图片 保存到本地
		url: 图片链接
		filename: 本地文件名
	"""
	Page = loadPage(url)
	content = etree.HTML(Page)
	content_list = content.xpath('//img[@class="BDE_Image"]/@src')

	global imagenumber
	for tmp in content_list:
		image = loadPage(tmp)

		print tmp
		with open(filename, 'wb') as f:
			f.write(image)
			print '---下载第%d图片完成---' %imagenumber
			imagenumber += 1


# 得到帖子所有的图片的链接
def get_picture_link(content_list):
	"""
			下载图片然后保存到本地
			url: 图片链接
			filename: 本地文件名
	"""
	url = "https://tieba.baidu.com"
	for tmp in content_list:
		fullurl = url + tmp
		writeToFile(fullurl, fullurl[-5:] + '.jpg')


def tiebaSpider(url, beginPage, endPage):
	"""
        贴吧爬虫调度器: 组合url	获得贴吧所有帖子的链接
        url : 贴吧url的前部分
        beginPage : 起始页
        endPage : 结束页
    """
	for tmp in range(beginPage, endPage + 1):
		pn = (tmp - 1) * 50
		fullurl = url + '&pn=' + str(pn)
		# print fullurl

		html = loadPage(fullurl)
		# print html

		content = etree.HTML(html)
		content_list = content.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')
		# content_list = content.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')

		picture_list = get_picture_link(content_list)


if __name__ == "__main__":
	kw = raw_input("请输入需要爬取的贴吧名：")
	beginPage = int(raw_input("请输入起始页："))
	endPage = int(raw_input("请输入结束页："))

	key = urllib.urlencode({"kw": kw})


	url = "http://tieba.baidu.com/f"
	fullurl = url + '?' + key
	# print fullurl
	tiebaSpider(fullurl, beginPage, endPage)
