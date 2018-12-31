#!/usr/bin/python3
#coding=utf-8

__all__ = ["Class_test", "test1"]

#可以根据__name__变量的结果能够判断出，是直接执行的python脚本(__main__)还是被加载模块的
if __name__ == "__main__":
	print("*"*100)

if __name__ == "myself_module":
	print("+"*100)

print("myself module")

class Class_test(object):
	def printf(self):
		print("------this-Class_test-----")

def test1():
	print("-------test1--------")

def test2():
	print("-------test2--------")

