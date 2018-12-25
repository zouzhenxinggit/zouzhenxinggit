#!/usr/bin/python3
#coding=utf-8


class Ma(object):
	def pao(self):
		print("马在跑")

	def jiao(self):
		print("马在叫")


class Lv(object):
	def tuowupin(self):
		print("驴托物品")

	def jiao(self):
		print("驴在叫")


class Luozi(Ma, Lv):
	pass

luozi = Luozi()
luozi.pao()
luozi.tuowupin()
		
#当两个父类都有同名函数的时候 跟继承顺序有关
luozi.jiao()

#当类的继承情况很复杂的时候 有一个mro算法 很复杂 同名函数就优先从__mro__列表开始找
print(Luozi.__mro__)
#(<class '__main__.Luozi'>, <class '__main__.Ma'>, <class '__main__.Lv'>, <class 'object'>)