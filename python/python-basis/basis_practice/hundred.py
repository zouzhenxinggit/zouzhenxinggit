#!/usr/bin/python3
#coding=utf-8

print("打印1-100数的和")
i = 1
s = 0

while i <= 100 :
	i += 1
	s += i
print("1-100数的和%d" %s)






print("打印1-100所有的偶数")
i = 1
s = 0

while i <= 100 :
	i += 1
	if i%2 == 0 :
		print("%d" %i , end = " ")
print()






print("打印1-100所有的偶数的和")
i = 1
s = 0

while i <= 100 :
	i += 1
	if i%2 == 0 :
		s += i
print("1-100所有的偶数%d" %s)



'''
*
**
***
****
*****
'''
print("while循环嵌套")

i = 1
while i <= 5 :
	print("*"*i)
	i += 1


print("乘法口诀")
x = 1
while x <= 9:
	y = 1

	while y <= x :
		print("%d*%d=%-2d  " %(y, x, x*y), end = " ")
		y += 1

	print()
	x += 1

'''
m = 1
x = 1

while m <= 9:
	n = 1
	y = 1

	while n <= m :
		print("%d*%d=%-2d  " %(y, x, x*y), end = " ")
		n += 1
		y += 1

	print()
	m += 1
	x += 1'
	'''