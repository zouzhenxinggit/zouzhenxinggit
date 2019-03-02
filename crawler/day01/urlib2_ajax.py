#!/usr/bin/python
#coding=utf-8


#ajax加载
#HTTPS请求 SSL证书验证

import urllib
import urllib2

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action"

headers = {
	"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36"
}

formdata = {
        "start":"0",
        "limit":"20"
}

data = urllib.urlencode(formdata)


print data


request = urllib2.Request(url, headers = headers, data = data)

response = urllib2.urlopen(request)

html = response.read()

print html