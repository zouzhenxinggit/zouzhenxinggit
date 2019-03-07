#!/usr/bin/python
#coding=utf-8

from bs4 import BeautifulSoup
import requests
import json

def tencentCookie():
	#创建session对象，可以保存Cookie值
	ssion = requests.Session()

	headers = {
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36"
	}

	url = "https://hr.tencent.com/position.php?&start=10#a"
	html = ssion.get(url, verify = False, headers = headers).text
	
	bs = BeautifulSoup(html, "lxml")
	
	result = bs.select('tr[class="even"]')
	result1 = bs.select('tr[class="odd"]')
	result += result1

	items = []
	for m in result:
		# print m
		item = {}
		name = m.select('td')[0].get_text()
		detailink = m.select('td a')[0].attrs['href']
		classification = m.select('td')[1].get_text()
		number_of = m.select('td')[2].get_text()
		city = m.select('td')[3].get_text()
		time = m.select('td')[4].get_text()
		# https://hr.tencent.com/position_detail.php?id=48141&keywords=&tid=0&lid=0
		# print name, detailink, classification, number_of, city, time

		item['name'] = name
		item['detailink'] = "https://hr.tencent.com/" + detailink
		item['classification'] = classification
		item['number_of'] = number_of
		item['city'] = city
		item['time'] = time

		items.append(item)

	# for x in items:
	# 	print x['name']
	# 	print x['detailink']
	# 	print x['classification']
	# 	print x['number_of']
	# 	print x['city']
	# 	print x['time']

	line = json.dumps(items,ensure_ascii=False)
	# print line

	with open('tencent.json', 'w') as f:
		f.write(line.encode("utf-8"))

if __name__ == "__main__":
	tencentCookie()
