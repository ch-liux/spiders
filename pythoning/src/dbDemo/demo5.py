'''
Created on 2018年8月20日

@author: Administrator
'''

"""ORM"""

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()
# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'tb_user'
    # 表的结构:
    id = Column(String(20), primary_key=True)
    username = Column(String(50))
    password = Column(String(32))
    phone = Column(String(20))
    email = Column(String(50))
# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/yame')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter().all()
# user = session.query(User).filter(User.id==7).one()
for u in user:
    print(u.username, u.password, u.phone, u.email)
