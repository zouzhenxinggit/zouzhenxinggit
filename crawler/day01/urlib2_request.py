#!/usr/bin/python
#coding=utf-8


import urllib2

ua_headers = {
	"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36"
}

# 通过urllib2.Request() 方法构造一个请求对象
url = "http://www.baidu.com/"
request = urllib2.Request(url, headers = ua_headers)

# 向指定的url地址发送请求，并返回服务器响应的类文件对象
response = urllib2.urlopen(request)

# read()方法就是读取文件里的全部内容，返回字符串
html = response.read()

print html

# 返回 HTTP的响应码，成功返回200，4服务器页面出错，5服务器问题
print response.getcode()
