#!/usr/bin/python3
#coding=utf-8

print("return practice", end = "  \n")

def func(num1, num2):
	return num1 // num2, num1 %num2

a,b = func(5, 2)
print(a, b)

#返回是一个元祖
print( func(5, 2) )

c,d = (1,2.3)
print(c, d)

#缺省参数 这个缺省参数一定要放在最后边
def func_qx(a,b,c=10,d = 22):
	print(a)
	print(b)
	print(c)
	print(d)

func_qx(1,2,3,4)
func_qx(1,2,3)
func_qx(1,2)
func_qx(1,2, d = 50)

func_qx(b=1,a=8)

#不定长参数  不定长的参数部分会扔到 元祖或者字典里面去 这不是指针
#传递的时候只要没名字就会扔到元组里面去
print("不定长参数")
def func_buc(a,b,*args, **kwargs):
	print(a)
	print(b)
	print(args)
	print(kwargs)

func_buc(1,22,44,"sd",3.3,mm=44,nn=55)

A = [11,22,33]
B = {"aa":44,"bb":55}

func_buc(1,2,A,B)
func_buc(1,2,A,nn=B)

#*解包操作  *A 就是解包操作 *A ---> 11,22,33 **B -->aa=44,bb=55
print('*'*9)
print(*A)
print(*B)
print('*'*9)
func_buc(1,2,*A,**B) #==>func_buc(1,2,11,22,33,aa=44,bb=55)
func_buc(1,2,A,B)
