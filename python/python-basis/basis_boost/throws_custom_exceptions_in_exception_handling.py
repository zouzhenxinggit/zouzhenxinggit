#!/usr/bin/python3
#coding=utf-8

#在异常处理中抛出自定义异常
print("Throws custom exceptions in exception handling")

class Self_exception(Exception):
	def __init__(self,m,n):
		self.m = m
		self.n = n

	def __str__(self):
		return "测试异常	m:" + str(self.m)  + "n:" + str(self.n)


class Test(object):
	def __init__(self, switch):
		self.switch = switch

	def cacl(self,a,b):
		try :
			return a/b
		
		except Exception as resulf:
			if self.switch:
				print("捕获异常处理异常:%s"%resulf)
			else:
				try:
					raise Self_exception(100,200)
				except Self_exception as resulf:
					print("异常中抛出自定义异常:%s" %resulf)



a = Test(True)
a.cacl(11,0)

print("----------------------华丽的分割线----------------")

a.switch = False
a.cacl(11,0)
