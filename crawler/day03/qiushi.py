#!/usr/bin/python
#coding=utf-8

from bs4 import BeautifulSoup
from lxml import etree 
import requests
import json

page = 2 #奇数有问题

url = "https://www.qiushibaike.com/8hr/page/"

headers = {
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36"
}

fullurl = url + str(page)
sion = requests.get(fullurl, headers = headers).text

# print sion
content = etree.HTML(sion)
node_list = content.xpath('//li[contains(@id, "qiushi_tag")]')									


for node in node_list:
	username = node.xpath('./div//@alt')[0]
	image = node.xpath('.//img//@src')[0]
	content = node.xpath('.//div[@class="recmd-right"]/a')[0].text
	zan = node.xpath('.//span')[0].text
	comments = node.xpath('.//span')[3].text


	# print username, image, content, zan, comments
	items = {
		"username": username,
		"image": "https:" + image,
		"content": content,
		"zan": zan,
		"comments": comments
	}

	content = json.dumps(items,ensure_ascii=False)

	with open("qiushi.json", "a") as f:
		f.write(content.encode("utf-8") + "\n")