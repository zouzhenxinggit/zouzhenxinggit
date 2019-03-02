#!/usr/bin/python
#coding=utf-8

# ctrl+KU 转换文字为大写
# ctrl+KL 转换文字为小写

import urllib
import urllib2
import random


url = "http://www.baidu.com"

# https://www.xicidaili.com/
proxy_list = [
	{ "https": "116.209.54.9" },
	{ "https": "116.209.59.222" },
	{ "https": "218.17.139.5" },
	{ "https": "60.216.101.46" }	
]

# 构建了两个代理Handler，一个有代理IP，一个没有代理IP
# httpproxy_handler = urllib2.ProxyHandler({"https": "218.17.139.5"})
httpproxy_handler = urllib2.ProxyHandler(random.choice(proxy_list))
nullproxy_handler = urllib2.ProxyHandler({})

#定义一个代理开关
proxySwitch = True

# 通过 urllib2.build_opener()方法使用这些代理Handler对象，创建自定义opener对象
# 根据代理开关是否打开，使用不同的代理模式
if proxySwitch:
	opener = urllib2.build_opener(httpproxy_handler)
else:
	opener = urllib2.build_opener(nullproxy_handler)

request = urllib2.Request(url)


# 1. 如果这么写，只有使用opener.open()方法发送请求才使用自定义的代理，而urlopen()则不使用自定义代理。
# reposen = opener.open(request)

# 2. 如果这么写，就是将opener应用到全局，之后所有的，不管是opener.open()还是urlopen() 发送请求，都将使用自定义代理。
urllib2.install_opener(opener)
reposen = urllib2.urlopen(request)

print reposen.read()
