#!/usr/bin/python3
#coding=utf-8

username = input("请输入用户名\n")
password = input("请输入密码\n")

if username == "zouzhenxing" and password == "123456" :
	print("登陆成功！尊敬的%s会员欢迎您!" %username)
else :
	print("登陆失败！请重试")

if ( password == "king private" or password == "zouzhenxing") :
	print("您激活隐藏最高权限")

#not 就是！
num = int(input("输入一个数字\n"))

if not (num >= 3 and num <=7) :
	print("请到办公室领奖")

#elif
numm = int(input("输入一个数字"))

if numm == 1:
	print("numm == %d" %numm)
elif numm == 2:
	print("numm == %d" %numm)
elif numm == 3:
	print("numm == %d" %numm)
else :
	print("other")
