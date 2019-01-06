#!/usr/bin/python3
#coding=utf-8


import sys
print(sys.path)
sys.path.append("/home/zouzhenxing/zouzhenxing_study_project/python/python-basis/plane")
print(sys.path)
from plane import * 



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

		#敌机做的工作
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
		time.sleep(0.001)

if __name__ == "__main__":
	print("play the plane")
	main()


