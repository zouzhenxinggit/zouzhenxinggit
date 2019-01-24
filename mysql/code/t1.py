#coding=utf-8

from MysqlHelper import *



mysql = MysqlHelper("localhost", 3306, "study", "zouzhenxing", "zouzhenxing")

sql1 = 'select count(*) from stu'
sql2 = 'select * from stu'
sql3 = 'insert into stu values(5,"郭芙",0,"襄阳","1996-10-15",0)'


print mysql.insert(sql3)
rows1 = mysql.fetchone(sql1)
rows2 = mysql.fetchall(sql2)


print rows1[0]
print "\n"

for row in rows2:
    for tmp in row:
        print tmp

