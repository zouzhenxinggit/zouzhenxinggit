#!/usr/bin/python3
#coding=utf-8

stuinfos = []


def addinfos():
	print("添加学生信息")
	newname = input("请输入添加的学生姓名：")
	newsex = input("请输入添加的学生性别(nan/nv)：")
	newphone = input("请输入添加的学生电话：")

	newinfo = {}
	newinfo['name'] = newname
	newinfo['sex'] = newsex
	newinfo['phone'] = newphone
	return newinfo


def printfinfos():
	pass
	print(25*"=")
	print("	学生管理系统 v1.0")
	print("1：添加学生信息")
	print("2：删除学生信息")
	print("3：修改学生信息")
	print("4：查询学生信息")
	print("5：显示所有学生信息")
	print("0：退出系统")


def main():
	while True:
		printfinfos()

		key = input("请选择要执行的操作")

		if key == '1':
			info = addinfos()
			stuinfos.append(info)

		elif key == '2':
			print("删除学生信息")
			stuid = int(input("请输入要删除的学生ID："))
			del stuinfos[stuid-1]

		elif key == '3':
			print("修改学生信息")
			stuid = int(input("请输入要修改的学生ID："))
			newname = input("请重新输入学生姓名：")
			newsex = input("请重新输入学生性别(nan/nv)：")
			newphone = input("请重新输入学生电话：")

			stuinfos[stuid-1]['name'] = newname
			stuinfos[stuid-1]['sex'] = newsex
			stuinfos[stuid-1]['phone'] = newphone

		elif key == '4':
			print("查询学生信息")
			stuid = int(input("请输入要查询的学生ID："))
			'''
			for tmp in stuinfos[stuid-1].items() :
				print("%s %s" %(tmp[0], tmp[1]))

			for key,value in stuinfos[stuid-1].items() :
				print("%s %s" %(key, value))
			'''
			print( "name:%s" %stuinfos[stuid-1]['name'] ) 
			print( "sex:%s" %(stuinfos[stuid-1]['sex']) )
			print( "phone:%s" %(stuinfos[stuid-1]['phone']) )

		elif key == '5':
			print("显示所有学生信息")
			print("序号		姓名		性别		电话")
			for i,tmp in enumerate(stuinfos):
				print("%-15d%-15s%-15s%-15s" %(i+1,tmp['name'],tmp['sex'],tmp['phone']))

		elif key == '0':
			print("退出系统")
			break
		else:
			print("未知错误")
			pass

'''
def addinfos(): #在这里也行 因为只要定义在main函数之前就行 
#main函数执行的时候会在main函数之前的作用域寻找子函数 找不到就挂
def printfinfos():	'''

main();
