#!/usr/bin/python3
#coding=utf-8

ticket = 1 #1:有车票 0:没车票
knife_lenght = 8 #刀的长度 刀大于10等检查吧吧

if ticket == 1:
	if knife_lenght < 10:
		print("上车回家")
	else:
		print("刀太长了")
		print("等待警察叔叔")
else:
	print("没票")



