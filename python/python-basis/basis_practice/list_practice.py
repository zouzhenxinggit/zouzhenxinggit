#!/usr/bin/python3
#coding=utf-8

name = []

while True :
	print("*"*30)
	print("	欢迎使用xxx系统  v6.08")
	print("1:添加一个新名字")
	print("2:删除一个新名字")
	print("3:修改一个名字")
	print("4:查询一个名字")
	print("5:遍历所有的名字")
	print("0:退出系统")
	print("*"*30)

	key = input("请输入您要的数字")

	if key == '1':
		newname = input("请输入要添加的新名字")
		name.append(newname)

	elif key == '2':
		print("*"*30)
		newname = input("请输入要删除名字")
		if newname in name:
			name.remove(newname)
		else :
			print("没有这个要删除名字")

	elif key == '3':
		print("*"*30)
		newname1 = input("请输入要修改哪个名字")
		newname2 = input("请输入要修改成什么")
		if newname1 in name:
			name[name.index(newname1)] = newname2
		else :
			print("没有这个名字")

	elif key == '4':
		print("*"*30)
		newname = input("请输入要查询的名字")
		if newname in name:
			print("您输入的名字索引:%d" %(name.index(newname)))
			print(name[name.index(newname)])
		else :
			print("没有这个名字")

	elif key == '5':
		print("*"*30)
		for tmp in name:
			print(tmp)

	elif key == '0':
		print("*"*30)
		print("退出系统")
		break
	else:
		print("*"*30)
		print("无效命令")