#!/usr/bin/python3
#coding=utf-8

import random

while True :
	computer	= random.randint(1, 3)
	print(computer)

	print("猜拳游戏")
	person = int(input("请选择：剪刀 (1) 石头 (2) 布 (3) \n"))

	if (person == 1 and computer == 3) \
	or (person == 2 and computer == 1) \
	or (person == 3 and computer == 2):
		print("赢了")
	elif person == computer :
		print("平局")
	else :
		print("输了")

