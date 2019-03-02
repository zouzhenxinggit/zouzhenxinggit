#!/usr/bin/python
#coding=utf-8


import urllib
import urllib2

url = "http://www.baidu.com"

# 构建一个HTTPHandler 处理器对象，支持处理HTTP请求
# http_hander = urllib2.HTTPHandler()
#调试信息
http_hander = urllib2.HTTPHandler(debuglevel=1)
# 构建一个HTTPHandler 处理器对象，支持处理HTTPS请求
# http_hander = urllib2.HTTPS_handler()

# 调用urllib2.build_opener()方法，创建支持处理HTTP请求的opener对象
opener = urllib2.build_opener(http_hander)

# 构建 Request请求
request = urllib2.Request(url)

# 调用自定义opener对象的open()方法，发送request请求
response = opener.open(request)

# 获取服务器响应内容
print response.read()








