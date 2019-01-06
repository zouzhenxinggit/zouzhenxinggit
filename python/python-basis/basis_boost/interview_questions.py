#!/usr/bin/python3
#coding=utf-8


print("interview_questions")


#请写出一段 Python 代码实现分组一个 list 里面的元素
#比如 [1,2,3,...100]变成 [[1,2,3],[4,5,6]....]
a = [x for x in range(1,101)]
b = [ a[i:i+3] for i in range(0,len(a),3)]
print(a)
print(b)





#请写出一段 Python 代码实现删除一个 list 里面的重复元素
list_tmp = [11,22,33,44,55,11,22,33,55,"a","b","a"]
print( list( set(list_tmp) ) )





#设计实现遍历目录与子目录,抓取.pyc 文件
import os
#os.walk(".")
#最后会生成元祖([],[],[])
#列表1:当前路径
#列表2:当前路径下目录
#列表3:当前路径下文件名

for tmp in os.walk("."):
	filename = tmp[2]
	for tmp2 in filename:
		position = tmp2.rfind(".")
		if not  position == -1:
			if tmp2[position:] == '.pyc':
				print(tmp2)



#写出一个函数,给定参数 n
#生成含有 n 个元素值为 1~n 的数 组,元素顺序随机,但值不重复
import random
import time
def test(num):
	new_list = []

	#new_list.append()
	while True:
		if len(new_list) == num:
			break

		tmp = random.randint(1,num)
		if not tmp in new_list:
			new_list.append(tmp)

	print(new_list)

test(10)



#内建类型 平时直接可用的函数 ipython3
#dir(__builtin__)

#s = "abcdefg"
#print(s[-2:-5])


#确省参数是可变的 有特性  初始化一次
def default(a,b=[],c={}):
	b.append(a)
	c[a] = a
	return b,c

list1 = default('a')   #(['a'],{'a':'a'})
list2 = default(100,["10","a","b"])	#([["10","a","b"],100],{'a':'a',100:100})
list3 = default(10) # (['a',10],{'a':'a',100:100,10:10})

print(list1)# (['a',10],{'a':'a',100:100,10:10})
print(list2)# (['10', 'a', 'b', 100], {10: 10, 100: 100, 'a': 'a'})
print(list3)# (['a',10],{'a':'a',100:100,10:10})

#b指向一块内存空间 由于b是列表是可变的 初始化一次 而不是在创建一个缺省值
#所以list1和list3也指向b空间  一个修改另一个也跟着修改了
 