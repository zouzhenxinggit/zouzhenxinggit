#!/usr/bin/python3
#coding=utf-8

print("catch_exceptions")

try:
	print(a)

except NameError:	#单异常
	print("NameError")
except (NameError,FileNotFoundError) as result: #多异常
	print("NameError,FileNotFoundError: %s" %result)
except Exception as result: #所有异常
	print("Exception") 
except:	#所有异常
	print("error")
else: #无异常
	print("not err")
finally:	#都会执行
	print("finally")


#ctrl+C属于KeyboardInterrupt异常