#!/usr/bin/python3
#coding=utf-8



print("class_and_instance_attribute")





class Cat(object):

	#类属性
	num = 0

	def __init__(self):
		#实例属性
		self.age = 10
		#self.num = 111

	#这个cls是和self一样的 是啥都一样
	#传递谁就调用谁
	@classmethod
	def setNum(cls, num):
		cls.num = num
		pass

	def run(this):
		print("cat run------")

	@staticmethod
	def pri():
		print("------")




cat = Cat()

#用类名去访问类属性
print(Cat.num)
Cat.num += 1
print(Cat.num)

#用对象去访问类属性也可以但是有问题
#比如cat.num就会创建实例属性 表面修改
cat.num = 100000
print(Cat.num)
print(cat.num)

#通常用类方法去访问类属性 对象访问也行 是对象看到 修饰器也会变成类名
Cat.setNum(12553)
print(Cat.num)
cat.setNum(323)
print(Cat.num)

#静态方法 一个普通的函数放到类里
Cat.pri()
cat.pri()
#类名不能访问实例属性 没法访问啊 创建那么多对象 访问哪个啊



#总结
#对象可以访问类的所有方法 对象不能访问类属性(能访问是假象)
#类可以访问类属性 类方法 静态方法  不能访问实例属性 实例函数