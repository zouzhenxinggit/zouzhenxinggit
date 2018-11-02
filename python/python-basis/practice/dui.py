#!/usr/bin/python3
#coding=utf-8

score = int(input("请输入您当前的分数\n"))

serial_number = input("请输入您的违章 1：闯红灯 2：酒驾\n")

print("根据输入计算分数.....")

if serial_number == '1':
	score -=3
if serial_number == '2':
	score -=6

if score >= 0:
	print("您剩余的分数是：%d" %score)
else :
	print("您当前分数<0\
请重新学习")
