'''
Created on 2018年8月20日

@author: Administrator
'''


from sqlalchemy import Column, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class Order(Base):
    # 表的名字:
    __tablename__ = 'tb_order'
    # 表的结构:
    order_id = Column(String(50), primary_key=True)
#     payment = Column(String(50))
    # 一对多:
#     order_item = relationship('OrderItem')
    
# class OrderItem(Base):
#     # 表的名字:
#     __tablename__ = 'tb_order_item'
#     # 表的结构:
#     id = Column(String(20), primary_key=True)
#     title = Column(String(200))
#     # “多”的一方的book表是通过外键关联到user表的:
#     order_id = Column(String(20), ForeignKey('order.order_id'))
    
    
# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/yame?charset=utf8')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
order = session.query(Order).filter().all()
# user = session.query(User).filter(User.id==7).one()
for o in order:
    print(o)
    
    
    
    