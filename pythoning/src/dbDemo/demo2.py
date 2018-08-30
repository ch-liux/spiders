'''
Created on 2018年8月20日

@author: Administrator
'''

"""使用SQLite
"""

import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
r = cursor.execute("select * from user where id = ?", ('1',))
# cursor.execute('select * from user where name=? and pwd=?', ('abc', 'password'))
print("r is %s" % str(r))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()


