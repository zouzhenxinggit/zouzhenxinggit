#!/usr/bin/python3
#coding=utf-8


print("list-str each other change")


#列表->str   str->列表

stuinfos = [{"name":"zouzx", "age":18}, {"name":"ghq","age":19}, {"name":"zouxj", "age":20}]
str_info = str(stuinfos)

print(str_info)
print(type(str_info))

str_info = eval(str_info)
print(str_info)
print(type(str_info))