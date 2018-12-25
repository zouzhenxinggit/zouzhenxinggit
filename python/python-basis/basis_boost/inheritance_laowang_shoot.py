#!/usr/bin/python3
#coding=utf-8

#躺在地上数人玩
print("laowang shoot")
		
class Ren(object):

	def __init__(self, name):
		self.name = name
		self.xue = 100
		self.qiang = None

	def __str__(self):
		if self.qiang:
			return self.name + "有枪," + "剩余血量" + str(self.xue)
		else :
			return self.name + "没枪," + "剩余血量" + str(self.xue)

	def zhaungzidan(self,danjia,zidan):
		danjia.baocunzidan(zidan)

	def zhuangdanjia(self,qiang, danjia):
		qiang.lianjiedanjia(danjia)

	def naqiang(self, qiang):
		self.qiang = qiang

	def kaiqiang(self, diren):
		self.qiang.fashezidan(diren)

	def diaoxue(self, shanghailiang):
		if self.xue - shanghailiang < 0:
			print("敌人没血了,子弹发射了 但是没有伤害")
		else :
			self.xue -= shanghailiang


class Danjia(object):

	def __init__(self, rongliang):
		self.rongliang = rongliang
		self.zidanshu = []

	def __str__(self):
		return "弹夹当前子弹数为:" + str(len(self.zidanshu)) + "/" + str(self.rongliang)

	def baocunzidan(self, zidan):
		if len(self.zidanshu) < self.rongliang:
			self.zidanshu.append(zidan)
			#print(self.zidanshu)
		else:
			print("弹夹满")

	def danjiazidanshu(self):
		return str(len(self.zidanshu)) + "/" + str(self.rongliang)

	def tanchuzidan(self):
		if self.zidanshu:
			tanchuzidan = self.zidanshu[-1]
			self.zidanshu.pop()		#删除列表最后一个元素
			return tanchuzidan
		else:
			return None
			print("弹夹没子弹了")


class Zidan(object):
	def __init__(self, shanghailiang):
		self.shanghailiang =10

	def shanghaidiren(self,diren):
		diren.diaoxue(self.shanghailiang)


class Qiang(object):
	def __init__(self):
		self.danjia = None

	def __str__(self):
		if self.danjia:
			return "枪有弹夹" + "弹夹里有" + self.danjia.danjiazidanshu() + "子弹"
		else :
			return "枪没有弹夹"

	def lianjiedanjia(self, danjia):
		if not self.danjia:
			self.danjia = danjia

	def fashezidan(self,diren):
		zidan = self.danjia.tanchuzidan()
		if zidan:
			zidan.shanghaidiren(diren)
		else:
			print("发射失败")

class AK47(Qiang):
	pass


class M4A1(Qiang):
	pass


class SanDanqiang(Qiang):
	#重写
	def fashezidan(self,diren):
		i = 0
		while i < 3:
			#调用父类同名函数
			super().fashezidan(diren)
			i+=1


laowang = Ren("laowang")

danjia = Danjia(20)
		
#给弹夹装装子弹
i=0
while i<15:
	zidan = Zidan(10)
	laowang.zhaungzidan(danjia, zidan)
	print(danjia)
	i+=1

#把弹夹放到枪里
qiang = SanDanqiang()
print(qiang)

#老王给枪装子弹
laowang.zhuangdanjia(qiang, danjia)
print(qiang)

#老王拿枪
print(laowang)
laowang.naqiang(qiang)
print(laowang)

#创建敌人
diren = Ren("diren")
print(diren)

#老王开枪射敌人
i = 0
while i < 11:
	laowang.kaiqiang(diren)
	print(diren)
	print(danjia)
	i+=1


