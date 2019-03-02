#!/usr/bin/python
#coding=utf-8


#post 请求


import urllib
import urllib2

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

headers = {
	"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36"
}

key = raw_input("请输入要翻译的东西：")

formdata = {
	"i": key,
	"from": "AUTO",
	"to": "AUTO",
	"smartresult": "dict",
	"client": "fanyideskweb",
	"salt": "15512364405104",
	"sign": "738bb0ce3da5d6380bb56ed1fa03bd0c",
	"ts": "1551236440510",
	"bv": "67a416fcf7fdeed24f58a30cccce190d",
	"doctype": "json",
	"version": "2.1",
	"keyfrom": "fanyi.web",
	"action": "FY_BY_CLICKBUTTION",
	"typoResult": "false"
}

data = urllib.urlencode(formdata)
print data

request = urllib2.Request(url, data = data, headers = headers)

html = urllib2.urlopen(request).read()

print html
