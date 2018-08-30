'''
Created on 2018年8月4日

@author: Administrator
'''

"""
访问限制
"""

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def get_name(self):
        return self.__name
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError("error score")
    def print_score(self):
        print("%s:%s" % (self.__name, self.__score))

stu = Student("lmx", 85)
print(stu.__dict__)
# print(stu.__name)
print(stu.get_name())
print(stu._Student__name)
# stu.set_score(-1)
stu.__name = 'lx'
print(stu.__dict__)















