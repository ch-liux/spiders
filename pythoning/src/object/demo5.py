'''
Created on 2018年8月5日

@author: Administrator
'''

"""
实例属性和类属性 
"""
class Student(object):
    name = 'Student'
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count += 1
    
s = Student('lmx')
print(s.name)
s.name = 'lxzy'
print(Student.name)
print(s.name)
del s.name
print(s.name)

for i in range(1, 5):
    temp = Student('lmx')
#     Student.count += 1
print(Student.count)
