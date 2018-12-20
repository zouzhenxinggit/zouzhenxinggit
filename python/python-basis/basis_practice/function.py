#!/usr/bin/python3
#coding=utf-8

def function():
	'''大佛镇楼图'''
	print ("                            _ooOoo_  ")
	print ("                           o8888888o  ")
	print ("                           88  .  88  ")
	print ("                           (| -_- |)  ")
	print ("                            O\\ = /O  ")
	print ("                        ____/`---'\\____  ")
	print ("                      .   ' \\| |// `.  ")
	print ("                       / \\||| : |||// \\  ")
	print ("                     / _||||| -:- |||||- \\  ")
	print ("                       | | \\\\\\ - /// | |  ")
	print ("                     | \\_| ''\\---/'' | |  ")
	print ("                      \\ .-\\__ `-` ___/-. /  ")
	print ("                   ___`. .' /--.--\\ `. . __  ")
	print ("                ."" '< `.___\\_<|>_/___.' >'"".  ")
	print ("               | | : `- \\`.;`\\ _ /`;.`/ - ` : | |  ")
	print ("                 \\ \\ `-. \\_ __\\ /__ _/ .-` / /  ")
	print ("         ======`-.____`-.___\\_____/___.-`____.-'======  ")
	print ("                            `=---='  ")
	print ("  ")

def func2(num1, num2):
	#function()
	return (num1 + num2) #只会执行第一个 
	return (num1 *  num2)

def func3():
	print("helo word")


ina = int(input("请输入第一个值"))
inb = int(input("请输入第二个值"))

print ( func2(ina, inb) )
num = func2(ina, inb)
print(num)

print(10*"*")
print ( func3() ) #没有返回值是None

def fun4():
	i = int(input("请输入一个值"))
	if i < 20:
		return 100
	else:
		return 200

print(fun4())


'''四种函数类型
无参数 无返回值
无参数 有返回值
有参数 无返回值
有参数 有返回值'''

def sum(num):
	#计算1-num的和
	i = 1
	s = 0
	while i <= num:
		s += i
		i += 1
		print(s)
	return s

result = sum(10);
print(result)



#函数的嵌套

def A():
	print("A")
	B()

#A() #no

def B():
	print("B")

A() #ok
#C() #no

def C():
	print("C")
C() #ok	

#若函数A调用了B A函数的调用位置必须在A和B函数定义之后 要不找不到

#函数名别重复 重复就会被覆盖
