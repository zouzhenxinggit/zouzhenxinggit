#!/usr/bin/python3
#coding=utf-8
import random

#一个学校，有3个办公室，现在有8位老师等待工位的分配，请编写程序，完成随机的分配

rome = [[],[],[]]
teacher = ['A','B','C','D','E','F','G','H']

for tmp in teacher :
	rome[random.randint(0,2)].append(tmp)

#方法1
#print(rome)

'''方法2
for tmp1 in rome :
	print(tmp1)'''

#方法3
i = 1
for tmp1 in rome :
	print("房间%d中老师是：")
	for tmp2 in tmp1 :
		print(tmp2, end = " ")
	print(end = '\n')
	i += 1