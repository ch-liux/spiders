'''
Created on 2018年8月4日

@author: Administrator
'''

"""
类和实例
"""

# class Student(object):
#     pass
# 
# stu = Student()
# print(stu)
# print(Student)
# 
# stu.name = "lmx"
# print(stu.name)
# print(stu.__dict__)
# print(type(stu))
# print(Student.__dict__)

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s:%s' % (self.name, self.score))
    
print(Student.__dict__)
stu = Student('lmx', 85)
print(stu.name)
print(stu.__dict__)
print(Student.__dict__)

def print_score(stu):
    print('%s:%s' % (stu.name, stu.score))

print_score(stu)
stu.print_score()
stu.age = 8
print(stu.age)







