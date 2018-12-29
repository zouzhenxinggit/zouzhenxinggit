#!/usr/bin/python3
#coding=utf-8

print("singleon_pattern_factory_method")


#编写一个工厂模式+单例模式
#大哥要来哈尔滨玩
#他要好玩的 -> 冰雪大世界
#他要好吃的 -> 锅包肉

#创建大哥类
class Dage(object):
	
	def create(self):
		pass

	def Choice(self, typename):
		self.happy = self.create(typename)
		self.happy.play()


#创建我带大哥玩的类
class Zouzhenxing(Dage):
	def create(self,typename):
		self.factory = Factory()
		print(self.factory)
		return self.factory.backmethod(typename)


#创建工厂(单例模式)
class Factory(object):

	__instance = None
	__first_init = False

	def __init__(self):
		if not Factory.__first_init:
			print("第一次初始化")
			Factory.__first_init = True
	
	def __new__(cls):
		if not Factory.__instance:
			#cls.__instance = object.__new__(cls)
			Factory.__instance = super().__new__(cls)
		return Factory.__instance

	def backmethod(self,typename):
		if typename == "eat":
			tmp = Guobaorou()
		elif typename == "play":
			tmp = Bingxuedashijie()
		return tmp


class Bingxuedashijie(object):
	def play(self):
		print("冰雪大世界真好玩")

class Guobaorou(object):
	def play(self):
		print("锅包肉真好吃")




zou = Zouzhenxing()
zou.Choice("play")

zou2 = Zouzhenxing()
zou.Choice("eat")