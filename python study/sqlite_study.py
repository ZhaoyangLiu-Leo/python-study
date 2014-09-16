#-*- coding:utf-8 -*-

import sqlite3

#创建链接
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
#cursor.execute('create table user(id varchar(20) primary key, name varchar(20))')

#cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# 通过rowcount获得插入的行数
print cursor.rowcount

#如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，有几个?占位符就必须对应几个参数
cursor.execute('select * from user where id=?', '1')

values = cursor.fetchall()

print type(values)
print values
cursor.close()
conn.commit()
conn.close()
