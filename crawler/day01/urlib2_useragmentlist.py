#!/usr/bin/python
#coding=utf-8


import urllib2
import random

url = "http://www.baidu.com/"

# 可以是User-Agent列表，也可以是代理列表
ua_list = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
]

# 通过urllib2.Request() 方法构造一个请求对象
request = urllib2.Request(url)

# 在User-Agent列表里随机选择一个User-Agent
user_agent = random.choice(ua_list)

request.add_header("User-Agent", user_agent)

# print request.get_header("User-agent") ;


# 向指定的url地址发送请求，并返回服务器响应的类文件对象
response = urllib2.urlopen(request)

# read()方法就是读取文件里的全部内容，返回字符串
html = response.read()

print html

# 返回 HTTP的响应码，成功返回200，4服务器页面出错，5服务器问题
print response.getcode()
