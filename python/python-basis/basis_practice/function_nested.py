#!/usr/bin/python3
#coding=utf-8


def print_line():
	print("*"*30)


def print_lines(num):
	i = 0
	while i < num:
		print("*"*30)
		i += 1 

print_lines(5)


'''
求三个数的和
求三个数的平均数'''

def calculation_num(num1, num2, num3):
	return num1+num2+num3

def calculation_average(num1, num2, num3):
	return calculation_num(num1, num2, num3)/3

def main():
	num1 = int(input("输入第一个值"))
	num2 = int(input("输入第二个值"))
	num3 = int(input("输入第三个值"))

	sums = calculation_num(num1, num2, num3)
	print("三个数的和为%d" %sums)

	average = calculation_average(num1, num2, num3)
	print("三个数的平均数%d" %average)

main()

