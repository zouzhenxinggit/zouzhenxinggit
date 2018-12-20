#!/usr/bin/python3
#coding=utf-8

print("全局变量和局部变量")

import time

def A():
	num = 10
	print(num)

def B():
	num = 20
	print(num)
	time.sleep(1)
	num += 100
	print(num)



B()
A()


glo_num = 100

def C():
	#global glonum
	glo_num = 10
	print(glo_num)

def D():
	print(glo_num)

print("*"*10)
C()
D()

#全局变量
#修改的时候需要+global 也有可能会被局部同名变量覆盖 也有可能会挂

#但是一种情况突破了界限 那就是append类似的函数 不需要+global

glo_list = []

def E():
	glo_list = [11,22]
	print(glo_list)

def F():
	glo_list.append(11)
	print(glo_list)

print("*"*10)
print(glo_list)
E();
print(glo_list)
print("*"*10)
F();
print(glo_list)
