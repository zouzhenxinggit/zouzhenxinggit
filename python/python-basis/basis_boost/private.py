#!/usr/bin/python3
#coding=utf-8


print("private")


#__name __私有变量 不能在外部直接调用 内部函数可以调用
#__func __私有函数 不能在外部直接调用 内部函数可以通过self.__(xx)调用
class private:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def setage(self, age):
        self.__age = age
    
    def getage(self):
        return self.__age

    def __func(self):
        print("__func")

    def fun(self):
        self.__func()
        print("func")

pp = private("laowang", 30)
print(pp)

age = pp.getage()
print(age)

pp.setage(40)

age = pp.getage()
print(age)

pp.fun()



#但有时候我就是想调用私有成员函数怎么办
#私有成员函数本质就是该函数名 _类名__函数名 找不到就无法调用
class Test(object):
	def __func(self):
		print("__func")


print(dir(Test))
test = Test()
test._Test__func()
'''
['_Test__func',
 '__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__']

'''


