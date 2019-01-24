#coding=utf-8

import MySQLdb


try:
    conn = MySQLdb.connect(host="localhost",port=3306,db='study',user='zouzhenxing',passwd='zouzhenxing',charset='utf8')
    cursor1 = conn.cursor()

    # 向表中插入数据
    # print cursor1.execute('insert into stu(name) values("张三")')

    # 修改表中数据
    # uname = raw_input("请输入用户名:")
    # ubirthday = raw_input("请输入生日")
    # params = [uname, ubirthday, 6]
    # sql = 'update stu set name=%s, birthday=%s where id=%s'
    # cursor1.execute(sql,params)

    #查询一行数据
    cursor1.execute("select count(*) from stu")
    num = cursor1.fetchone()
    print num[0]
    print "\n"

    #查询多行数据
    cursor1.execute("select * from stu")
    rows = cursor1.fetchall()

    for row in rows:
        for tmp in row:
            print tmp,
        print "\n"


    #更新数据的时候再提交 这是一个事务
    #conn.commit()
    cursor1.close()
    conn.close()

except Exception as result:
    print("this is Exception",result)


