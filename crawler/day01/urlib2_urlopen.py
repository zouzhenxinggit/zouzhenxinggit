#!/usr/bin/python
#coding=utf-8

#urllib2 在 python3.x 中被改为urllib.request 我用了但是3不太好用 
import urllib2

# 向指定的url地址发送请求，并返回服务器响应的类文件对象
response = urllib2.urlopen("http://www.baidu.com/")

# 服务器返回的类文件对象
html = response.read()

# 打印响应内容
print html



