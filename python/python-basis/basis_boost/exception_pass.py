#!/usr/bin/python3
#coding=utf-8


print("exception_pass")

#异常的传递

def text1():
	print("------1-1-----")
	print(a)
	print("------1-2-----")

def text2():
	print("------2-1-----")
	text1()
	print("------2-2-----")

def text3():
	try:
		print("------3-1-----")
		text1()
		print("------3-2-----")
	except:
		print("err")

	print("----异常处理之后继续执行-----")

#text2()

text3()


'''
异常的传递
A->B->C->D D有异常 D没有异常处理 传给C 
C没有异常处理传给B 
一直传到处理的位置
若传到头也没有异常处理 就按照默认的办
'''