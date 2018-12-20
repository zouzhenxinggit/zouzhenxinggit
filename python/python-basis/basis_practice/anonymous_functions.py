#!/usr/bin/python3
#coding=utf-8

print("anonymous_functions")

aa = lambda x, y : x+y

print (aa(1,3))


#实现加减乘除四个函数

def function(a,b,c):
	return c(a,b)

resufls = function(11,22,lambda x,y :x*y)
'''
resufls = function(11,22,lambda x,y :x/y)
resufls = function(11,22,lambda x,y :x+y)
resufls = function(11,22,lambda x,y :x-y)
'''

print(resufls)



#给字典排序
bb = [{"id":22,"age":23}, {"id":25,"age":11}, {"id":21,"age":19}]

bb.sort(key=lambda x:x["age"],	reverse=True)
print(bb)



#函数名重名会覆盖
