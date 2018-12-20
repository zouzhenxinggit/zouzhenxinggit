#!/usr/bin/python3
#coding=utf-8

print("file wr")

f = open('text.txt', "w")
f.write("www1www2www3www4ww\
	qweqwewqew write\nwew write\nwewq write\nwewew write\n")
f.close()

f = open('text.txt', "r")

str = f.read(5)
print(str)

str = f.read(5)
print(str)

f.close()

print(type(str))



f = open('text.txt', "r")

str = f.read()
print(str)

f.close()


print("*"*9)

f = open('text.txt', "r")
print(f.readline())		#读一行
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())

f.close()


f = open('text.txt', "r")
print(f.readlines())

#readlines把每一行都当做列表的一个元素


#取出文件名的后缀                         
filename = "Zou.txt.exe"
print( filename[filename.find('.') : : ])
print( filename[filename.rfind('.') : : ])
print( filename.find('.'))