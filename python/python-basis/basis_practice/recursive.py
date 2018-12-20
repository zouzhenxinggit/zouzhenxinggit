#!/usr/bin/python3
#coding=utf-8

print("recursive prative")

#1+2+3+...+100
#1*2*3*...*100

i = 1
resufls = 1
while i <= 100:
	resufls *= i
	i += 1

print(resufls)




def function(num):
	if num > 1:
		return num*function(num-1)
	else :
		return 1

print(function(100))