#!//usr/bin/python3
#coding=utf-8

print("hello word")
'''
	Multiline comment
'''
print("中文")

name = "zouzhenxing"
age = 100

print(name)
print(age)

age += 1
print(age)

print(type(name))
print(type(age))

#python2 is ok ,python 3 not ok
#print name

import keyword
print(keyword.kwlist)

'''
all this is  keyword ，don't name variable
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 
'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import',
 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
 '''

print("zou zhen xing")
print("zou \nzhen \nxing")
print("zou \t zhen \t xing")

print(name+str(age))

print("my fuck %d" %age)
print("my name : %s my age : %d" %(name,age))


#ipython3
#help(print)
#dir(print)

print("my fuck", end = "  -iy- ")
print("my fuck", end = "")
print("my fuck")

myName = input("请输入名字\n")
print("你刚刚输入的名字是%s" %(myName), end = "ooo\n")

print("------------------------------------")
myName2 = input("myName is input")
print(myName2)

mynum	= input("输入数字\n")   #<---213123 
print(type(mynum))

'''
	python2 
	p2 = raw_input("abcd1")		the same as  python3		 input("abcd2")

	M = input("please in")  <--- 3+4
	print(M) ---> 7
	M = raw_input("please in")  <--- 3+4
	print(M) ---> 3+4
'''

#python3
p3 = input("abcd2")
print(type(age))
print(type(p3))
print("%d" ,int(p3))


print("%s + %s = %d" %(str(age), p3, age+int(p3)))