'''
Created on 2018年8月20日

@author: Administrator
'''

"""使用SQLite
"""

# 导入SQLite驱动:
import sqlite3
# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('test.db')
# 创建一个Cursor:
cursor = conn.cursor()
# 执行一条SQL语句，创建user表:
r = cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
print("r is %s" % str(r))
# 继续执行一条SQL语句，插入一条记录:
r = cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
print("r is %s" % str(r))
# 通过rowcount获得插入的行数:
r = cursor.rowcount
print("r is %s" % str(r))
# 关闭Cursor:
cursor.close()
# 提交事务:
conn.commit()
# 关闭Connection:
conn.close()





