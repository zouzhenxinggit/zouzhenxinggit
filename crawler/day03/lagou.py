#!/usr/bin/python
#coding=utf-8


from bs4 import BeautifulSoup
import requests
import json
import jsonpath

url = "https://www.lagou.com/lbs/getAllCitySearchLabels.json"
headers = {
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36"
}

html = requests.get(url, headers = headers).text
# print html

html_py = json.loads(html)

citylist = jsonpath.jsonpath(html_py, "$..name")
# print citylist

content = json.dumps(citylist, ensure_ascii=False)
# print content

with open('city.json', 'w') as f:
	f.write(content.encode('utf-8'))