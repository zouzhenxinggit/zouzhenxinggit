#!/usr/bin/python3
#coding=utf-8

i = 0

while True :
	i+=1
	if i==5 : continue
	if i==15 : break

	print("wocao %d" %i)


print("break 和 continue 都是跳出当前循环\
 不同的是 continue 是跳过当前循环，进入下一循环")