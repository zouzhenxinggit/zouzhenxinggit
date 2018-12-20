#!/usr/bin/python3
#coding=utf-8

print("list 元素列表遍历")

roster = ["zhenxing","hongtao","weichao"]
roster1 = ["zhenxing","hongtao","weichao"]
roster2 = ["zhenxing","hongtao","weichao"]
each_name = input("请输入要查找的名字：")

#方法1
flag = 0
for tmp in roster :
	if tmp == each_name :
		flag = 1
		break

if  flag :
	print("找到了")

else :
	print("没找到 手动添加")
	roster.append(each_name)

print("*"*20)
print(roster)


print("*"*50)
#方法2
if each_name in  roster1:
	print("找到了")
else :
	print("没找到")
print(roster1)

print("*"*50)
#方法3
if each_name not in  roster2:
	print("没找到 手动添加")
	roster2.append(each_name)
else :
	print("找到了")
print(roster2)