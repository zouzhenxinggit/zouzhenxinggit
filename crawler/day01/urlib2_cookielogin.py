#!/usr/bin/python
#coding=utf-8

import urllib2

url = "http://www.renren.com/410043129/profile"


headers = {
    # "Host" : "www.renren.com",
    # "Connection" : "keep-alive",
    # #"Upgrade-Insecure-Requests" : "1",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    # "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    # "Referer" : "http://www.renren.com/SysHome.do",
    # #"Accept-Encoding" : "gzip, deflate, sdch",
    "Cookie": "anonymid=jsn03t7z4k7dzu; depovince=GW; _r01_=1; ick_login=af0f7317-f97d-43aa-bfa0-f2318e966ce8; jebe_key=7f916560-b255-43ba-a7cb-1a6a67d2a743%7Ccfcd208495d565ef66e7dff9f98764da%7C1551259893134%7C0; t=42ca62c359433f0690e2fab10b3e66f59; societyguester=42ca62c359433f0690e2fab10b3e66f59; id=969882339; xnsid=d1a62c08; jebecookies=5c749925-62de-4ee4-bb35-254fc79284d5|||||; ver=7.0; loginfrom=null"
}

request = urllib2.Request(url, headers = headers)
print urllib2.urlopen(request).read()