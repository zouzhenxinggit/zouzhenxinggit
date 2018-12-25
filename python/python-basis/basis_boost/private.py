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