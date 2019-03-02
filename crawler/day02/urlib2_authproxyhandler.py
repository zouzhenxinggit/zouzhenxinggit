#!/usr/bin/python
#coding=utf-8

# 不用这种方法
# import urllib2
# import urllib

# # 私密代理授权的账户
# user = "mr_mao_hacker"
# # 私密代理授权的密码
# passwd = "sffqry9r"
# # 私密代理 IP
# proxyserver = "61.158.163.130:16816"

# # 1. 构建一个密码管理对象，用来保存需要处理的用户名和密码
# passwdmgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

# # 2. 添加账户信息，第一个参数realm是与远程服务器相关的域信息，一般没人管它都是写None，后面三个参数分别是 代理服务器、用户名、密码
# passwdmgr.add_password(None, proxyserver, user, passwd)

# # 3. 构建一个代理基础用户名/密码验证的ProxyBasicAuthHandler处理器对象，参数是创建的密码管理对象
# #   注意，这里不再使用普通ProxyHandler类了
# proxyauth_handler = urllib2.ProxyBasicAuthHandler(passwdmgr)

# # 4. 通过 build_opener()方法使用这些代理Handler对象，创建自定义opener对象，参数包括构建的 proxy_handler 和 proxyauth_handler
# opener = urllib2.build_opener(proxyauth_handler)

# # 5. 构造Request 请求
# request = urllib2.Request("http://www.baidu.com/")

# # 6. 使用自定义opener发送请求
# response = opener.open(request)

# # 7. 打印响应内容
# print response.read()


import urllib2
import urllib

# 私密代理密码账号
user = "mr_mao_hacker"

# 私密代理授权的密码
passwd = "sffqry9r"

# 私密代理 IP
proxy = "61.158.163.130:16816"

full_private_proxy = {
	"https": user + ":" + user + "@" + proxy
}

print full_private_proxy

url = "http://www.baidu.com/"

httpproxy_handler = urllib2.ProxyHandler(full_private_proxy)

opener = urllib2.build_opener(httpproxy_handler)

request = urllib2.Request(url)

response = opener.open(request)

print response.read()


# 密码写在用户环境变量里 ~/.bashrc
# proxyuser="mr_mao_hacker"
# export proxyuser
import os

name = os.environ.get("proxyuser")

print name

# 然后在拼接成新的full_private_proxy