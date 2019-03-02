#!/usr/bin/python
#coding=utf-8

import urllib
import urllib2
import cookielib


#构建一个CookieJar对象来保存cookie
cookiejar = cookielib.CookieJar()

#使用HTTPCookieProcessor来创建handler_cookie处理器对象
handler_cookie = urllib2.HTTPCookieProcessor(cookiejar)

#通过build_opener来构建opener
opener = urllib2.build_opener(handler_cookie)


url = "http://www.renren.com/PLogin.do"

formdata = {
	"email": "15145100618",
	"password": "zouge666666"
}

data = urllib.urlencode(formdata)

print data

#第一次登录获取cookie
request = urllib2.Request(url, data = data)
response = opener.open(request)
print response.read()
print "*\n" * 30

#第二次登录获取cookie 之前opener保存了cookie直接登录就行
url_dyj = "http://www.renren.com/410043129/profile"
print opener.open(url_dyj).read()
print "*\n" * 30



# cookieStr = ""
# for item in cookiejar:
#     cookieStr = cookieStr + item.name + "=" + item.value + ";"

# ## 舍去最后一位的分号
# print cookieStr[:-1]