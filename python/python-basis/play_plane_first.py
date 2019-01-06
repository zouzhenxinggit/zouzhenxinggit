#!/usr/bin/python3
#coding=utf-8

import pygame
import time
import random
from pygame.locals import *



class HeroBullet(object):
	def __init__(self,position,screen):
		self.x = position[0] + 40
		self.y = position[1]
		self.distance = 1
		self.screen = screen
		self.imageName = "./plane/bullet-3.gif"
		self.image = pygame.image.load(self.imageName).convert()

	def display(self):
		self.screen.blit(self.image,(self.x,self.y))
		#self.screen.blit(self.image,(100,100))
	
	def move_direction(self):
		self.y -= self.distance

	def judgeout(self):
		if self.y < 1 :
			return True
		else :
			return False


class EnemyBullet(object):
	def __init__(self,position,screen):
		self.x = position[0] + 25
		self.y = position[1]
		self.distance = 1
		self.screen = screen
		self.imageName = "./plane/bullet-1.gif"
		self.image = pygame.image.load(self.imageName).convert()

	def display(self):
		self.screen.blit(self.image,(self.x,self.y))
		#self.screen.blit(self.image,(100,100))
	
	def move_direction(self):
		self.y += self.distance

	def judgeout(self):
		if self.y > 852 :
			return True
		else :
			return False






class EnemyPlane(object):
	def __init__(self, screen):
		self.screen = screen
		self.position = [0,0]
		#距离
		self.distance = 1
		#方向
		self.direction = "right"
		self.imageName = "./plane/enemy-1.gif"
		self.image = pygame.image.load(self.imageName).convert()
		self.bulletList = []

	def display(self):
		self.screen.blit(self.image,(self.position[0],self.position[1]))

		time.sleep(0.001)
		needRemoveList = []	#这里存放的是引用

		for tempBullet in self.bulletList:
			if tempBullet.judgeout():
				needRemoveList.append(tempBullet)

		for tempBullet in needRemoveList:
			self.bulletList.remove(tempBullet)

		#print(len(self.bulletList))
		for tmp in self.bulletList:
			tmp.display()
			tmp.move_direction()

	def move_direction(self,direction):
		if direction == "right":
			self.position[0]  += self.distance
		elif direction == "left":
			self.position[0] -= self.distance

	def change_direction(self):
		if self.position[0] > 430:
			self.direction = "left"
		elif self.position[0] < 0:
			self.direction = "right"

	def fire_bullet(self):
		if random.randint(0,100) == 50:
			bullet = EnemyBullet(self.position,self.screen)
			self.bulletList.append(bullet)



class HeroPlane(object):
	def __init__(self, screen):
		self.screen = screen
		self.position = [230,600]
		self.distance = 20
		self.imageName = "./plane/hero.gif"
		self.image = pygame.image.load(self.imageName).convert()
		self.bulletList = []

	def display(self):
		self.screen.blit(self.image,(self.position[0],self.position[1]))

		time.sleep(0.001)
		needRemoveList = []	#这里存放的是引用

		for tempBullet in self.bulletList:
			if tempBullet.judgeout():
				needRemoveList.append(tempBullet)

		for tempBullet in needRemoveList:
			self.bulletList.remove(tempBullet)

		#print(len(self.bulletList))
		for tmp in self.bulletList:
			tmp.display()
			tmp.move_direction()

	def move_direction(self,direction):
		if direction == "right":
			self.position[0]  += self.distance
		elif direction == "left":
			self.position[0] -= self.distance

	def fire_bullet(self):
		bullet = HeroBullet(self.position,self.screen)
		self.bulletList.append(bullet)



def main():
	#创建一个窗口
	screen = pygame.display.set_mode((480,852),0,32)
	#创建一个背景图片
	background = pygame.image.load("./plane/background.png").convert()
	#创建英雄飞机对象
	heroplane = HeroPlane(screen)
	#创建敌人飞机对象
	enemyplane = EnemyPlane(screen)

	while True:

		#把背景图片放在窗口
		screen.blit(background,(0,0))
		heroplane.display()

		enemyplane.fire_bullet()
		enemyplane.display()
		enemyplane.move_direction(enemyplane.direction)



		enemyplane.change_direction()



		#获取事件，比如按键等
		for event in pygame.event.get():

			#判断是否点击了退出按钮
			if event.type == QUIT:
				print("exit")
				exit()

			#判断是否按下了退出按钮
			elif event.type == KEYDOWN:
				if event.key == K_a or event.key == K_LEFT:
					heroplane.move_direction("left")
					print("left")

				elif event.key == K_d or event.key == K_RIGHT:
					heroplane.move_direction("right")
					print("right'")

				elif event.key == K_w or event.key == K_UP:
					print("up")

				elif event.key == K_s or event.key == K_DOWN:
					print("down")

				elif event.key == K_SPACE:
					heroplane.fire_bullet()
					print('space')

		#更新显示
		pygame.display.update()


if __name__ == "__main__":
	print("play the plane")
	main()


