#!/usr/bin/python3
#coding=utf-8

#内存与引用 引用引出可变与不可变 引出字典的存储方式(哈希算法)
print("memory and references")



#可变与不可变
#id 内存地址
a = 10
b = a
print(id(a))
print(id(b))

a = 20
print(id(a)) 


A = [11,22]
B = A

A.append(33)
print(A)
print(B)

print(id(A))
print(id(B))

'''
#这现象是为什么呢 就是可变与不可变
a=b=10
a和b都指向10 10是不可修改的 所以让a重新指向20

但是A和B都指向[11,22] 修改A 列表是可修改的 所以修改A B也跟着就改变了
'''

'''可变类型与不可变类型
可变:列表 字典
不可变:常亮 元祖 字符串
'''

'''
字典的键值是不可变的 平时不是用字符串吗 (11,22) 110都行
'''
xx = (22,42)
C = {"name":"wocao", 100:10000, (11,22):50, xx:22222}
print(C)
print(C["name"])
print(C[100])
print(C[(11,22)])
print(C[xx])

'''
字典在内存中的存储
C = {"name":"wocao", 100:10000}
C--->"name" 100

将键值名字通过哈希算法变成唯一的值
例如
name转化成唯一的值  这个值的内存空间存储"wocao" 
100 转化成另一个唯一值 这个值的内存空间存储10000 
所以 这个唯一的值是不可变的 如果可变 万一修改了 那就找不到值了 
'''



print("*"*10)
#函数传递引用
def func(a, b):
	print(id(a))
	print(a)
	#a  = a + a 
	a += a  #这两句话生成的结果不同 a+=a 是修改原来的列表
							#a = a+a是创建一个新列表 然后把结果存到当中
	print(id(a))
	print(a)

A = 10
print(id(A))
func(A,11)


B = [11,22]
print(id(B))
func(B,11)

#总结
#python传递参数参数都是引用   
#如果要是这个引用是不可变的 修改值就会新开辟空间
#如果要是这个引用是可变的 看怎么修改
#a += a 修改原来的
#a = a+a新开辟空间 然后把结果存到当中