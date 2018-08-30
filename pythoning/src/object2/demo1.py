'''
Created on 2018年8月5日

@author: Administrator
'''

"""
使用__slots__
"""
from types import MethodType

class Student(object):
    # 限制属性
    __slots__ = ('name', 'score', 'set_age', 'age')
def set_age(self, age):
    self.age = age
s = Student()
# 单个
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

def set_score(self, score):
    self.score = score
# 全局
Student.set_score = set_score
# 属性限制  子类不受限制
# s.age = 1
class StudentChildern(Student):
    pass
sc = StudentChildern()
sc.sex = 2


